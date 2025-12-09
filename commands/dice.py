import random
from flask import jsonify

def dice(data):
    text = data.get('text', '')
    split = text.split()

    if len(split) != 2:
        res = {
            "response_type": "ephemeral",
            "text": "need two argument a (min) b (max)"
        }

    res = {
        "response_type": "ephemeral",
        "text": f"{random.randint(int(split[0]), int(split[1]))}"
    }

    return jsonify(res)