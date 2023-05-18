import requests

def make_request(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, allow_redirects=False)
        if response.status_code == 302 or response.status_code == 301:
            redirect_url = response.headers['Location']
            print('Redirected to:', redirect_url)
        else:
            response.raise_for_status()  # Menghasilkan exception jika permintaan gagal
            # Lakukan sesuatu dengan respons di sini
            print('Success')
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    except requests.exceptions.ProxyError as e:
        print('Proxy Error:', e)

def rotate_proxies():
    url = 'http://www1.fips.ru/registers-doc-view/fips_servlet?DB=RUPAT&DocNumber=1'
    with open('proxy.txt', 'r') as f:
        proxy_list = f.read().split('\n')

    for proxy in proxy_list:
        print('Using proxy:', proxy)
        make_request(url, proxy)

rotate_proxies()
