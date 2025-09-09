
import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    data.append({'Title': title, 'Price': price})
    print(f'Title: {title}, Price: {price}')

# Simpan ke CSV
import pandas as pd
df = pd.DataFrame(data, columns=['Title', 'Price'])
df.to_csv('books_data.csv', index=False)