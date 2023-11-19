import requests
from bs4 import BeautifulSoup


def USD():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[3].text
    return price


def EUR():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[8].text
    return price


def BRL():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[43].text
    return price


def KRW():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[53].text
    return price


def HKD():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[58].text
    return price


def AED():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[68].text
    return price


def INR():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[73].text
    return price


def CNY():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[93].text
    return price


def GBP():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[153].text
    return price


def JPY():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[178].text
    return price
