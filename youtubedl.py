#!/usr/bin/env python

import json
import struct
import sys
import subprocess
import youtube_dl

###
def getMessage():
    rawLength = sys.stdin.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.read(messageLength)
    return json.loads(message)

def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent)
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

def sendMessage(messageContent):
    encodedMessage = encodeMessage(messageContent)
    sys.stdout.write(encodedMessage['length'])
    sys.stdout.write(encodedMessage['content'])
    sys.stdout.flush()
###

url = getMessage()
#url = "https://www.youtube.com/watch?v=F-x6qqNy0mo"
sendMessage(url)

url = url.split("&")[0]

bashScript = "youtube-dl " + url + " -x --audio-format=mp3 --audio-quality=256K -c --socket-timeout 5 -o ~/Music/test/%(title)s.%(ext)s"

process = subprocess.Popen(bashScript.split(), shell=False, stdout=subprocess.PIPE)
output, error = process.communicate()
    
    

