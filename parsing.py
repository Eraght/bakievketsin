"=============================================Parsing=============================="
# парсинг - процесс фвтоматичекого сбора данных

# Библиотеки
# 1. requests - отправляет запрос на сайт и в итоге получает html код страницы.
# 2. Beautiful Soup - помогает извлеч информацию из html, такдже он помогает обращаться к определенным тегам и вытаскивать информацию.
# 3. lxml - выступает в роли парсера для BS (рзбивает информацию на мелкие части и анализирует данные)
# python3 -m venv venv - создание виртуального окружения

# source venv/bin/ativate - активировали виртуальное окружение
# . venv/bin/activate

import requests
from bs4 import BeautifulSoup as BS
import csv

URL = "https://enter.kg/computers/noutbuki_bishkek"


def get_html(url):
    response = requests.get(url)
    return response.text


def write_to_csv(data):
    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([data["title"], data["price"], data["image"]])


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # return soup.prettify()
    list_comp = soup.find_all("div", class_="row")
    dict_ = {}
    for comp in list_comp:
        title = comp.find("span", class_="prouct_name").text
        price = comp.find("span", class_="price").text
        image = "https://enter.kg" + comp.find("img").get("src")
        dict_ = {"title": title, "price": price, "image": image}
        write_to_csv(dict_)
        count = 1
        print(f"count->{count}")


# print(get_data(get_html(URL)))
count = 1
while True:
    print(f"count->{count}")
    get_data(get_html(URL))
    count += 1
