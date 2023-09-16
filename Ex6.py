import requests

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Upgrade-Insecure-Requests': '1',
}
response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True, headers=headers)

for r in response.history:
    print(r.url)