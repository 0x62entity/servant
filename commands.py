import time
from flask import jsonify

class Commands:
    def test(data):
        user_id = data.get('user_id')
        channel_id = data.get('channel_id')

        response = {
            "response_type": "ephemeral",
            "text": f"User ID: {user_id}\nChannel ID: {channel_id}"
        }

        return jsonify(response)
    
    def reminder(data, app):
        user_id = data.get('user_id')

        if user_id != "U092839T3A7":
            res = {
                "response_type": "ephemeral",
                "text": "pls stop trying to gaslight me into thinking i have shit to do\n\nyou dont have perms to use this cmd"
            }

            return jsonify(res)

        channel_id = data.get('channel_id')
        text = data.get('text', '')
        split = text.split()

        if len(split) < 2:
            res = {
                "response_type": "ephemeral",
                "text": "noooo u need at least two argument"
            }
            return jsonify(res)
        
        minutes = split[-1]
        reminder = text.removesuffix(minutes).strip()
        
        try:
            minutes = int(minutes)
            post_at = int(time.time()) + (minutes * 60)
            
            app.client.chat_scheduleMessage(
                channel=channel_id,
                post_at=post_at,
                text=f"<@U092839T3A7> reminder: u got shit to do: {reminder}"
            )
        except ValueError:
            res = {
                "response_type": "ephemeral",
                "text": "time needs to be a number in mins"
            }
            return jsonify(res)
        
        except Exception as e:
            res = {
                "response_type": "ephemeral",
                "text": f"error: {str(e)}"
            }
            return jsonify(res)
            
        res = {
            "response_type": "ephemeral",
            "text": f"ok, will remind '{reminder}' in {minutes} minutes"
        }
        return jsonify(res)