[[!meta title="dropbox"]]

* Authors: Patrick ZAJDA, Filaos and other contributors

This plugin will add a shortcut to announce Dropbox status, version or open the Dropbox systray menu.
Also page tabs working on the preferences dialog with Ctrl+tab / Ctrl+Shift+Tab and Ctrl+PageUp/Down.
To conclude, make the cancel button working with escape.

* Shortcut: NVDA+Shift+D
* Ctrl+Alt+T announce the active tab.

## Known issues ##

* If you switch between tabs using the shortcuts, when you'll close the preferences window, NVDA won't be able to know the windows doesn't exist anymore.
It is a known issue on NVDA and cannot be fixed.

## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor

## Changes for 4.0 ##

* Change Shift+NVDA+D behavior: if pressed once announce Dropbox status, twice open the context menu.
* Translations update.
* Fixed issues with windows 8 metro app.
* Addon help is no longer available in the help menu, it's found in the addons manager instead.
* As Dropbox changes his gui from version to version, all features for settings dialog were removed.
* Modified the shortcut to get dropbox status to Alt+NVDA+D to avoid conflict with audio ducking support.

## Changes for 3.1 ##

* Use another way to get cancel button and page tab. Now we don't have to focus them before using shortcuts.
* When changing the active tab, the focus move to the tab page so when pressing tab, the first item of the tab is activated instead of staying to the previous used tab even if it is not activated anymore.
* In the preferences dialog, it is now possible to press control+page up/down to switch between tabs. Control+tab and control+shift+tab still work.
* All localized manifest files should now be OK.
* Minor corrections.

## Changes for 3.0 ##

* Minor correction in the main manifest file (authors are correctly displayed).
* Improved context menu detection when pressing Shift+NVDA+D three times.
* The escape button now works (only when using Dropbox in the same language NVDA uses).
* A lot of corrections in the code.
* Added/updated documentations of all scripts.
* New languages: Arabic, Brazilian Portuguese, Czech, Dutch, Finnish, Galician, German, Hungarian, Japanese, Nepali, Polish, Russian, Spanish, Slovak, Tamil, Turkish.

## Changes for 2.0 ##

* New languages: Italian
* Pressing the shortcut three times or more when already being in the context menu doesn't cause problem anymore.

## Changes for 1.0 ##

* Initial Release

