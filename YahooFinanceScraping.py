import requests
from bs4 import BeautifulSoup
import json

mystocks = ['WISH', 'TSLA', 'DIDI', 'CLOV']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 OPR/77.0.4054.172'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'symbol': symbol,
    'price': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
    'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock 

def output(stock):
    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open('ScrapeToSheets').sheet1
    sh.append_row([str(stock['name'], str(stock['date'], float(stock['price'], float(stock['market cap'])])
    return

for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)
