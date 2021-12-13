from fastapi import FastAPI
from lyrics import *

app = FastAPI(title='Ardx Lyrics API', version='1.0.0')


@app.get("/")
def read_root():
    data = {
        'message': "Welcome to Ardx Lyrics API"
    }
    return data

@app.get("/lyrics/")
def read_items(q: str):
    data = searchLyrics(q)
    return {'result': data, 'message': 'lyrics provided by Musixmatch. made with <3'}
