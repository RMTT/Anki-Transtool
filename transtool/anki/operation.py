import json
import requests
from . import REQ_URL


def add_card(deck_name: str, model_name: str, version: int, front: str, back: str):
    data = {
        "action": "guiAddCards",
        "version": version,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": model_name,
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "options": {
                    "closeAfterAdding": True
                }
            }
        }
    }
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    rep = requests.post(url=REQ_URL, json=data, headers=headers)


def add_media(b64: str, filename: str, version: int):
    data = {
        "action": "storeMediaFile",
        "version": version,
        "params": {
            "filename": filename,
            "data": b64
        }
    }
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    rep = requests.post(url=REQ_URL, json=data, headers=headers)
