###########################################################################################
#
# WebCrawler_ScrapingContents.py
#
# This is sample code for web scraping with Python
# extracting contents from web page
# (ex, https://basicenglishspeaking.com/daily-english-conversation-topic)
# easily click on links for all contents
# (ex, http://basicenglishspeaking.com/wp-content/uploads/audio/QA/Q-01-01.mp3)
#
# Created by Jonggil Nam
# LinkedIn: https://www.linkedin.com/in/jonggil-nam-6099a162/
# Github: https://github.com/woodstone10
# e-mail: woodstone10@gmail.com
# phone: +82-10-8709-6299
###########################################################################################

import requests
from bs4 import BeautifulSoup

def crawl(url):
    try:
        rData = requests.get(url)  # web crawling
        print(rData)  # expect Response [200]
        return rData
    except:
        print("<Response Error>")
        return 0

def parse(str):
    bsData = BeautifulSoup(str, "html.parser")  # parsing from web crawling data
    links = []
    for link in bsData.findAll('a'):
        #print(link.get('href'))
        links.append(link.get('href')) #get url link
    return links

str = crawl('https://basicenglishspeaking.com/daily-english-conversation-topic')
url = parse(str.text)

def contents(str):
    try:
        bsData = BeautifulSoup(str.text, "html.parser")
        contents = bsData.findAll("div", {"class": "sc_player_container1"})
        for i in range(len(contents)):
            print(contents[i])
    except:
        print("No contents")

for i in range(len(url)):
    print(url[i])
    str = crawl(url[i])
    contents(str)
