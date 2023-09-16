import requests

ex_url = "https://playground.learnqa.ru/api/compare_query_type"

# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response1 = requests.get(ex_url)
print(f"1) Ответ на запрос без параметра method: {response1.text}")

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response2 = requests.head(ex_url)
print(f"2) Ответ на запрос не из списка: {response2.text}")

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
payload = {"method": "GET"}
response3 = requests.get(ex_url, params=payload)
print(f"3) Ответ на правильный запрос: {response3.text}")

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

print("4) Перебор методов и параметров")
list = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
for gmas in list:
    response_get = requests.get(ex_url, params=gmas)
    print(f"GET response with {gmas} parameter is: {response_get.text}")
    response_post = requests.post(ex_url, data=gmas)
    print(f"POST response with {gmas} parameter is: {response_post.text}")
    response_put = requests.put(ex_url,data=gmas)
    print(f"PUT response with {gmas} parameter is: {response_put.text}")
    response_delete = requests.delete(ex_url, data=gmas)
    print(f"DELETE response with {gmas} parfmere is: {response_delete.text}")



