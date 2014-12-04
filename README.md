# degoogler

Lints a JSON object copied from multiple cells of a Google Spreadsheet. Currently it removes initial `"`s, then replaces `` ` ``s with `"`s, and lastly replaces `NaN`s with `0`s (because NaN is not a valid JSON value).

For example, it turns:

```
"{"
  `name`: `Joe Pietruch`,
  `age`: NaN,
  `quote`: `\`No worries!\``
"}"
```

into

```
 { 
  "name": "Joe Pietruch",
  "age": 0,
  "quote": "\"No worries!\""
 } 
```

## Installation

1. [**Install Package Control**](https://sublime.wbond.net/installation): a means for easily adding plugins to SublimeText.
2. **Add Repository**: In Sublime, press Cmd+Shift+P and start typing in the entry field so that *Package Control: Add Repository* comes up. Hit enter, and then paste `https://github.com/Percipient24/degoogler` in the field that opens at the bottom of the window.
3. **Install degoogler**: In Sublime, press Cmd+Shift+P again, and start typing so that *Package Control: Install Package* comes up. Hit enter, and then start typing `degoogler`. When it appears on the list, select it, and look to the bottom of the window for a status message that lets you know it worked!

## Usage

Once installed, have the file you would like to convert open and focused, then simply press `Cmd+Alt+G`.

### Changelog

**v0.0.1** A first attempt.
- initial commit of the package files to get things up and running
