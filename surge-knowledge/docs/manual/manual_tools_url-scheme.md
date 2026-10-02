# URL Scheme

Surge supports URL scheme actions on iOS and macOS for automating common operations, such as starting Surge or installing a configuration.

On iOS, use the `surge` scheme:

```
surge:///start
```

On macOS, use the `surge` scheme. The `surgeconfig` scheme is also supported for compatibility. {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

```
surge:///install-config?url=x
surgeconfig:///install-config?url=x
```

## Actions

* `surge:///start`

  Start with the selected configuration. iOS only.

* `surge:///stop`

  Stop the current session. iOS only.

* `surge:///toggle`

  Start or stop with the selected configuration. iOS only.

* `surge:///install-config?url=x`

  Install a configuration from a URL. The URL should be encoded in percent encoding.

* `surge:///install-module?url=x`

  Install a [module](../profile/module.md) from a URL. The URL should be encoded in percent encoding.

* `surge:///email-license?email=x&key=y`

  Open the email license activation flow and prefill the email and license key.

  On iOS, this is available only when no active non-trial license is installed.

  On macOS, this is available only while the activation window is open.

* `surge:///enterprise-license?companyID=x&userID=y&passcode=z`

  Open the team license activation flow and prefill the company ID, user ID, and passcode.

  `team-license` is an alias of `enterprise-license`:

  ```
  surge:///team-license?companyID=x&userID=y&passcode=z
  ```

  The following parameter aliases are also accepted:

  * `companyID`, `company-id`, `company_id`, `company`
  * `userID`, `user-id`, `user_id`, `user`
  * `passcode`, `pass-code`, `pass_code`

  On iOS, this is available only when no active non-trial license is installed.

  On macOS, this is available only while the activation window is open.

## Options

* `autoclose=true`

  Automatically close Surge after the action is completed. iOS only. Cannot be used with `install-config`.

  Example:

  ```
  surge:///toggle?autoclose=true
  ```

## x-callback-url

Surge supports the x-callback-url specification from v3.4. The URL scheme is `surge` and the available actions are `start`, `stop`, and `toggle`.
