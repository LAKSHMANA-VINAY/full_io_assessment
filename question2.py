# 2)  WAP to get the Social Links, Email & Contacts details of a website on user input

import requests
from bs4 import BeautifulSoup
import re

def content_in_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    epattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(epattern, soup.get_text())
    ppattern = r'\b(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})\b'
    phone_numbers = re.findall(ppattern, soup.get_text())
    print("emails :",emails)
    print("phone numbers :",phone_numbers)
    social_media_links = []
    social_media_platforms = ["facebook.com", "instagram.com", "linkedin.com","twitter.com","youtube.com"]
    for i in soup.find_all('a', href=True):
        for j in social_media_platforms:
            if j in i['href']:
                social_media_links.append(i['href'])
                break
    print("social media links :",social_media_links)

website_url = "https://srkrec.edu.in/"
content_in_site(website_url)

website_url = "https://ful.io"
content_in_site(website_url)

website_url = "https://www.tcs.com/"
content_in_site(website_url)