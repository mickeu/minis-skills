---
name: Hyperframes CLI
version: 1.0.0
description: >
  HyperFrames CLI and Minis rendering. Use for: (1) CLI commands — init, add, catalog,
  capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats,
  keyframes, single or batch render, publish, cloud, cloudrun, feedback, lambda, doctor,
  browser, info, upgrade, skills, compositions, timeline, history, clean, docs, benchmark,
  telemetry, transcribe, auth, tts, remove-background; (2) Minis iOS rendering
  (set_viewport + minis-browser-use + ffmpeg, no Chrome required); (3) Website-to-video
  workflow — capture a URL and produce a professional MP4 in 7 steps; (4) Preview/snapshot
  compositions at correct resolution. validate, inspect, and layout are deprecated aliases;
  use check. Trigger when user says render, init project, lint, check, transcribe audio,
  generate TTS, capture a website for video, or run any hyperframes CLI command.
source: |
  Adapted from the official HyperFrames CLI and website-to-hyperframes skills by HeyGen.
  Originals:
    https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-cli
    https://github.com/heygen-com/hyperframes/tree/main/skills/website-to-hyperframes
  Original license: Apache-2.0 (https://github.com/heygen-com/hyperframes/blob/main/LICENSE)
  Minis adaptation: Merged hyperframes-cli + website-to-hyperframes into a single skill,
  added Minis iOS rendering notes (minis-browser-use set_viewport + ffmpeg) and dependency
  management guidance.
  Adapter copyright: OpenMinis contributors, MIT License.
source_url: https://github.com/heygen-com/hyperframes
license: Apache-2.0
cli_version: v0.8.104
last_sync: 2026-10-01
---
# HyperFrames CLI

## Environment Check (Run First)

Before any task, verify the environment is ready:

- `minis-browser-use` — built-in Minis tool for browser control (required for rendering and preview)
- `ffmpeg` — video encoding (`ffmpeg -version`)
- `hyperframes` / `hyperframes-cli` skills — this skill itself
- Node.js >= 22 — required by the `npx hyperframes` CLI

**If `minis-browser-use` is missing**: it is a Minis built-in tool. Update Minis App to the latest version — it ships with the app and cannot be installed separately.

**If a skill is missing**, reinstall it from the upstream repository:
```bash
git clone --depth 1 https://github.com/heygen-com/hyperframes.git /tmp/hyperframes
# copy skills/hyperframes and skills/hyperframes-cli into /var/minis/skills/
```

**If Node.js or FFmpeg is missing**, install them (e.g. `apk add nodejs ffmpeg` on Alpine/iSH) before running CLI commands.

Everything runs through `npx hyperframes`. Requires Node.js >= 22 and FFmpeg.

## Workflow

1. **Scaffold** — `npx hyperframes init my-video`
2. **Write** — author HTML composition (see the `hyperframes` skill)
3. **Lint** — `npx hyperframes lint` (after first HTML pass and structural changes)
4. **Check** — `npx hyperframes check` (the final gate; reruns lint, then audits runtime errors, failed requests, layout, `*.motion.json` assertions, and WCAG contrast in one browser pass). Do not prepend a redundant standalone `lint` — `check` already runs it.
5. **Preview** — `npx hyperframes preview`
6. **Render** — `npx hyperframes render` (only after approval)

`check` is the maintained final gate. `validate`, `inspect`, and `layout` are deprecated aliases kept for old scripts — use `check` in new instructions. Lint before preview catches missing `data-composition-id`, overlapping tracks, unregistered timelines.

## Scaffolding

```bash
npx hyperframes init my-video                        # interactive wizard
npx hyperframes init my-video --example warm-grain   # pick an example
npx hyperframes init my-video --video clip.mp4        # with video file
npx hyperframes init my-video --audio track.mp3       # with audio file
npx hyperframes init my-video --non-interactive       # skip prompts (CI/agents)
```

Templates: `blank`, `warm-grain`, `play-mode`, `swiss-grid`, `vignelli`, `decision-tree`, `kinetic-type`, `product-promo`, `nyt-graph`.

`init` creates the right file structure, copies media, transcribes audio with Whisper, and installs AI coding skills. Use it instead of creating files by hand.

## Linting

```bash
npx hyperframes lint                  # current directory
npx hyperframes lint ./my-project     # specific project
npx hyperframes lint --verbose        # info-level findings
npx hyperframes lint --json           # machine-readable
```

Lints `index.html` and all files in `compositions/`. Reports errors (must fix), warnings (should fix), and info (with `--verbose`).

## Check (final gate)

```bash
npx hyperframes check                  # lint + runtime audit + WCAG contrast
npx hyperframes check --snapshots       # add annotated overview frames and finding crops
npx hyperframes check --strict          # gate on warnings (not just errors)
npx hyperframes check --json            # machine-readable
```

`check` reruns lint first, then uses one browser session and one seek pass to audit runtime errors, failed requests, layout, `*.motion.json` assertions, and WCAG contrast. Persistent findings gate the exit code; transient entrance/exit findings are informational. Run it before previewing/rendering. Do not prepend a redundant standalone `lint` — `check` already runs it.

### Deprecated aliases

`validate`, `inspect`, and `layout` are deprecated aliases kept for old scripts. `check` is the one that is maintained, and it is what every reference in this skill assumes. Do not use the deprecated names in new instructions or scripts.

## Previewing

```bash
npx hyperframes preview                   # serve current directory
npx hyperframes preview --port 4567       # custom port (default 3002)
```

Hot-reloads on file changes. Opens the studio in your browser automatically.

### 🍎 Minis (iOS) Alternative — Preview & Snapshot

Set viewport to composition size first, then navigate. This gives accurate preview at the correct resolution.

```bash
# Preview at correct resolution
minis-browser-use set_viewport --width 960 --height 540
minis-browser-use navigate --url minis://workspace/<project>/index.html

# Snapshot at specific timestamps
minis-browser-use execute_js --script 'window.__hf.seek(2.5)'
minis-browser-use screenshot   # saves to /var/minis/browser/
```

Always `set_viewport` before navigating — otherwise the browser uses the phone's default viewport and the composition renders at the wrong scale.

## Rendering

```bash
npx hyperframes render                                # standard MP4
npx hyperframes render --output final.mp4             # named output
npx hyperframes render --quality draft                # fast iteration
npx hyperframes render --fps 60 --quality high        # final delivery
npx hyperframes render --format webm                  # transparent WebM
npx hyperframes render --docker                       # byte-identical
```

| Flag           | Options               | Default                    | Notes                       |
| -------------- | --------------------- | -------------------------- | --------------------------- |
| `--output`     | path                  | renders/name_timestamp.mp4 | Output path                 |
| `--fps`        | 24, 30, 60            | 30                         | 60fps doubles render time   |
| `--quality`    | draft, standard, high | standard                   | draft for iterating         |
| `--format`     | mp4, webm             | mp4                        | WebM supports transparency  |
| `--workers`    | 1-8 or auto           | auto                       | Each spawns Chrome          |
| `--docker`     | flag                  | off                        | Reproducible output         |
| `--gpu`        | flag                  | off                        | GPU-accelerated encoding    |
| `--strict`     | flag                  | off                        | Fail on lint errors         |
| `--strict-all` | flag                  | off                        | Fail on errors AND warnings |

**Quality guidance:** `draft` while iterating, `standard` for review, `high` for final delivery.

### 🍎 Minis (iOS) — 手动渲染流程

`npx hyperframes render` requires Puppeteer + Chrome (unavailable on iOS). Use the Minis-native flow instead: `minis-browser-use set_viewport` locks the browser to the exact composition size, capture frames at Retina resolution, then encode with FFmpeg.

**Manual render steps:**
1. `minis-browser-use set_viewport --width W --height H` — use the composition's `data-width`/`data-height`
2. `minis-browser-use navigate --url minis://workspace/<project>/index.html`
3. Wait for `window.__hf` (`{ duration, seek }`) — works with GSAP and pure CSS animations
4. For each frame: `minis-browser-use execute_js --script 'window.__hf.seek(t)'` → `minis-browser-use screenshot` → save JPEG
5. Encode with FFmpeg: `ffmpeg -framerate 24 -i frames/%04d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4`
6. `minis-browser-use set_viewport --reset` — always run, even on error

**Suggested settings:**

| Setting | Options | Default | Notes |
|---|---|---|---|
| FPS | 24, 30 | 24 | 30fps increases render time ~25% |
| Bitrate | 2/4/8 Mbps | 4 Mbps | draft=2Mbps, standard=4Mbps, high=8Mbps |
| Output | path | `<project>/renders/output.mp4` | Output path |

**How it works:**
1. `set_viewport W H` — locks browser CSS viewport to composition size
2. Navigate to `minis://workspace/<rel-path>/index.html` (supports subdirectories)
3. Wait for `window.__hf` (`{ duration, seek }`) — works with GSAP and pure CSS animations
4. For each frame: `execute_js __hf.seek(t)` → `screenshot --with-base64` → save JPEG
5. Frames captured at Retina resolution (e.g. 2880×1620 for 960×540 @ DPR=3)
6. `ffmpeg` lanczos-downscale → MP4 (h264_videotoolbox, fallback libx264)
7. `set_viewport --reset` always runs — even on error or Ctrl-C

**Performance:** ~10fps capture (~12s for a 5s@24fps video on iPhone).

**Requirements for `index.html`:**

The composition MUST expose `window.__hf` at the end of its `<script>` block:

```js
// Required: __hf render protocol
const DURATION = 5.0; // seconds — must match your actual animation length
window.__hf = {
  get duration() { return DURATION; },
  seek(t) { tl.pause(); tl.seek(Math.max(0, Math.min(t, DURATION)), false); }
};
window.__playerReady = true;
window.__renderReady = true;
```

**DURATION must equal the GSAP timeline's actual duration.** If ambient animations use `repeat`, calculate carefully:

```js
// WRONG — glow-gold ends at 0.4 + 2.0*(2+1) = 6.4s, timeline extends past 5s → black frames
tl.to("#glow", { duration: 2.0, repeat: 2, yoyo: true }, 0.4);

// CORRECT — calculate max repeats that fit within DURATION
const DURATION = 5.0;
tl.to("#glow", {
  duration: 2.0,
  repeat: Math.floor((DURATION - 0.4) / 2.0) - 1,  // = 1 repeat, ends at 4.4s
  yoyo: true
}, 0.4);
```

**HTML template rules (required for correct rendering):**
- Fixed `width/height` on `html`, `body`, and `#stage` — match `data-width`/`data-height`
- No `<meta name="viewport">` — the renderer sets viewport externally via `set_viewport`
- No scale wrappers, no `transform: scale()` on the stage — these break pixel accuracy
- Project must be under `/var/minis/workspace/` — the renderer converts the path to a `minis://` URL
- **Multi-scene layout: use `position:absolute; inset:0` per scene** — see note below

> **⚠️ Minis layout difference from standard HyperFrames:**
> The standard skill says `.scene-content` should use `width:100%; height:100%`. In Minis/iOS
> WebKit, `set_viewport` sets the CSS viewport *width* but iOS Safari's height is influenced by
> system UI, so `height:100%` on a flex container can exceed the stage height. Content then
> centers relative to that oversized container and lands outside the screenshot crop.
>
> **Fix:** for compositions with multiple sequential scenes, give each scene its own
> `position:absolute; inset:0` container (see the `hyperframes` skill → "Multi-scene compositions"
> section). For single-scene compositions, `width:100%; height:100%` is fine.

```html
<!-- Correct HTML structure -->
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<!-- NO viewport meta -->
<style>
  html, body { margin: 0; padding: 0; width: 960px; height: 540px; overflow: hidden; }
  #stage { width: 960px; height: 540px; position: relative; overflow: hidden; }
</style>
</head>
<body>
<div id="stage" data-composition-id="my-comp" data-width="960" data-height="540">
  <!-- content -->
</div>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script>
  window.__timelines = window.__timelines || {};
  const DURATION = 5.0;
  const tl = gsap.timeline({ paused: true });
  // ... tweens ...
  window.__timelines["my-comp"] = tl;

  window.__hf = {
    get duration() { return DURATION; },
    seek(t) { tl.pause(); tl.seek(Math.max(0, Math.min(t, DURATION)), false); }
  };
  window.__playerReady = true;
  window.__renderReady = true;
</script>
</body>
</html>
```

## Transcription

```bash
npx hyperframes transcribe audio.mp3
npx hyperframes transcribe video.mp4 --model medium.en --language en
npx hyperframes transcribe subtitles.srt   # import existing
npx hyperframes transcribe subtitles.vtt
npx hyperframes transcribe openai-response.json
```

## Text-to-Speech

```bash
npx hyperframes tts "Text here" --voice af_nova --output narration.wav
npx hyperframes tts script.txt --voice bf_emma
npx hyperframes tts --list  # show all voices
```

## Troubleshooting

```bash
npx hyperframes doctor       # check environment (Chrome, FFmpeg, Node, memory)
npx hyperframes browser      # manage bundled Chrome
npx hyperframes info         # version and environment details
npx hyperframes upgrade      # check for updates
```

Run `doctor` first if rendering fails. Common issues: missing FFmpeg, missing Chrome, low memory.

## Command reference

Beyond the core loop (init → lint → check → preview → render), the CLI exposes:

```bash
# Project & catalog
npx hyperframes add <name>                # install a registry block/component
npx hyperframes catalog --query "reveal a headline one line at a time"  # local move search (nothing sent)
npx hyperframes catalog --query "..." --on-device   # meaning-ranked search (~33 MB one-time download)
npx hyperframes compositions              # list compositions in project
npx hyperframes timeline --json           # tracks, clips, starts, ends — prefer --json over text
npx hyperframes history begin --who <name> --label "..."   # start an undoable turn
npx hyperframes history --since mine --who <name>          # see changes since your last turn
npx hyperframes history undo --who <name>                  # undo your newest turn
npx hyperframes history end               # close the turn
npx hyperframes clean [--dry-run]         # remove dead renders and idle caches
npx hyperframes skills update <name>      # install/refresh a workflow skill

# Inspection & snapshots
npx hyperframes snapshot --at 1,2.5,5     # capture frames at timestamps
npx hyperframes compare a.mp4 b.mp4       # diff two renders
npx hyperframes grade-compare a.mp4 b.mp4 # perceptual grade comparison

# Studio & presentation
npx hyperframes play                      # play timeline in Studio
npx hyperframes present <dir> --port 3004 # navigable deck with presenter/audience sync
npx hyperframes beats <dir> --json        # Studio beat-grid utility
npx hyperframes keyframes <dir> --json    # animation trajectory / motion-path diagnostics

# Rendering at scale
npx hyperframes render --batch rows.json --output "renders/{name}.mp4"  # variable-driven batch
npx hyperframes publish                   # publish a render
npx hyperframes cloud render              # HeyGen-hosted zero-infrastructure render
npx hyperframes lambda render <proj> --width 1920 --height 1080 --wait   # self-managed AWS
npx hyperframes cloudrun render <proj> --width 1920 --height 1080 --wait # self-managed GCP

# Media & feedback
npx hyperframes transcribe audio.mp3                # Whisper transcription
npx hyperframes tts "text" --voice af_nova          # Kokoro-82M TTS
npx hyperframes remove-background image.png         # background removal
npx hyperframes auth                    # HeyGen account auth (cloud / template variables)
npx hyperframes feedback --rating 8 --comment "..." # submit a render report
npx hyperframes feedback --search-miss "<query>" --wanted "<move>" --tier <tier>  # report a catalog gap
npx hyperframes telemetry               # telemetry status
npx hyperframes benchmark .             # benchmark render performance

# Environment
npx hyperframes doctor       # check environment (Chrome, FFmpeg, Node, memory)
npx hyperframes browser      # manage bundled Chrome
npx hyperframes info         # version and environment details
npx hyperframes upgrade      # check for / apply updates
npx hyperframes docs         # open documentation
```

> **Note:** `events` is the telemetry endpoint skills use to report their **own** invocation — agents have no reason to call it by hand.

---

## Website → Video Workflow

Turn any URL into a video in 7 steps:

| Step | What |
|------|------|
| 1 | Capture website (screenshots, tokens, assets) |
| 2 | Write DESIGN.md (brand colors, fonts, style) |
| 3 | Write SCRIPT.md (narration, scene durations) |
| 4 | Write STORYBOARD.md (per-beat creative direction) |
| 5 | Generate VO + map word timestamps to beats |
| 6 | Build compositions (use the `hyperframes` skill) |
| 7 | Lint, snapshot, render, handoff |

**Visual techniques:** SVG drawing, Canvas 2D, 3D, typing, MotionPath, Lottie — apply them directly in the composition HTML.

### Quick formats

| Type | Duration | Beats | Narration |
|---|---|---|---|
| Social ad (IG/TikTok) | 10-15s | 3-4 | Optional |
| Product demo | 30-60s | 5-8 | Full |
| Feature announcement | 15-30s | 3-5 | Full |
| Brand reel | 20-45s | 4-6 | Optional |

Landscape: 1920×1080 · Portrait: 1080×1920 · Square: 1080×1080
