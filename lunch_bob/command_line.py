from lunch_bob import slackbot
import datetime
import json
import os

BASE_PATH = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))


def main():
    message = 'Same procedure as yesterday...'
    with open(os.path.join(BASE_PATH, 'lunch_options.json')) as file_:
        lunch_options = json.load(file_)

    today = datetime.datetime.now().strftime('%A').lower()
    reactions = lunch_options['everyday'] + lunch_options[today]

    response = slackbot.send_message(message)
    slackbot.send_reactions(response['ts'], reactions)


if __name__ == '__main__':
    main()
