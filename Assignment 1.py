import requests
from bs4 import BeautifulSoup
url='https://finance.yahoo.com/quote/%5EHSI/history?period1=1488297600&period2=1503331200&interval=1d&filter=history&frequency=1d'
r=requests.get('https://finance.yahoo.com/quote/%5EHSI/history?period1=1488297600&period2=1503331200&interval=1d&filter=history&frequency=1d')
html_str=r.text
data=BeautifulSoup(html_str,"html.parser")
x=data.find_all('span')
len(x)
list=[]
for i in range(0,len(x)):
    list.append(x[i].text.strip())

list
import csv
with open('assignment 1.csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['Date','Open','High','Low','Close','Adj Close','volume']
    writer.writerow(header)
    for i in range(1,101):
        writer.writerow([list[i*7+24],list[i*7+25],list[i*7+26],list[i*7+27],list[i*7+28],list[i*7+29],list[i*7+30]])