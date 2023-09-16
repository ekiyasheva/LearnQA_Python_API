import json
import pprint

json_text = '{"messages": [{"message": "This is the first message","timestamp": "2021-06-04 16:40:53"},{"message": "And this is a second message","timestamp": "2021-06-04 16:41:01"}]}'
obj_load = json.loads(json_text)

index = 1
for mess in obj_load["messages"]:
    if index == 2:
        print(mess["message"])
    else:
        index = index + 1
