from dotenv import load_dotenv
from slackclient import SlackClient
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(os.path.join(BASE_PATH, '.env'))

slack_token = os.getenv('LUNCH_BOB_TOKEN')
slack_channel = os.getenv('LUNCH_CHANNEL')


slack_client = SlackClient(slack_token)


def send_message(message):
    response = slack_client.api_call(
        'chat.postMessage',
        channel=slack_channel,
        text=message
    )

    return response


def send_reactions(timestamp, reactions):
    if not iter(reactions):
        reactions = [reactions]
    responses = []
    for reaction in reactions:
        responses.append(slack_client.api_call(
            'reactions.add',
            channel=slack_channel,
            name=reaction,
            timestamp=timestamp
        ))
    return responses

