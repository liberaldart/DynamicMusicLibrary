# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    import pafy
    song = pafy.new("https://www.youtube.com/watch?v=uENITui5_jU")
    audio = song.getbestaudio()
    audio.download()
    return dict()

def error():
    return dict()
