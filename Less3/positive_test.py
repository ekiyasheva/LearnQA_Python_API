import requests
class TestUserAuth:
    def test_auth_user(self):
        url_login = "https://playground.learnqa.ru/api/user/login"
        url_auth = "https://playground.learnqa.ru/api/user/auth"
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post(url_login, data=data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "There is no user id in the response"

        auth_id = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        print(user_id_from_auth_method)
        print(auth_id)
        print(token)

        response2 = requests.get(url_auth, headers={"x-csrf-token": token}, cookies={"auth_sid": auth_id})

        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_check_method = response2.json()["user_id"]
        print(user_id_check_method)

        assert user_id_from_auth_method == user_id_check_method, "User id from auth method is not equal to user id from check method"