import requests as req
from bs4 import BeautifulSoup as bs4
import pandas as pd

book_list = []
for i in range(1,6):
    # Set up the request uri
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    response = req.get(url)
    response = response.content

    soup = bs4(response,'html.parser')

    ol = soup.find('ol')
    books = ol.find_all('article', class_="product_pod")

    
    for book in books:
        book_image = book.find('img')
        book_title = book_image.attrs['alt']

        book_rating =  book.find('p')
        book_rating = book_rating['class'][1]

        book_price = book.find('p',class_='price_color').text
        book_price = float(book_price[1:])

        book_list.append([book_title, book_price, book_rating])


# Import to csv

data = pd.DataFrame(book_list, columns=['Book Title', 'Book Price', 'Book rating'])
data.to_csv('data/book_list.csv')



    
    
