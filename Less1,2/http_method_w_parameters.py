import requests

payload = {"name":"User"}

response_get = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
#response_put = requests.put()
#response_del = requests.delete()
print(response_get.text)

response_get1 = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
print(response_get1.text)

response_post = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response_post.text)
