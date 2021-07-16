import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.linkedin.com/in/akshithkumar-05/')

soup = BeautifulSoup(req.content, 'html.parser')

res = soup.title
print(soup.get_text())