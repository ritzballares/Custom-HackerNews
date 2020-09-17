import requests
from bs4 import BeautifulSoup
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


def get_custom_hackernews(storylink, subtext):
    # Returns a list of hacker news stories containing title, url, and votes
    # Stories will be >= 100 votes
    # Sorted from highest to lowest votes
    custom_hn = []
    for i, story in enumerate(storylink):
        title = story.getText()
        url = story.get('href')
        votes = subtext[i].select('.score')

        # Make sure the story has votes
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))

            # Append stories to list if points > 99
            if points > 99:
                custom_hn.append(
                    {'Title': title, 'Link': url, 'Votes': points})

    # Sorts list in descending order
    return sorted(custom_hn, key=lambda k: k['Votes'], reverse=True)


def display_custom_hackernews(custom_hn):
    # Displays custom hacker news
    for story in custom_hn:
        for k, v in story.items():
            print(k + ':', v)

        print()


def create_sms_msg(custom_hn):
    sms_msg = 'Hi! Here are the top news for today:\n\n'

    for story in custom_hn:
        for k, v in story.items():
            sms_msg += k + ': ' + str(v)
            sms_msg += '\n'

        sms_msg += '\n'

    return sms_msg


def send_sms(custom_hn):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'Enter ACCOUNT SID here'
    auth_token = 'Enter AUTH TOKEN here'
    client = Client(account_sid, auth_token)

    sms_msg = create_sms_msg(custom_hn)
    message = client.messages.create(
        body=sms_msg,
        from_='Enter TWILIO PHONE NUMBER here',
        to='Enter the phone number that you wish to send an SMS to here'
    )

    print('Message sent successfully')
    print(message.sid)


def main():
    res = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    storylink = soup.select('.storylink')  # Contains titles and URLs
    subtext = soup.select('.subtext')  # Contains votes

    # Grab stories with 100 or more votes
    custom_hn = get_custom_hackernews(storylink, subtext)

    # Display custom hackernews list
    display_custom_hackernews(custom_hn)

    # Change top_n_stories to whatever number you like (3 = 3 stories, 4 = 4 stories, and so forth)
    # Keep in mind that there is a 1600 character limit for sending an sms
    # You can modify sms message body in create_sms_msg()
    # Check the README of this repo to learn how to use send_sms()
    top_n_stories = 5
    send_sms(custom_hn[:top_n_stories])


if __name__ == '__main__':
    main()
