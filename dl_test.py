#!/usr/local/bin/python3
# coding: utf-8

# ytdl-bot - dl_test.py
# 5/4/21 12:56
#

import youtube_dl

ydl_opts = {
# %(title)s.%(ext)s
    'outtmpl': '/Users/psycho/Downloads/abc/%(title)s.%(ext)s',

}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])