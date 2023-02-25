import requests
from bs4 import BeautifulSoup
import lxml
url = "https://rozetka.com.ua/ua/avtomobilnie-invertori/c4639256/"
agent = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
respons = requests.get(url, headers=agent)
sout = BeautifulSoup(respons.text, "lxml")

all_product = sout.find('ul', class_='catalog-grid ng-star-inserted')
list_produxt = all_product.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
# print(list_produxt[0].text)
for elem in list_produxt:
    title = elem.find('span', class_='goods-tile__title')
    print(elem.text)
    with open('product.txt', "a", encoding="UTF8") as f:
        f.write(f'{elem.text}, \n')
