import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import csv

translator = Translator()

url = 'https://www1.fips.ru/registers-doc-view/fips_servlet?DB=RUPAT&DocNumber='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0'
}

csv_file = open('data.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Dokumen', 'Penemuan', 'Terbit', 'Status'])

for docnumber in range(1, 10):
    req = requests.get(url+str(docnumber), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    judulp = soup.findAll('div', id='mainDoc')

    for it in judulp:
        halaman = it.find('div', id='top4').find('a').get_text(strip=False)
        judul = it.find('p', id='B542').get_text(strip=False)
        terbit = it.find('table', id='bib').get_text(strip=False)
        status = it.find('td', id='StatusR').get_text(strip=False)

        print('Dokumen:', halaman)

        detected_language = translator.detect(judul).lang
        translated_text = translator.translate(judul, src=detected_language, dest='id').text.replace('(54)', '')
        print('Penemuan:', translated_text, '\n')

        detected_language = translator.detect(terbit).lang
        translated_text2 = translator.translate(terbit, src=detected_language, dest='id').text.replace('(21) (22)', '')
        translated_text2 = translated_text2.replace('\n', '')
        labels = ['(21)', '(22)', '(45)', '(71)', '(72)', '(73)', '(24)', '(56)']
        for label in labels:
            translated_text2 = translated_text2.replace(label, '\n').replace('Aplikasi', 'Ditemukan')
        print(translated_text2)

        detected_language = translator.detect(status).lang
        translated_text3 = translator.translate(status, src=detected_language, dest='id').text.replace('tidak ada data', 'tidak ada pembaruan')
        print(translated_text3, '\n')
