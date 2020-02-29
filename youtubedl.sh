#!/bin/bash

echo "$1"

youtube-dl $1 -x --audio-format=mp3 --audio-quality=256K -o ~/Music/test/'%(title)s.%(ext)s'
