# flask-mail-demo

A simple example demonstrating Flask-mail functionality. Takes user input from a form and sends email to specified address. Supports attachments.

Note that `os.path.join` (line 34 in `app.py`) is for Windows. Syntax varies by OS.

Setup note:
This example uses gmail. You must turn on the setting to "allow less secure apps" (https://myaccount.google.com/lesssecureapps). You must also disable 2FA, so I recommend making new emails for development/testing.
