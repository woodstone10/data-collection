###########################################################################################
#
# WebCrawler_SaveToExcel.py
#
# This is sample code for Web crawling with Python
# save data to excel (using pandas)
#
# Created by Jonggil Nam
# LinkedIn: https://www.linkedin.com/in/jonggil-nam-6099a162/
# Github: https://github.com/woodstone10
# e-mail: woodstone10@gmail.com
# phone: +82-10-8709-6299
###########################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl(url):
    try:
        rData = requests.get(url)  # web crawling
        print(rData)  # expect Response [200]
        return rData.content
    except:
        print("<Response Error>")
        return 0

def parse(str):
    bsData = BeautifulSoup(str, "html.parser")  # parsing from web crawling data
    # tag and class information: Chrome > Google Finance > Options > More tools > Developer tools
    # get company name and current stock price
    name = bsData.find("h1", {"class": "KY7mAb"})  # < h1 class ="KY7mAb" > Company name < / h1 >
    price = bsData.find("div", {"class": "YMlKec fxKbKc"})  # <div class="YMlKec fxKbKc">Price $xx.xx</div>
    return {"name": name.text, "price": price.text}

url = ["https://www.google.com/finance/quote/VZ:NYSE",  # Verizon
    "https://www.google.com/finance/quote/QCOM:NASDAQ",  # Qualcomm
    "https://www.error",  # wrong page for error handling test purpose
    ]

data = []
for i in range(len(url)):
    str = crawl(url[i])
    if str == 0:
        continue
    txt = parse(str)
    name = txt.get("name")
    price = txt.get("price")
    print(name, ":", price)
    data.append([name, float(price.split('$')[1])])

df = pd.DataFrame(data, columns = ['Company Name','Stock Price'])
print(df)
df.to_excel("output.xlsx", sheet_name='sheet1')
