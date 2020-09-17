# Custom-HackerNews
This is a web scraping project that scrapes data from the front page of Hacker News. Using Twilio's API, this sends the top *n* stories as an SMS (5 is the default value for *n*). It will also display the stories that have 100 or more votes in the terminal.

1. Clone this repo
2. Install dependencies
```
pip3 install requests
pip3 install beautifulsoup4
pip3 install twilio
```
3. To send an SMS using Twilio's API: 
    - You'll have to sign up in Twilio first: https://www.twilio.com/try-twilio
    - Change the value for *accound_sid*, *auth_token*, and the *twilio trial phone number* (change the value for the key **from_**) in `send_sms()`
        - All of the information can be found in twilio.com/console once you've signed up
        - Don't forget to change the value for the key **to** (Enter the phone number that you wish to send an SMS to here)
    - Change the value of *top_n_stories* (found in `main()`) to any number that you like depending on if you want more/less news
        - The script currently sends the top five news from the list
        - `top_n_stories = 2` will send the top 2 news, `top_n_stories = 4` will send the top 4, and so forth; the value for *top_n_stories* will be passed to `send_sms()` as an argument
        - As far as I know, 1600 characters is the limit when sending an SMS
    - There is a Python Quickstart for using Twilio SMS: https://www.twilio.com/docs/sms/quickstart/python
4. Run the script `python3 hacker_news_scraper.py`