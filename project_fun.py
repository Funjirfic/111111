import requests
from bs4 import BeautifulSoup


def USD():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[3].text
    return float(f'{price}')


def EUR():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[8].text
    return float(f'{price}')


def BRL():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[43].text
    return float(f'{price}')


def KRW():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[53].text
    return float(f'{price}')


def HKD():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[58].text
    return float(f'{price}')


def AED():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[68].text
    return float(f'{price}')


def INR():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[73].text
    return float(f'{price}')


def CNY():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[93].text
    return float(f'{price}')


def GBP():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[153].text
    return float(f'{price}')


def JPY():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[178].text
    return float(f'{price}')

