###########################################################################################
#
# WebCrawler_DataFilter.py
#
# This is sample code for Web crawling with Python
# data filter for data analysos
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
        "https://www.error", # wrong page for error handling test purpose
        "https://www.google.com/finance/quote/AAPL:NASDAQ",
        "https://www.google.com/finance/quote/AMZN:NASDAQ",
        "https://www.google.com/finance/quote/TMUS:NASDAQ",
        "https://www.google.com/finance/quote/TSLA:NASDAQ",
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
    data.append([name, float(price.split('$')[1].replace(',',''))]) #fix convert string to float due to comma

#Save to Excel
df = pd.DataFrame(data, columns = ['Company Name','Stock Price'])
print("=== Total data (Excel) ====")
print(df)
df.to_excel("output.xlsx", sheet_name='sheet1')

#Data filter for data analysis
def filter_keyword(data, keyword):
    fData = data[data['Company Name'].str.contains(keyword)] #filter condition, matching with keyword
    print("Find ",keyword,":",fData)
    #print(keyword,":",fData.count()) #example, show count number

def filter_range(data, range):
    fData = data[data['Stock Price']>range] #filter condition, value in range
    print("Find >",range,":",fData)

print("=== Filtered data ====")
filter_keyword(df, "Verizon")
filter_range(df, 100)

#Data sort
sData = df.sort_values(['Stock Price'], ascending=[0])
print("=== Sorted data (Ascending) ====")
print(sData)
#print(sData.head(10)) #example, show top 10
#print(sData.tail(10)) #example, show tail 10
