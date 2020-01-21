import pymysql
import requests
from bs4 import BeautifulSoup
import time

url = 'http://nj.sell.house365.com/district/'

def get_html_info(url):
    results = requests.get(url)
    soap = BeautifulSoup(results.text)
    return soap

def get_links(url):
    soap = get_html_info(url)
    links_div = soap.find_all('div', class_ = "listItem__pic fl")
    links = [div.a.get('href') for div in links_div]
    return links

def get_house_info(url):
    soap = get_html_info(url)
    price = soap.find('div', class_ = 'infoDetail__title clearfix').span.get_text()[0:10]
    area = soap.find('div', class_='infoDetail__BarL fl').p.get_text()
    fixture = soap.find('div', class_='infoDetail__BarL fl').div.get_text()
    layout = soap.find('div', class_='infoDetail__BarM fl').p.get_text().strip()
    floor = soap.find('div', class_='infoDetail__BarM fl').div.get_text().strip()
    orientations = soap.find('div', class_='infoDetail__BarR fl').p.get_text().strip()
    years = soap.find('div', class_='infoDetail__BarR fl').div.get_text().strip()
    community = soap.find('div', class_='infoDetail__item long').a.get_text()

    house_info = {
        "price": price,
        "area": area,
        "fixture": fixture,
        "layout": layout,
        "floor": floor,
        "orientation": orientations,
        "years": years,
        "community": community
    }
    print(house_info)

    return house_info

if __name__ == '__main__':
    links = get_links(url)
    for link in links:
        time.sleep(5)
        values = get_house_info(link)
        value = "'{}',"*7 + "'{}'"
        sql_values = value.format(values['price'],
                                   values['area'],
                                   values['fixture'],
                                   values['layout'],
                                   values['floor'],
                                   values['orientation'],
                                   values['years'],
                                   values['community'])
        print(sql_values)
        break
