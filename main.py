import requests
import telegram
from environs import Env
import os
import os.path
from urllib.parse import urlparse
import random


def download_image(url, folder_path):
    filename = os.path.split(url)[1]
    response = requests.get(url)
    response.raise_for_status()
    filepath = f'{folder_path}{filename}'
    with open(filepath, "wb") as file:
        file.write(response.content)
    return filepath


def get_random_url_response():
    min_comics_value = 1
    max_comics_value = 2600
    random_num_comics = random.randint(min_comics_value, max_comics_value)
    url = f"https://xkcd.com/{random_num_comics}/info.0.json"
    response = requests.get(url)
    comics = response.json()
    return comics


if __name__ == '__main__':
    env = Env()
    env.read_env()
    telegram_bot_token = env.str('TELEGRAM_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)

    folder = os.path.join('images/')
    os.makedirs(folder, exist_ok=True)
    filepath = download_image(get_random_url_response()['img'], folder)
    try:
        with open(filepath, 'rb') as photo:
            bot.send_message(tg_chat_id, get_random_url_response()['alt'])
            bot.send_photo(tg_chat_id,  photo)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    finally:
        os.remove(filepath)
