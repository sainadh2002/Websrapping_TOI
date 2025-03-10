# -*- coding: utf-8 -*-

#Importing Libraries
import numpy as np
import pandas as pd
import bs4
import requests

#Fetching the Web Page
url = "https://timesofindia.indiatimes.com/"
response = requests.get(url)
print(response.status_code)

#Parsing the HTML
from bs4 import BeautifulSoup
data = BeautifulSoup(response.text ,"lxml")
data

#Extracting Data (label_names,label_link, img_urls)
label_names=[]
label_link=[]
img_urls=[]



for i in data.find_all('a'):
  labels=i.get_text()
  links=i.get('href')
  desc=i.find('p')
  img_link=i.find('img')
  img_src=img_link.get('src') if img_link else None




  label_names.append(labels)
  label_link.append(links)
  img_urls.append(img_src)

#Extracting Descriptions
descriptions=[]
desc_1 = data.find_all("p")
desc_2 = data.find_all("figcaption")
desc_3 = data.find_all("span")

desc_1

desc_2

desc_3

for tag in desc_1 + desc_2 + desc_3:
    descriptions.append(tag.text)
descriptions

label_names

label_link

img_urls

#Printing and Checking Lengths

print(len(label_names))
print(len(label_link))
print(len(img_urls))
print(len(descriptions))

#Ensuring Consistent Lengths

min_length = min(len(label_names), len(label_link), len(img_urls), len(descriptions))

label_names = label_names[:min_length]
label_link = label_link[:min_length]
img_urls = img_urls[:min_length]
descriptions = descriptions[:min_length]

#Creating a Pandas DataFrame

df = pd.DataFrame({
    "Label Names": label_names,
    "Label Links": label_link,
    "Image URLs": img_urls,
    "Description": description  # Combined description
})

df

df.to_csv('TOI_info.csv',index=False)
df

#NULL VALUES

df.isnull().sum()

