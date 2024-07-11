import requests
import telegram
from environs import Env
import os
import os.path
import random
import shutil


def download_image(url, folder_path):
    filename = os.path.split(url)[1]
    response = requests.get(url)
    response.raise_for_status()
    filepath = f'{folder_path}{filename}'
    with open(filepath, "wb") as file:
        file.write(response.content)
    return filepath


def get_random_comic():
    min_comics_value = 1
    max_comics_value = 2600
    random_num_comics = random.randint(min_comics_value, max_comics_value)
    url = f"https://xkcd.com/{random_num_comics}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()
    return comic


if __name__ == '__main__':
    env = Env()
    env.read_env()
    telegram_bot_token = env.str('TELEGRAM_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)

    folder = os.path.join('images/')
    os.makedirs(folder, exist_ok=True)

    try:
        filepath = download_image(get_random_comic()['img'], folder)
        with open(filepath, 'rb') as photo:
            bot.send_message(tg_chat_id, get_random_comic()['alt'])
            bot.send_photo(tg_chat_id,  photo)
    except requests.exceptions.HTTPError:
        print('Данная ссылка не работает')
    except requests.exceptions.JSONDecodeError:
        print('Несуществующая ссылка')
    except requests.exceptions.ConnectionError:
        print('Отсутствует подключение к интернету')
    finally:
        shutil.rmtree(folder)
