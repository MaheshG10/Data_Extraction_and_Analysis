#importing excel file
import pandas as pd
df=pd.read_excel('Input.xlsx')
print(df)

#Creating .txt files
import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup
for i, row in df.iterrows():

    # Get the URL_ID and URL from the current row
    url_id = row['URL_ID']
    url = row['URL']
    
    # Make a GET request to the URL and parse the HTML content using BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Find the article title and text using their HTML tags
    try:
      title = soup.find('h1').get_text().strip()
    except AttributeError:
      title = 'Untitled Article'
    article_text = '\n'.join([p.get_text().strip() for p in soup.find_all('p')])
    
    # Save the article text in a text file with URL_ID as the file name
    with open(f'{url_id}.txt', 'w', encoding='utf-8') as f:
        f.write(title + '\n\n')
        f.write(article_text)
        print(f"Creating {url_id}.txt file is done ✅")
