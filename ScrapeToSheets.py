import gspread

gc = gspread.service_account(filename='credentials.json')

sh = gc.open('YahooScrapeToSheets').sheet1

