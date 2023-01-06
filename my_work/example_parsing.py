import requests
from bs4 import BeautifulSoup as BS

def get_product_data(product_box:BS) -> dict:
    title = product_box.find('div', {'class':'product_title'}).text
    price = product_box.find('div', {'class':'product_price'}).text.strip()
    image = product_box.find('div', {'class':'product_img'}).find('img').get('src')
    return {"title":title, "price":price, "image":image}

def get_all_products(soup:BS) -> list:
    products = []
    for product_box in soup.find_all('div', {'class':'product_box'}):
        product_data = get_product_data(product_box)
        products.append(product_data)
    return products

def get_soup(url:str) -> BS:
    response = requests.get(url)
    html = response.text
    soup = BS(html, 'lxml')
    return soup

def main():
    soup = get_soup('https://www.kivano.kg/')
    products = get_all_products(soup)
    # write_to_json(products)
    return products

print(main())