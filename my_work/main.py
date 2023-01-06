import csv
import requests
from bs4 import BeautifulSoup as BS

main_url = 'https://www.mashina.kg/search/all/'

def get_soup(url: str) -> BS:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    response = requests.get(url, headers = headers)
    return BS(response.text, 'lxml')

def get_all_cars_from_page(soup: BS) -> list:
    products = []
    for product in soup.find_all('div', {'class':'list-item'}):
        product_info = get_car_info(product)
        products.append(product_info)
    return products

def write_to_csv(data):
    with open('cars_mashina.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'], data['price'], data['info'], data['photo']))

def get_car_info(car: BS) -> dict:
    photo = car.find('a').find('img').get('data-src')
    title = car.find('div', class_="block title").text.replace('\n','').strip()
    price = car.find('div', class_="block price").text.replace('\n', '').split()
    info = car.find('div', class_="block info-wrapper item-info-wrapper").text.replace('\n', '').split()
    data = {'title': title, 'price': price, 'info': info, 'photo':photo}
    write_to_csv(data)
    return data

def get_total_pages (soup):
    pages_ul = soup.find('div', class_="search-results-table").find('ul', class_='pagination')
    last_page = pages_ul.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    return int(total_pages)
    
def get_data_by_category(category: str) -> dict:
    soup = get_soup(main_url + category)
    last_page = get_total_pages(soup)
    all_cars = []
    for page in range(1, last_page+1):
        print(f'{main_url}{category}?page={page}')
        soup = get_soup(f'{main_url}{category}?page={page}')
        products = get_all_cars_from_page(soup)
        all_cars.extend(products)
    return {category: all_cars}

def main():
    categories = main_url
    all_data = {}
    for category in categories:
        data = get_data_by_category(category)
        all_data.update (data)

main()






