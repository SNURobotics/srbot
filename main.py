from flask import Flask, request, abort, jsonify
from util import send_message_slack
from menu import snu_menu
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/slack/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        verification_token = 'SduAkwzrdH8Ta9UJbmSIQc2Q'
        token = request.form.get('token', None)
        response_url = request.form.get('response_url', None)
        params = request.form.get('text', None)

        if token == verification_token:
            if isinstance(params, str):
                params = params.strip()
            msg = snu_menu(params)
            return jsonify({'response_type': 'in_channel',
                            'text': msg})
        else:
            return jsonify({'text': 'failure'})
    elif request.method == 'GET':
        verification_token = 'snurobotics'
        token = request.args.get('token')
        test = int(request.args.get('test', 0))
        dt = datetime.now()
        if dt.hour <= 1:
            meal = '점심'
        else:
            meal = '저녁'

        if test:
            to = 'test'
        else:
            to = 'general'

        if token == verification_token:
            msg = snu_menu(meal)
            send_message_slack(msg, to=to)
        return 'worked' 


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
