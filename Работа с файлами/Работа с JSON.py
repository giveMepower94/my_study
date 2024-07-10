import json
from random import randint
from datetime import datetime
from pprint import pprint

str_json = """
{
"response": {
    "count": 5961880,
    "items": [
        {
        "first_name": "John",
        "last_name": "Doe",
        "id": 1234567890
        }, {
        "first_name": "Иван",
        "last_name": "Иванов",
        "id": 1234567891
        }]
    }    
}
"""

# print(type(str_json))  # <class 'str'>

data = json.loads(str_json)
# print(type(data))  # <class 'dict'>

for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(0, 100)
    item['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# print(data['response']['items'])


# make var data to json and create file json
# with open('data.json', 'w', encoding='utf-8') as file:
#     if json.dump(data, file, indent=3, ensure_ascii=False):
#         print('Файл создан')


# read file json
with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
    pprint(data)