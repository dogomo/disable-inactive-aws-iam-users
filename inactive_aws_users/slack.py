import json
import requests


def message(color, pretext, title, message, webhook):
    payload = {
        "attachments": [
            {
                "color": color,
                "pretext": pretext,
                "title": title,
                "text": message
            }
        ]
    }
    requests.post(webhook,
                  json.dumps(payload),
                  headers={'content-type': 'application/json'})
