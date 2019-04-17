# Python Mattermost Python CLI for API V4

This is a simple CLI to upload files to mattermost

Supported API Version: *V4*

Just do `python send_file.py -h`

~~~~{.python}
 Mattermost File send CLI for API V4

positional arguments:
  SERVER_URL            The Mattermost Server Url
  ACCESS_TOKEN          Personal Access Token to Authorize
  Channel_ID            The Channel ID you want to send the file to.
  FILE_PATH             The Path to the file you want to send.

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        Message that is attached to the uploaded file.
  -am ATTACHMENT_MESSAGE, --attachment_message ATTACHMENT_MESSAGE
                        Message that is attached to the uploaded file.
  -c HEXCODE, --color HEXCODE
                        Attachment Box Color as HEX Code. Default: #00FF00
~~~~


To use it you need a personal access token.
https://docs.mattermost.com/developer/personal-access-tokens.html
The Channel ID can be found in the channel settings -> 'View Info'

You can choose with the optional arguments to send a normal message or a message with a specific color as attachment box.
