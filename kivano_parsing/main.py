import requests
from bs4 import BeautifulSoup as BS

main_url = 'https://www.kivano.kg'

def get_soup(url: str) -> BS:
    """
    Принимает ссылку, отправляет запрос.
    Возвращает обьект BeautifulSoup с этой страницы
    """
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'}
    import time
    time.sleep(5)
    response = requests.get(url, headers=headers)
    return BS(response.text, 'lxml')

def get_all_products_from_page(soup: BS) -> list:
    """
    Принимает суп страницы, ищет все блоки с данными о продуктах.
    """
    products = []
    for product in soup.find_all('div', {'class':'product_listbox'}):
        product_info = get_product_info(product)
        products.append(product_info)
    return products

# <div class = "listbox_img"> <img src="1234567890.jpg"></img> </div>
# <div class = "listbox_img"> </div>
# <div class = "listbox_img"> </div>
# <div class = "listbox_img"> </div>

def get_product_info(product: BS) -> dict:
    """
    Принимает блок данных о продукте. Находит title, price, image. Возвращает данные ввиде словаря
    """
    title = product.find('div', {'class':'listbox_title'}).text.strip()
    # extract - вырезает элемент из soup
    # product.find('div', {'class':'listbox_title'}).extract()
    # desc = product.find('div', {'class':'product_text'}).text
    image = product.find('div', {'class':'listbox_img'}).find('img').get('src')
    price = product.find('div', {'class':'listbox_price'}).text.strip()
    return {'title':title, 'price':price, 'image':create_full_image_url(image)}

def create_full_image_url(url: str):
    return main_url + url

def get_last_page(soup: BS):
    ul = soup.find('ul', {'class':'pagination'})
    if ul is None:
        return 1
    last = ul.find('li', {'class':'last'})
    return int(last.text)

def write_to_db(data):
    """
    Принимает данные и запиывает их в файл db.json
    """
    import json
    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_all_categories() -> list:
    """
    Находит все категории и возвращает список с ссылками на категории
    """
    soup = get_soup(main_url)
    categories = []
    menu_items = soup.find_all('div', {'class':'leftmenu-item'})
    for menu_item in menu_items:
        a = menu_item.find('div', {'class':'leftmenu-title'}).find('a')
        categories.append(a.get('href'))
    return categories

def get_data_by_category(category:str) -> dict:
    soup = get_soup(main_url + category)
    last_page = get_last_page(soup)
    all_products = []
    for page in range(1, last_page + 1):
        print(f'{main_url}{category}?page={page}')
        soup = get_soup(f'{main_url}{category}?page={page}')
        products = get_all_products_from_page(soup)
        all_products.extend(products)
    return {category: all_products}

get_product_info()



def main():
    categories = get_all_categories()
    all_data = {}
    for category in categories:
        data = get_data_by_category(category)
        all_data.update(data)
    # write_to_db(all_data)

main()