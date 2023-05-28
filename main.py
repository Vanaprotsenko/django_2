from bs4 import BeautifulSoup
import requests


enter = str(input())

url = f'https://ua.sinoptik.ua/погода-{enter}/2023-05-27'


result = requests.get(url)

soup = BeautifulSoup(result.text,'html.parser')

def find_city():
    mini = soup.find('div',{'class':'min'})
    maxi = soup.find('div',{'class':'max'})
    print(f'Мінімальна температура {mini} та максимальна {maxi}')

find_city()