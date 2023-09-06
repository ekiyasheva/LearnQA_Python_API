from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name":"User"})
json_parse_text = response.json()
print(json_parse_text["answer"])

response = requests.get("https://playground.learnqa.ru/api/get_text", params={"name":"User"})
try:
    json_parse_text = response.json()
    print(json_parse_text["answer"])
except JSONDecodeError:
    print("Response is not a JSON format")