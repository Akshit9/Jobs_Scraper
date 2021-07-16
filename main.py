from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.mathsisfun.com/data/data.html')

soup = BeautifulSoup(req.content, 'lxml')
# print(soup.get_text())

header_tags = soup.find_all('div', id='content')

for header in header_tags:
    header_1 = header.h1.text
    info_1 = header.p.text

    header_2 = header.h2.text
    info_2 = header.li.text

    print(header_1)
    print(info_1)
    print('\n')
    print(header_2)
    print(info_2)
