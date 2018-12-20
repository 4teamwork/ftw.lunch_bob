from dotenv import load_dotenv
from slackclient import SlackClient
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(os.path.join(BASE_PATH, '.env'))

slack_token = os.getenv('POST_BOY_SLACK_TOKEN')
slack_channel = os.getenv('POST_BOY_CHANNEL')


def send_message(pretext, text, color=None, img_url=None):
    slack_client = SlackClient(slack_token)
    if(slack_client.rtm_connect(with_team_state=False)):
        print("Starter Bot connected and running!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        slack_client.api_call(
            "chat.postMessage",
            channel=slack_channel,
            as_user=True,
            user=starterbot_id,
            attachments=[
                {
                    "pretext": pretext,
                    "text": text,
                    "color": color,
                    "image_url": img_url,
                }
            ],
        )
    else:
        print("Connection failed.")
