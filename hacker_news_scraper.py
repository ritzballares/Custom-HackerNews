import requests
from bs4 import BeautifulSoup


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


def main():
    res = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    storylink = soup.select('.storylink')  # Contains titles and URLs

    subtext = soup.select('.subtext')  # Contains votes

    custom_hn = get_custom_hackernews(storylink, subtext)
    display_custom_hackernews(custom_hn)


if __name__ == '__main__':
    main()
