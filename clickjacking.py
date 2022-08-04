import urllib.request
import requests
import json

urls = [
    'https://test.com', 'https://test_two.com'
]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

x_frame = []

for url in urls:
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        if 'X-Frame-Options' not in r.headers:
            x_frame.append('Missing Header/Missing anti-framing policy - X-Frame-Options')
        else: 
            x_frame.append(r.headers['X-Frame-Options'])
    else:
        print(f'Status code diferente de 200:, {r.status_code}, url: {url}')

clickjacking_dictionary = dict(zip(urls, x_frame))

# save json file
with open('result.json', 'w') as fp:
    json.dump(clickjacking_dictionary, fp)
    
