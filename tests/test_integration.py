import os, time

import requests


def test_ping_data():
    time.sleep(1)

    resp = requests.get(os.environ["DATA_API_URL"])
    
    assert resp.status_code == 200
    
    j = resp.json()
    assert type(j) is list
    assert len(j) > 0
    assert j[0]['x'] == 0


def test_ping_app():
    time.sleep(1)
    
    resp = requests.get(os.environ["APP_URL"])

    assert resp.status_code == 200

    assert resp.content.decode().startswith("<!DOCTYPE html>")
    
