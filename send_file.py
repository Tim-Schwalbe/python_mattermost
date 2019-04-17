import os
import json
import requests
import argparse

parser = argparse.ArgumentParser(
    description='Mattermost File send CLI for API V4')
parser.add_argument(dest='server_url', metavar='SERVER_URL',
                    type=str, help='The Mattermost Server Url')
parser.add_argument(dest='access_token', metavar='ACCESS_TOKEN',
                    type=str, help='Personal Access Token to Authorize')
parser.add_argument(dest='channel_id', metavar='Channel_ID',
                    type=str, help='The Channel ID you want to send the file to.')
parser.add_argument(dest='file_path', metavar='FILE_PATH',
                    type=str, help='The Path to the file you want to send.')
parser.add_argument('-m', '--message', dest='message', default='',
                    help='Message that is attached to the uploaded file.')
parser.add_argument('-am', '--attachment_message', dest='attachment_message', default='',
                    help='Message that is attached to the uploaded file.')
parser.add_argument('-c', '--color', dest='color',metavar='HEXCODE', default='#00FF00',
                    help='Attachment Box Color as HEX Code. Default: #00FF00')
args = parser.parse_args()

server_url = args.server_url
access_token = args.access_token
channel_id = args.channel_id
file_path = args.file_path
message = args.message
attachment_message = args.attachment_message
color = args.color

if attachment_message == "":
    props = {}
else:
    props = {"attachments": [{"text":attachment_message,"color":color}]}

print(props)
s = requests.Session()
s.headers.update({"Authorization": "Bearer " + access_token})

form_data = {
    "channel_id": ('', channel_id),
    "client_ids": ('', "id_for_the_file"),
    "files": (os.path.basename(file_path), open(file_path, 'rb')),
}
r = s.post(server_url + '/api/v4/files', files=form_data)

FILE_ID = r.json()["file_infos"][0]["id"]

p = s.post(server_url + '/api/v4/posts', data=json.dumps({
    "channel_id": channel_id,
    "message": message,
    "file_ids": [FILE_ID],
    "props": props
}))
