import csv
import requests
import time
from bs4 import BeautifulSoup
from googletrans import Translator
from colorama import Fore, Style
from headers import headx
import io

translator = Translator()

headers = headx()

max_retries = 10
retry_delay = 1  # Delay in seconds

with open('Data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    lines = list(reader)

with io.open('Data.csv', 'a', newline='', encoding='utf-8', buffering=1) as csvfile:
    writer = csv.writer(csvfile)

    with open('proxy.txt', 'r') as f:
        proxy_list = f.read().split('\n')

    translated_texts = set()
    if lines:
        translated_texts = set((line[0], line[1]) for line in lines if len(line) > 1)

    for docnumber in range(913, 10000):
        retries = 0
        while retries < max_retries:
            try:
                url = "https://www1.fips.ru/registers-doc-view/fips_servlet"

                querystring = {
                    "hasfast": "true",
                    "authuser": "0",
                    "format": "json",
                    "DB": "RUPAT",
                    "DocNumber": str(docnumber)
                }

                payload = ""

                proxy = proxy_list[retries % len(proxy_list)]

                proxies = {'http': proxy, 'https': proxy}

                req = requests.get(url, params=querystring, headers=headers, proxies=proxies)
                req.raise_for_status()

                if 'Документ с данным номером отсутствует' in req.text:
                    print(Fore.YELLOW + f'Skipping document number={docnumber} - "Документ с данным номером отсутствует"')

                    doc_not_available = (docnumber, 'Dokumen Tidak Tersedia')
                    if doc_not_available not in translated_texts:
                        writer.writerow(doc_not_available)
                        translated_texts.add(doc_not_available)

                    break

                soup = BeautifulSoup(req.text, 'html.parser')
                judulp = soup.findAll('div', id='mainDoc')

                if judulp:
                    it = judulp[0]
                    halaman = it.find('div', id='top4').find('a').get_text(strip=True)
                    judul = it.find('p', id='B542').get_text(strip=True)

                    detected_language = translator.detect(judul).lang
                    translated_text = translator.translate(judul, src=detected_language, dest='id').text.replace('(54)', '')

                    print(Fore.BLUE + '>' + Fore.RED + '[' + halaman + ']' + Fore.GREEN + ' Penemuan:' + Style.RESET_ALL + translated_text)

                    if (halaman, translated_text) not in translated_texts:
                        writer.writerow([halaman, translated_text])
                        translated_texts.add((halaman, translated_text))

                    break

            except Exception as e:
                print(Fore.RED + f'Identitas di blokir untuk nomor dokumen={docnumber}. Sedang mencoba lagi...')
                retries += 1
                if retries < max_retries:
                    time.sleep(retry_delay)

                proxy_list.remove(proxy)
                with open('proxy.txt', 'w') as f:
                    f.write('\n'.join(proxy_list))

                continue

        else:
            print(Fore.RED + f'Permintaan gagal untuk nomor dokumen={docnumber} setelah {max_retries} percobaan. Melanjutkan ke nomor dokumen berikutnya.')
            break
