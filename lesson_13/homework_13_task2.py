import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('json__Alokhin.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


with open('task_json/localizations_en.json', 'r') as file1:
    try:
        file_content = file1.read()
        data = json.loads(file_content)
        print(data)
    except (json.JSONDecodeError, TypeError) as err:
        logging.error(f'localizations_en.json - not a JSON, {err}')

with open('task_json/localizations_ru.json', 'r') as file2:
    try:
        file_content = file2.read()
        data = json.loads(file_content)
    except (json.JSONDecodeError, TypeError) as err:
        logging.error(f'localizations_ru.json - not a JSON, {err}')

with open('task_json/login.json', 'r') as file3:
    try:
        file_content = file3.read()
        data = json.loads(file_content)
    except (json.JSONDecodeError, TypeError) as err:
        logging.error(f'login.json - not a JSON, {err}')

with open('task_json/swagger.json', 'r') as file4:
    try:
        file_content = file4.read()
        data = json.loads(file_content)
    except (json.JSONDecodeError, TypeError) as err:
        logging.error(f'sawgger.json - not a JSON, {err}')