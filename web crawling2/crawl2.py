import requests
url = "https://rate.bot.com.tw/xrt?Lang=en-US"
html = requests.get(url)
from bs4 import BeautifulSoup

sp = BeautifulSoup(html.text, 'html.parser')

import pandas as pd
tables = pd.read_html("https://rate.bot.com.tw/xrt?Lang=en-US")
table = tables[0]
table = table.iloc[:, :5]
table.columns = ["Currency", "Cash Buying", "Cash Selling", "Spot Buying", "Spot Selling"]
table.set_index('Currency')

currency = input().upper()

amount_ntd = int(input())

rate = table[table['Currency'].str.contains(f'{currency}')].iloc[0]['Cash Buying']
if rate == '-':
    rate = table[table['Currency'].str.contains(f'{currency}')].iloc[0]['Spot Buying']

target_amount = round(amount_ntd / float(rate), 3)
print(f'{target_amount} {currency}')