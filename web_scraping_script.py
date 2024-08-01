import requests
from bs4 import  BeautifulSoup
import re
import pandas as pd

names = []
prices = []
descriptions = []

for i in range(1,11):
    print("Page - ",i)
    
    url = "https://www.flipkart.com/search?q=mobile+under+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    name = soup.find_all("div", class_ = "KzDlHZ")
    for i in name:
        names.append(i.get_text())
    tn = len(names)
    print(tn)


    price = soup.find_all("div", class_ = "Nx9bqj _4b5DiR")
    for i in price:
        prices.append(i.get_text())
    tp = len(prices)
    print(tp)


    description = soup.find_all("ul", class_ = "G4BRas")
    for i in description:
        descriptions.append(i.get_text())
    td = len(descriptions)
    print(td)


df = pd.DataFrame({"Name":names, "Price":prices ,"Specification":descriptions})
print(df)

df.to_csv("Downloads/Mobile_Data.csv")