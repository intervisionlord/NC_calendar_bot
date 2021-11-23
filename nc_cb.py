# Модули и прочая дичь
import requests, json, yaml

# Константы, конфиги, переменные
s_version = '0.0.1a-04'

# Проверяем наличие DEV конфигов. Если есть, используем.
# Если нет, берем дефолтные
try:
    main_cfg = yaml.full_load(open('conf/DEV_api_conf.yml', 'r'))
    auth_cfg = yaml.full_load(open('conf/DEV_auth_conf.yml', 'r'))
except:
    main_cfg = yaml.full_load(open('conf/api_conf.yml', 'r'))
    auth_cfg = yaml.full_load(open('conf/auth_conf.yml', 'r'))
finally:
    api_url = main_cfg['ncapi']['url']
    api_username = auth_cfg['auth']['login']
    api_password = auth_cfg['auth']['password']

# s_locale = 'ru'
# Вынести ее в конфиг и подготовить что-то вроде локализации
#################

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