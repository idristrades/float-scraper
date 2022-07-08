from requests import get
from bs4 import BeautifulSoup

stock = input('Enter ticker symbol:')

try:

    ss_url = 'https://shortsqueeze.com/?symbol=' + stock
    response = get(ss_url)
    page_html = BeautifulSoup(response.text,'html.parser')

    # Find float
    table1 = page_html.find_all('table', attrs = {'width':'760'})
    td = table1.find_all('td', attrs = {'align':'right'})
    table2 = td.find_all('table')[2]
    tr1 = table2.find_all('tr')[3]
    tr2 = tr1.find_all('tr')[6]
    ss_float = tr2.find('td', class_ ='style12').text
    
    print('Float: ' + ss_float)

except:
    print('error, check code & try again')
