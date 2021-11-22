# Модули и прочая дичь
import requests
import json

# Константы
s_version = '0.0.1a'
# s_locale = 'ru'

# Берем данные об УЗ из конфига
auth_conf=open('auth.conf')
auth=auth_conf.read().splitlines()
api_username=str(auth[0])
api_password=str(auth[1])
api_url=str(auth[2])
auth_conf.close()

# Формируем запрос к API
headers = {'OCS-APIRequest': 'true', 'Accept': 'application/json'}

# Обращаемся к API
api_request = requests.get(api_url, headers=headers, auth=(api_username, api_password)).json()

# Выгружаем список пользователей (JSON)
api_users = api_request['ocs']['data']['users']

# Выводим спсиок пообъектно
for users in api_users:
    print(users)

# Вывод версии на всякий
#print(s_version)