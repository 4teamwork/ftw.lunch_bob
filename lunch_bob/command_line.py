from lunch_bob import slackbot


def main():
    message = 'Same procedure as yesterday...'
    reactions = ['inder']
    response = slackbot.send_message(message)
    print(response)
    rsp = slackbot.send_reactions(response['ts'], reactions)
    print(rsp)


if __name__ == '__main__':
    main()
