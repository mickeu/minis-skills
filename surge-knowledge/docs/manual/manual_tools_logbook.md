# Logbook {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }}

Logbook persistently records Surge events so they remain available after Surge is closed. The current version keeps the most recent 7 days of events by default.

Surge records Logbook entries for events such as profile reloads, network switching, crash recovery, updates, and DHCP-related changes. More event types may be added in future versions.

## Remote Viewing

[Surge Dashboard](dashboard.md) can read Logbook content from remote Surge Mac and Surge iOS instances. Script-type records support remote viewing of input, output, and log output.

Logbook records can also be read from the command line with `surge-cli logbook`; see [Surge CLI](cli.md).
