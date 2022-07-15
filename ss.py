# Import Packages and Modules
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from time import time

# Prompt for ticker symbol (e.g. AAPL)
stock = input('Enter ticker symbol:')

# Set start time to measure the speed of the whole operation
start = time()

# Get float from shortsqueeze.com
try:
    # Get html
    sscom_url = 'http://shortsqueeze.com/?symbol=' + stock
    response = get(sscom_url)
    page_html = BeautifulSoup(response.text,'html.parser')

    # Find float
    table = page_html.find_all('table', attrs = {'width':'100%'})[7]
    sscom_stock_float = table.find_all('td', attrs = {'align':'right'})[6].text.replace(" ","")
    stock_float = float(sscom_stock_float.replace(',', ''))
    stock_float = round(float(stock_float) / 1000000, 1)

    # Results
    print('Float: ' + str(stock_float) + 'M')


# If not available, print error message
except:
    print('No data available')
    
# Calculate the time taken for the entire scraping operation
end = time()
print('Time taken: ' + str(round(end - start, 2)) + 's')
