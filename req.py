import requests
from bs4 import BeautifulSoup
from headers import headx

url = "https://www1.fips.ru/registers-doc-view/fips_servlet"

querystring = {
    "hasfast": "true",
    "authuser": "0",
    "format": "json",
    "DB": "RUPAT",
    "DocNumber": "199"
}
payload = ""

headers = headx()

response = requests.get(url, params=querystring, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)