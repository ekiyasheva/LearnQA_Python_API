import json

string_as_json = '{"answer":"Hello, User"}'
obj = json.loads(string_as_json)

key = "answer"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON не существует")

