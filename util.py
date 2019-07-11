"""
util.py
=======
Utility functions
"""
import requests
import json

SLACK_WEBHOOD_URLS \
        = {'experiments': 'https://hooks.slack.com/services/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',
           'general': 'https://hooks.slack.com/services/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',
           'test': 'https://hooks.slack.com/services/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',
          }


def send_message_slack(msg, to='experiments'):
    """msg: str. message to send
    to: target channel."""
    url = SLACK_WEBHOOD_URLS[to]
    data = json.dumps({'text': msg}, default=str)

    try:
        response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
    except requests.exceptions.ConnectionError:
        print('Slack Hook API is not working now')

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
