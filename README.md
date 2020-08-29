# Custom-HackerNews
This is a web scraping project that scrapes data from the front page of Hacker News. In this project, stories that have 100 or more points will get displayed in the terminal. As an additional feature of the script, you can also send the list as an SMS using Twilio's API (see #3).

1. Clone this repo
2. Install dependencies
```
pip3 install requests
pip3 install beautifulsoup4
pip3 install twilio
```
3. If you'd like to send the list as an SMS using Twilio's API: 
    - You'll have to sign up in Twilio first: https://www.twilio.com/try-twilio
    - Change the value for *accound_sid* (line 54), *auth_token* (line 55), and the *twilio trial phone number* (line 61) in `send_sms()`
        - All of the information can be found in twilio.com/console once you've signed up
    - Uncomment line 82 which calls `send_sms()`
        - You can change the parameter if you'd like to send more/less news
        - The script currently sends the top three news from the list
        - `send_sms(custom_hn[:2])` will send the top 2 news, `send_sms(custom_hn[:4])` will send the top 4, and so forth
        - As far as I know, 1600 characters is the limit when sending an SMS
    - There is a Python Quickstart for using Twilio SMS: https://www.twilio.com/docs/sms/quickstart/python
4. Run the script `python3 hacker_news_scraper.py`