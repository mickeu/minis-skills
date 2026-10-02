> For the complete documentation index, see [llms.txt](https://kb.nssurge.com/surge-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://kb.nssurge.com/surge-knowledge-base/guidelines/remote-management.md).

# Surge Remote Management

Manage Surge running on another Mac, iPhone, iPad, or Apple TV with Surge iOS, Surge Dashboard, or surge-cli.

Surge can be managed from another device. You can view requests from your iPhone on a Mac, switch policy groups on a headless Mac mini from your iPhone, check an Apple TV from anywhere, or script a remote Surge instance from the terminal.

Surge offers three ways to do this:

* **External Controller**: the native remote management channel. Surge iOS, Surge Dashboard, and surge-cli all use it. It is the most complete option, and this guide focuses on it.
* **HTTP API**: a REST-style interface for your own scripts and automation tools.
* **Web Dashboard**: a browser-based panel served through the HTTP API.

If you just want to manage another Surge device, use the External Controller.

## Controllers and Controlled Instances

Remote management always involves two roles:

* **The controlled instance**: the Surge you want to manage. This can be Surge Mac, Surge iOS (iPhone and iPad), or Surge tvOS.
* **The controller**: the app you use to manage it. This can be:
  * **Surge iOS**: from the Remote Controller section on the Utilities page.
  * **Surge Dashboard**: the app included with Surge Mac.
  * **surge-cli**: the command-line tool included with Surge Mac.

All three controllers use the same protocol, so any of them can manage any instance. A controller can also manage the Surge instance on its own device. For example, Surge Dashboard and surge-cli connect to the local Surge Mac with no setup.

| Controlled instance | Surge iOS | Surge Dashboard  | surge-cli |
| ------------------- | --------- | ---------------- | --------- |
| Surge Mac           | ✅         | ✅                | ✅         |
| Surge iOS           | ✅         | ✅ (Wi-Fi or USB) | ✅         |
| Surge tvOS          | ✅         | ✅                | ✅         |

## Choosing a Connection Method

### A. Surge Ponte (recommended for Mac and Apple TV)

If the controlled device is a Surge Mac or Surge tvOS acting as a [Surge Ponte](/surge-knowledge-base/guidelines/ponte.md) server, this is the easiest option:

* No address, port, or password is needed. The device appears automatically on every Surge iOS device signed in to the same iCloud account.
* It works from any network, including cellular and networks away from home.
* The connection is always end-to-end encrypted.

### B. External Controller over the local network

Turn on the External Controller on the controlled device and set a port and password. Controllers on the same network can then connect with the device's IP address, the port, and the password. This works for Surge Mac, Surge iOS, and Surge tvOS.

### C. USB (Surge iOS only)

When an iPhone or iPad is connected to a Mac with a cable, Surge Dashboard can connect over USB. This does not require Wi-Fi and is the only way to inspect traffic while the iPhone is using cellular data.

{% hint style="info" %}
You can combine methods. For example, if both ends run Surge with Ponte, you can connect Surge Dashboard or surge-cli to `ponte-name.sgponte` to reach the External Controller of a Mac at home from anywhere. See [Tips](#tips) below.
{% endhint %}

## Setting Up the Controlled Device

### Surge Mac

**Via Surge Ponte**

1. Turn on Surge Ponte as described in the [Surge Ponte Guide](/surge-knowledge-base/guidelines/ponte.md).
2. In the setup wizard, keep **Allow remote controller by other devices via Surge Ponte** selected.

The Mac then appears in the Remote Controller list in Surge iOS on your other devices. No password is needed.

**Via the External Controller**

1. Open **Settings › General**, and find the **External Controller** section.
2. Set a TCP port (default: 6170) and an access password.
3. Turn on **Allow** to accept connections from other devices. If you leave it off, only controllers on the same Mac, such as a local surge-cli or Dashboard, and connections through Surge Ponte can connect.

### Surge iOS

Surge iOS cannot be a Surge Ponte server, so it can only be managed through the External Controller:

1. On the Home page, open **More Settings**, then find the External Controller option in the **Remote Control** section.
2. Turn it on and set the port and password.
3. By default, only USB connections are allowed. To allow controllers on the same Wi-Fi network, turn on **Allow Access From Wi-Fi**.

{% hint style="warning" %}
For security reasons, Surge iOS always rejects External Controller connections from cellular networks. To manage an iPhone that is using cellular data, connect it to a Mac with a USB cable.
{% endhint %}

The External Controller is available only while Surge is running.

### Surge tvOS

Surge tvOS does not have its own control interface, and it is designed to be managed remotely. After you deploy it with Surge iOS, the Apple TV automatically appears in the Remote Controller list of Surge iOS through Surge Ponte. If you do not need to access the Apple TV from outside your home, you can set Surge Ponte to LAN-Only. See [Surge tvOS](/surge-knowledge-base/guidelines/tvos.md).

### Profile Syntax

The External Controller is stored in the `[General]` section of the profile, so you can also set it directly:

```
[General]
external-controller-access = MyPassword@0.0.0.0:6170
```

The value uses the format `password@address:port`. All three parts are required.

* `127.0.0.1`: accept local connections only. On Surge iOS, this means USB only.
* `0.0.0.0`: also accept connections from the local network. On Surge iOS, this means Wi-Fi.

## Connecting from a Controller

### From Surge iOS

Open the **Utilities** page and find the **Remote Controller** section:

* Surge Mac and Apple TV devices available through Surge Ponte are listed automatically, labeled "via Surge Ponte".
* To connect to a device on the local network, tap **Remote Controller**, enter its IP address, port, and password, and then tap **Connect**.

After you connect, you can add the device to **Favorites** for one-tap access later. You can also add a **Home Screen shortcut** for a favorite device to open its controls directly.

### From Surge Dashboard

Surge Dashboard opens the local Surge Mac by default. To manage another device, choose **New Connection** and then:

* **Remote**: enter the host, port, and password. You can save frequently used devices and open them again from the saved list or the Dock menu.
* **USB**: choose a connected iPhone or iPad, and enter the port and password configured on that device.

{% hint style="success" %}
When Surge iOS is running with the External Controller allowed on Wi-Fi, the iPhone offers a **Handoff** item to nearby Macs. Click it in the Mac Dock to open Surge Dashboard and connect to the iPhone automatically.
{% endhint %}

### From surge-cli

surge-cli is located at `/Applications/Surge.app/Contents/Applications/surge-cli`. Without extra parameters, it controls the local Surge Mac. Add `--remote` to control another instance:

```
surge-cli --remote 192.168.1.20:6170 status
```

To keep the password out of your shell history, enter it at the secure prompt, set the `SURGE_CLI_PASSWORD` environment variable, or pass it with `--password-stdin`. Do not put the password on the command line.

Running surge-cli without a command starts interactive mode, which supports auto-completion. See the [Surge CLI documentation](https://manual.nssurge.com/others/cli.html) for all commands.

{% hint style="info" %}
Surge iOS also includes a **Terminal** that accepts the same commands as surge-cli. It is available for the local instance on the Utilities page and for each remote device in its Remote Controller menu.
{% endhint %}

## What You Can Do Remotely

After you connect, you can manage Surge much as you would on the device itself:

* **Monitor**: recent and active requests, real-time traffic statistics, events, the DNS cache, and Logbook records.
* **Routing**: switch the outbound mode, change policy group selections, test policies, and view and edit rules.
* **Temporary rules**: add rules that take effect immediately and are discarded when Surge stops. They are useful for debugging.
* **Feature switches**: turn MitM, Rewrite, Scripting, HTTP Capture, and other features on or off.
* **Profiles and resources**: switch profiles, enable or disable modules, update external resources, and update managed profiles.
* **Diagnostics**: run network diagnostics, DNS lookups, rule match analysis, and more (mostly in the terminal).
* **Maintenance**: reload the profile or restart the engine.

When the controlled device is a **Surge Mac**, you can also:

* Manage [Gateway Mode](/surge-knowledge-base/guidelines/gateway.md) devices, including assigning static IPs, renaming devices, changing icons, and reconnecting devices.
* Edit the rules in the Mac profile.
* Manage plugins.
* Perform an unattended upgrade of Surge Mac, which updates and restarts it without anyone at the Mac.

{% hint style="warning" %}
Remote management works best when both devices run the latest version. If the controller warns about a version mismatch, some features may be unavailable or unstable. If you use a beta build on one device, use the beta on the other device too.
{% endhint %}

## Security

The External Controller gives full control of Surge, so protect it carefully:

* **Use it only on trusted networks.** An External Controller connection over the local network is not encrypted. Do not expose the External Controller port to the internet, such as through router port forwarding or DMZ. To manage a device from outside the local network, use Surge Ponte, which is always end-to-end encrypted.
* **Use a strong password.**
* **Protection against password guessing**: After 10 failed password attempts within 30 seconds, Surge temporarily bans the source IP address, or the local process, and shows an "Unauthorized access" warning. You can view or clear bans with `surge-cli security ban`.
* On Surge iOS, connections from cellular networks are always rejected, and Wi-Fi connections are rejected unless you allow them.

## Comparison with the HTTP API and Web Dashboard

Surge also provides an [HTTP API](https://manual.nssurge.com/others/http-api.html) and a Web Dashboard. They cover common tasks such as switching policies, toggling features, and viewing requests, but they are less complete than the External Controller.

|                           | External Controller                                          | HTTP API                   | Web Dashboard            |
| ------------------------- | ------------------------------------------------------------ | -------------------------- | ------------------------ |
| Used by                   | Surge iOS, Surge Dashboard, surge-cli                        | Your own scripts and tools | A web browser            |
| Scope                     | The most complete: nearly everything available on the device | Common operations          | Common operations        |
| Works through Surge Ponte | ✅                                                            | ❌                          | ❌                        |
| USB connection            | ✅ (Surge iOS)                                                | ❌                          | ❌                        |
| Profile option            | `external-controller-access`                                 | `http-api`                 | `http-api-web-dashboard` |

Use the HTTP API for integrations with other tools, and the Web Dashboard for quick access from a device without Surge. For day-to-day management of your own devices, use the External Controller.

## Tips

1. **Use surge-cli or Dashboard through Surge Ponte.** If both the controller Mac and the controlled Mac run Surge with Surge Ponte, you can use `ponte-name.sgponte` as the host, for example `surge-cli --remote mymacmini.sgponte:6170 status`. The connection is sent through the encrypted Ponte tunnel. Because `.sgponte` resolves to 127.0.0.1 on the remote device, the External Controller on the controlled Mac can remain restricted to `127.0.0.1` and does not need to be exposed to the local network.
2. **Headless Mac mini.** On a Mac used as a home gateway, turn on Surge Ponte with remote control allowed. You can then manage it, including [Gateway Mode](/surge-knowledge-base/guidelines/gateway.md) devices and unattended upgrades, from your iPhone anywhere.
3. **Debug an iPhone from a Mac.** Connect the iPhone with a USB cable and open it in Surge Dashboard. You can inspect every request on the larger screen, even while the iPhone is using cellular data.

## Troubleshooting

* **The device does not appear in the list.** Make sure both devices are signed in to the same iCloud account, Surge Ponte is enabled on the Mac or Apple TV, and remote control was allowed during Ponte setup.
* **Cannot connect to Surge iOS.** Make sure Surge is running on the iPhone, the External Controller is turned on, and **Allow Access From Wi-Fi** is on if you are connecting over Wi-Fi. Also confirm that both devices are on the same Wi-Fi network.
* **Password incorrect.** Check the password. If you entered it incorrectly several times in a row, wait a moment or clear the ban on the controlled device before trying again.
* **Some features are missing.** The controlled device may run an older version, or the feature may be available only on Surge Mac, such as Gateway Mode device management. Update Surge on both devices.
