import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "http://www.nepalstock.com/todaysprice"

#Create Object pageclear
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")
table1 = soup.find('table', {"class":'table table-condensed table-hover'})

headers = []

for i in table1.find_all('tr', class_="unique"):
    title = i.text
    headers.append(title)

#Create a dataframe
mydata = pd.DataFrame(columns=headers)
print(mydata)

# for j in table1.find_all('tr')[1:]:
#     row_data = j.find_all('td')
#     row = [i.text for i in row_data]
#     length = len(mydata)
#     mydata.loc[length] = row

# title = table1.find_all("tr", {"class":"unique"})
