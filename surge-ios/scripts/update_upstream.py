#!/usr/bin/env python3
"""Stage official files for review, then explicitly apply the reviewed transaction."""
import argparse, datetime, difflib, hashlib, json, os, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
MAP = {'SKILL.md':'references/upstream-SKILL.md', 'references/command-reference.md':'references/command-reference.md', 'references/plugin-authoring.md':'references/plugin-authoring.md', 'agents/openai.yaml':'agents/openai.yaml', 'assets/logo.png':'assets/logo.png'}
def sha(data): return hashlib.sha256(data).hexdigest()
def put(p,data):
    p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+'.update-tmp'); t.write_bytes(data); t.chmod(0o644); t.replace(p)
def current(p): return sha(p.read_bytes()) if p.exists() else None
def run(args): return subprocess.check_output(args,stderr=subprocess.PIPE)
def prepare(args):
    folder=Path('/var/minis/workspace/surge-updates')/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    folder.mkdir(parents=True); raw=folder/'raw'; staged=folder/'staged'
    version=args.version
    for src,dst in MAP.items():
        p=raw/src; p.parent.mkdir(parents=True,exist_ok=True)
        if args.source:
            p.write_bytes((Path(args.source)/src).read_bytes())
        else:
            run(['scp','-q','-oBatchMode=yes','-oConnectTimeout=10',args.host+':/Applications/Surge.app/Contents/Resources/Skills/surge/'+src,str(p)])
        put(staged/dst,p.read_bytes())
    if not args.source:
        version=run(['ssh','-oBatchMode=yes','-oConnectTimeout=10',args.host,'/Applications/Surge.app/Contents/Applications/surge-cli version']).decode().strip()
    if not version: raise SystemExit('Explicit --version required for local source')
    diff=[]
    for src,dst in MAP.items():
        old=ROOT/dst; new=raw/src
        if new.suffix in ('.md','.yaml'):
            diff.extend(difflib.unified_diff(old.read_text().splitlines(True) if old.exists() else [],new.read_text().splitlines(True),fromfile=dst,tofile='raw/'+src))
    (folder/'review.diff').write_text(''.join(diff))
    print('Review directory:',folder,flush=True)
    # Unknown references stop here; raw evidence and diff survive failure.
    subprocess.run(['python3',str(ROOT/'scripts/adapt_upstream_reference.py'),str(staged/'references/command-reference.md')],check=True)
    put(staged/'references/upstream-command-reference.md',(raw/'references/command-reference.md').read_bytes())
    provenance={'source':args.source or args.host,'version_report':version,'retrieved_at':datetime.datetime.now().isoformat(),'raw_sha256':{s:current(raw/s) for s in MAP},'runtime_validation':'not performed'}
    put(staged/'references/upstream-manifest.json',json.dumps(provenance,indent=2).encode())
    files={str(p.relative_to(staged)):{'before':current(ROOT/p.relative_to(staged)),'after':current(p)} for p in staged.rglob('*') if p.is_file()}
    doc=ROOT/'references/SOURCE.md'
    files['references/SOURCE.md']={'before':current(doc),'after':current(doc)}
    put(staged/'references/SOURCE.md',doc.read_bytes())
    (folder/'transaction.json').write_text(json.dumps({'files':files,'adapter':current(ROOT/'scripts/adapt_upstream_reference.py')},indent=2))
    print('Prepared; active skill unchanged. Inspect review.diff, raw/, staged/ before apply.')
def apply(args):
    folder=Path(args.directory).resolve(); tx=json.loads((folder/'transaction.json').read_text()); files=tx['files']
    allowed=set(MAP.values())|{'references/upstream-command-reference.md','references/upstream-manifest.json','references/SOURCE.md'}
    if set(files)!=allowed: raise SystemExit('Invalid transaction file list')
    if tx['adapter']!=current(ROOT/'scripts/adapt_upstream_reference.py'): raise SystemExit('Adapter changed; prepare again')
    for name,h in files.items():
        if current(ROOT/name)!=h['before'] or current(folder/'staged'/name)!=h['after']: raise SystemExit('Changed since prepare: '+name)
    backup=folder/'backup'; backup.mkdir() # refuse reapplication
    for name,h in files.items():
        if h['before'] is not None: put(backup/name,(ROOT/name).read_bytes())
    (folder/'state').write_text('applying')
    touched=[]
    try:
        for name in files:
            touched.append(name); put(ROOT/name,(folder/'staged'/name).read_bytes())
    except BaseException:
        for name in reversed(touched):
            if files[name]['before'] is None: (ROOT/name).unlink(missing_ok=True)
            else: put(ROOT/name,(backup/name).read_bytes())
        (folder/'state').write_text('rolled-back'); raise
    (folder/'state').write_text('applied')
    print('Applied. Backup:',backup,'; runtime not tested. Review local capability notes separately.')
p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='action',required=True)
s=sub.add_parser('prepare'); s.add_argument('--host',default='macmini'); s.add_argument('--source'); s.add_argument('--version')
s=sub.add_parser('apply'); s.add_argument('directory')
a=p.parse_args()
if a.action=='prepare': prepare(a)
else: apply(a)
