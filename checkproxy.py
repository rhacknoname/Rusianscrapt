import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open('proxylist.txt', 'r')as f:
    proxy = f.read().split('\n')
    for p in proxy:
        q.put(p)

def check_proxy():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get('https://www1.fips.ru/registers-doc-view/fips_servlet?DB=RUPAT&DocNumber=1',
                               proxies={'http': proxy,
                                        'https': proxy})
        except :
            continue
        if res.status_code == 200:
            print(proxy)

for _ in range(10):
    threading.Thread(target=check_proxy).start()