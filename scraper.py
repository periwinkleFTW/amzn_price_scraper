"""
This file checks a product page of a product on amazon.ca 
and sends an email if it falls below a certain value
The link must be added to the URL
"""


import requests
from bs4 import BeautifulSoup
import re
import smtplib

# URL to monitor
URL = 'https://www.amazon.ca/Razer-BlackShark-Gaming-Headset-Detachable/dp/B086PKMZ1Q/ref=sr_1_8?crid=2SJH7Q5XLX2DC&dchild=1&keywords=gaming+headset&qid=1602734400&sprefix=gamin%2Caps%2C280&sr=8-8'

# This field specifies the agent which is a broswer
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    # Get the html and data from the page you selected
    soup = BeautifulSoup(page.content, 'html.parser')

    # Use the inspection mode to find out what id or class has the data you need
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    # Convert the string with price to a float
    converted_price = re.findall(r'\d+', price)
    converted_price = float(converted_price[0]) + float(converted_price[1])/100

    if converted_price < 100:
        send_mail()

    print(price)
    print(converted_price)

# We can use gmail. With 2step verification enabled, generate a mail app password for a PC/Mac
def send_mail():
    server = smtp.SMTP('smtp.gmail.com', 587)
    # Identify your app when connecting to an email server
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('username@gmail.com', 'password')

    subject = "Price fell down"
    body = "Check the amazon link: {URL}\n\n\"

    msg = f"Subject: {subject}\n\n\{body}"

    server.sendmail(
        "username@gmail.com",
        "recepient@gmail.com"
        "password",
        msg,
    )
    print("Email has been sent!")

    # Close connection
    server.quit()

while(True):
    check_price()
    time.sleep(60) # In seconds

