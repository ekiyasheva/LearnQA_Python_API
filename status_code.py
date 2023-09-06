import requests

#response = requests.post("https://playground.learnqa.ru/api/check_type")
#print(response.status_code)

#response500 = requests.post("https://playground.learnqa.ru/api/any")
#print(response500.status_code)
#print(response500.text)

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Upgrade-Insecure-Requests': '1',
}
response301 = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True, headers=headers)
first_response = response301.history[0]
second_response = response301

print(first_response.url)
print(second_response.url)
print(response301.status_code)
#print(response301.text)