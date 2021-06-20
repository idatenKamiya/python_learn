#download stock data from a website and store it on the computer

from urllib import request

goog_url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1592681671&period2=1624217671&interval=1d&events=history&includeAdjustedClose=true"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    #put it in a raw stream
    dest_url = r'goog.csv'
    with open(dest_url, "w") as fx:
        for line in lines:
            fx.write(line + "\n")

download_stock_data(goog_url)