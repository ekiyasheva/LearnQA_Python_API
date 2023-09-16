import time
import requests

ex_url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response_noparam = requests.get(ex_url)
json_resp_noparam = response_noparam.json()
ex_token = json_resp_noparam["token"]
ex_timeout = json_resp_noparam["seconds"]

response_param = requests.get(ex_url, params={"token": ex_token})
json_resp_param = response_param.json()

if json_resp_param["status"] == "Job is NOT ready":
    print(f"Задача в процессе создания, ожидаем {ex_timeout} секунд")

time.sleep(ex_timeout)
response_param = requests.get(ex_url, params={"token": ex_token})
json_resp_param = response_param.json()

if json_resp_param["status"] == "Job is ready":
    print(f"Задача создана успешно")

#ex_status = "None"

#print(json_resp_noparam)
#print(ex_token)
#print(ex_timeout)
#print(ex_status)
#ex_status = "None"

#while ex_status != "Job is ready":
#    response_param = requests.get(ex_url, params={"token": ex_token})
#    json_resp_param = response_param.json()
#    ex_status = json_resp_param["status"]
#    print(json_resp_param)
#    time.sleep(ex_timeout)