# automatedPythoniMessage
This project merges my love for my friends and how I love to show that love: trolling them. This project allows you to input song lyrics and send them word for word via iMessage to a phone number.

automessage.py file utilizes this third-party module: https://pypi.org/project/py-iMessage/.
It worked for sending individual messages but had little functionality regarding multiple messages and looping.

automatemessagev2.py file is my second version where I switched to utilizing AppleScript to take in the phone number and message as parameters (credits to this article for the AppleScript help: https://medium.com/better-programming/so-i-wrote-a-py-web-scraper-that-sends-me-scpt-text-messages-about-job-postings-34ffef9a1128). It then uses my python file to take lyrics from any song (I used Kanye West's lovely Chick-Fil-A) and sends it individually word-for-word through a loop. There's still room for improvement though!
