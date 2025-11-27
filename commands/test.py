from flask import jsonify

def test(data):
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')

    response = {
        "response_type": "ephemeral",
        "text": f"User ID: {user_id}\nChannel ID: {channel_id}"
    }

    return jsonify(response)