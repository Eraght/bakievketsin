import requests
from bs4 import BeautifulSoup as BS
import csv

def write_to_csv(dict_):
    with open("jk.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([dict_["title"], dict_["img"], dict_["date"]])

def process_info(soup):
    info_title = soup.find_all("a", class_="news__item__title__link")
    info_image = soup.find_all("img", class_="news__item__image__img")
    info_date = soup.find_all("div", class_="news__item__date")

    for title, image, date in zip(info_title, info_image, info_date):
        title_ready = title.text.strip()
        image_ready = "kenesh/kg" + image.get("src")
        date_ready = date.text.strip()

        dict_ = {"title": title_ready, "img": image_ready, "date": date_ready}
        write_to_csv(dict_)

def parse_multiple_pages(start_page, end_page):
    for page in range(start_page, end_page + 1):
        url = f"http://kenesh.kg/ru/news/all/list?page={page}"
        response = requests.get(url).text
        soup = BS(response, "lxml")
        process_info(soup)

parse_multiple_pages(1, 21)
























































# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# url = "http://kenesh.kg/ru/news/all/list?page=1"
# response = requests.get(url).text
# soup = BS(response, "lxml")


# def write_to_csv(dict_):
#     with open("jk.csv", "a") as file:
#         writer = csv.writer(file)
#         writer.writerow([dict_["title"], dict_["img"], dict_["date"]])


# def process_info(soup):
#     info_title = soup.find_all("a", class_="news__item__title__link")
#     info_image = soup.find_all("img", class_="news__item__image__img")
#     info_date = soup.find_all("div", class_="news__item__date")
#     data_list = []

#     for title, image, date in zip(info_title, info_image, info_date):
#         title_ready = title.text.strip()
#         image_ready = "kenesh/kg" + image.get("src")
#         date_ready = date.text.strip()

#         dict_ = {"title": title_ready, "img": image_ready, "date": date_ready}
#         print(dict_)

#         write_to_csv(dict_)


# process_info(soup)

# Парсинг работает теперь нужно создать функцию которая будет продолжать парсить следующие 20 страниц
# http://kenesh.kg/ru/news/all/list?page=1
# http://kenesh.kg/ru/news/all/list?page=2
# http://kenesh.kg/ru/news/all/list?page=3 и так далее

















# dict_= {}

# info_title = soup.find_all("a", class_="news__item__title__link")
# for title in info_title:
#     title_ready = title.text.strip()
#     # dict_ = {"title": title_ready}
#     # write_to_csv(dict_)
#     print(dict_)

# info_image = soup.find_all("img", class_="news__item__image__img")
# for image in info_image:
#     image_ready = 'kenesh/kg' +image.get('src')
#     # print(image_ready)
#     dict_ = {"title": title_ready,"img": image_ready, 'date': date_ready}
#     write_to_csv(dict_)


# info_date = soup.find_all("div", class_="news__item__date")
# for date in info_date:
#     date_ready = date.text.strip()
#     # dict_={'date': date_ready}
#     write_to_csv(dict_)
