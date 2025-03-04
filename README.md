# Websrapping_TOI
Times Of India news paper web scrapping


**Web Scraping the Times of India newspaper with Beautiful Soup**


**Submitted By: UPPUTHOLLA VENKATA SAINADH**

**Mail:** [**sainadhupputholla2002@gmail.com**](mailto:sainadhupputholla2002@gmail.com)

**Role: DATA ANALYST  
<br/><br/>**

**WEB SCRAPPING**

Web scraping is a computer technique used to extract information from websites. It involves automatically fetching web pages, extracting data from them, and saving that data for various purposes. Here's a more detailed explanation:  

- Request: You start by sending a request to a website's server. This request is like entering a web address in your browser.  
- Response: The website's server responds by returning the requested web page. This page typically contains text, images, links, and other data.  
- Parsing: Web scraping tools or scripts analyze the web page's content. They can be programmed to locate and extract specific data from the web page, such as product prices, news articles, or contact information.  
- Storage or Usage: The extracted data can then be saved in a file or database for further analysis, or it can be used for various purposes, such as price comparison, research, or building a dataset.  

Web scraping helps automate gathering data from websites, which is tedious, time-consuming and error prone when done manually.  

**WEB SCRAPPING TOOL:**

A variety of tools are available to perform web scraping. Beautiful Soup (bs4) is a simple way to accomplish web scraping in our Python.

**Beautiful soup:**

BeautifulSoup4 is a user-friendly Python library designed for parsing HTML and XML documents. It simplifies the process of web scraping by allowing developers to effortlessly navigate, search and modify the parse tree of a webpage. With BeautifulSoup4, we can extract specific elements, attributes and text from complex web pages using intuitive methods. This library abstracts away the complexities of HTML and XML structures, enabling us to focus on retrieving and processing the data we need. BeautifulSoup4 supports multiple parsers (like Python’s built-in html.parser, lxml, and html5lib), giving us the flexibility to choose the best tool for our task. Whether we’re gathering data for research, automating data extraction or building web applications.

**SOURCE CODE:**

import numpy as np

import pandas as pd

import bs4

import requests

url = "<https://timesofindia.indiatimes.com/>"

response = requests.get(url)

print(response.status_code)

from bs4 import BeautifulSoup

data = BeautifulSoup(response.text ,"lxml")

data

label_names=\[\]

label_link=\[\]

img_urls=\[\]

for i in data.find_all('a'):

&nbsp; labels=i.get_text()

&nbsp; links=i.get('href')

&nbsp; desc=i.find('p')

&nbsp; img_link=i.find('img')

&nbsp; img_src=img_link.get('src') if img_link else None

&nbsp; label_names.append(labels)

&nbsp; label_link.append(links)

&nbsp; img_urls.append(img_src)

descriptions=\[\]

desc_1 = data.find_all("p")

desc_2 = data.find_all("figcaption")

desc_3 = data.find_all("span")

desc_1

desc_2

desc_3

for tag in desc_1 + desc_2 + desc_3:

&nbsp;   descriptions.append(tag.text)

descriptions

label_names

label_link

img_urls

print(len(label_names))

print(len(label_link))

print(len(img_urls))

print(len(descriptions))

min_length = min(len(label_names), len(label_link), len(img_urls), len(descriptions))

label_names = label_names\[:min_length\]

label_link = label_link\[:min_length\]

img_urls = img_urls\[:min_length\]

descriptions = descriptions\[:min_length\]

df = pd.DataFrame({

&nbsp;   "Label Names": label_names,

&nbsp;   "Label Links": label_link,

&nbsp;   "Image URLs": img_urls,

&nbsp;   "Description": description  # Combined description

})

df

df.to_csv('TOI_info.csv',index=False)

df

This Python script is designed to scrape data from the Times of India (TOI) website, extract specific information, and save it into a CSV file.

step-by-step explanation of the code along with the expected output at each stage.

**Step 1: Import Libraries**

import numpy as np

import pandas as pd

import bs4

import requests

**Explanation**:

The script imports necessary libraries:

- numpy and pandas for data manipulation.
- bs4 (BeautifulSoup) for parsing HTML content.
- requests for making HTTP requests to fetch the webpage.

**Step 2: Fetch the Webpage**

url = "<https://timesofindia.indiatimes.com/>"

response = requests.get(url)

print(response.status_code)

**Explanation**:

- The script sends an HTTP GET request to the TOI homepage.
- response.status_code checks if the request was successful (e.g., \`200\` for success).

**Output**:

The status code (e.g., \`200\`) is printed to the console.

**Step 3: Parse the HTML Content**

from bs4 import BeautifulSoup

data = BeautifulSoup(response.text, "lxml")

data

**Explanation**:

- The HTML content of the webpage is parsed using BeautifulSoup with the \`lxml\` parser.
- data\` now contains the parsed HTML structure of the webpage.

**Output**: The parsed HTML content is stored in the \`data\` variable.



**Step 4: Initialize Lists for Data Storage**

label_names = \[\]

label_link = \[\]

img_urls = \[\]

**Explanation**:

Three empty lists are initialized to store:

- label_names: Text of the links (e.g., article titles).
- label_link: URLs of the links.
- img_urls: URLs of the images.

**Step 5: Extract Data from Anchor Tags (\`&lt;a&gt;\`)**

for i in data.find_all('a'):

labels = i.get_text()

links = i.get('href')

desc = i.find('p')

img_link = i.find('img')

img_src = img_link.get('src') if img_link else None

label_names.append(labels)

label_link.append(links)

img_urls.append(img_src)

**Explanation:**

The script iterates through all \`&lt;a&gt;\` tags in the HTML.

For each \`&lt;a&gt;\` tag:

- labels: Extracts the text (e.g., article title).



- links: Extracts the \`href\` attribute (URL).



- img_src: Extracts the \`src\` attribute of the \`&lt;img&gt;\` tag (if present).



- The extracted data is appended to the respective lists.

**Output**:

The lists \`label_names\`, \`label_link\`, and \`img_urls\` are populated with data.

**Step 6: Extract Descriptions**

descriptions = \[\]

desc_1 = data.find_all("p")

desc_2 = data.find_all("figcaption")

desc_3 = data.find_all("span")

for tag in desc_1 + desc_2 + desc_3:

descriptions.append(tag.text)

**Explanation:**

- The script extracts text from \`&lt;p&gt;\`, \`&lt;figcaption&gt;\`, and \`&lt;span&gt;\` tags.
- These tags often contain descriptions or captions.
- The extracted text is appended to the \`descriptions\` list






**Output**: The \`descriptions\` list is populated with text from the specified tags.

**Step 7: Check Lengths of Extracted Data**

print(len(label_names))

print(len(label_link))

print(len(img_urls))

print(len(descriptions))

**Explanation:**

- The script prints the lengths of the extracted data lists to ensure they are populated.

**Output**:

The lengths of \`label_names\`, \`label_link\`, \`img_urls\`, and \`descriptions\` are printed to the console.

**Step 8: Align Data Lengths**

min_length = min(len(label_names), len(label_link), len(img_urls), len(descriptions))

label_names = label_names\[:min_length\]

label_link = label_link\[:min_length\]

img_urls = img_urls\[:min_length\]

descriptions = descriptions\[:min_length\]

**Explanation**:

- The script ensures all lists have the same length by truncating them to the length of the shortest list.
- This ensures the data can be combined into a DataFrame without mismatches.

**Output**:

The lists are truncated to the same length.

**Step 9: Create a DataFrame**

df = pd.DataFrame({

"Label Names": label_names,

"Label Links": label_link,

"Image URLs": img_urls,

"Description": descriptions

})

df



**Explanation**:

- A panda DataFrame is created using the extracted data.
- The DataFrame has four columns: \`Label Names\`, \`Label Links\`, \`Image URLs\`, and \`Description\`.

**Output**: The DataFrame is displayed in the console.

**Step 10: Save DataFrame to CSV**

df.to_csv('TOI_info.csv', index=False)

df

**Explanation**:

- The DataFrame is saved to a CSV file named \`TOI_info.csv\`.
- \`index=False\` ensures the DataFrame index is not included in the CSV file.

**Output**:

The CSV file is saved to the working directory, and the DataFrame is displayed again.

**Final Output**

The script outputs:

1\. A CSV file (\`TOI_info.csv\`) containing the extracted data.

2\. A DataFrame displayed in the console with the following columns:

- \`Label Names\`: Titles or text from links.
- \`Label Links\`: URLs of the links.
- \`Image URLs\`: URLs of the images.
- \`Description\`: Combined descriptions from \`&lt;p&gt;\`, \`&lt;figcaption&gt;\`, and \`&lt;span&gt;\` tags.

