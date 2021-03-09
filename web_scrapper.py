import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://www.onlinecarparts.co.uk/car-brands/spare-parts-ford/fiesta-vi/58967/10130/brake-pad-set.html"

#58967 --> to iterate through different models in the fiesta
#10130

header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "referer": "https://www.google.com/"
}

s = requests.Session()

response = s.get(url, headers=header)

soup = BeautifulSoup(response.content, features='lxml')

print(soup.prettify())


