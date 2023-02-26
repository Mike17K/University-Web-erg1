import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = 'https://www.skroutz.gr/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    
    print("The software of the server is : ",response.headers.get('Server'))
    if 'Set-Cookie' in response.headers:
        print("This website uses cookies.")

        cookies = response.cookies
        print("All cookies:")
        for cookie in cookies:
            print(cookie.name, datetime.datetime.fromtimestamp(cookie.expires))
    else:
        print("This website does not use cookies.")

