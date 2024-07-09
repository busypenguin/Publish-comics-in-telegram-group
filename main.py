import requests
import telegram
from environs import Env
import os
import random


def download_image(url, folder_path):
    filename = url.split("/")[-1]
    response = requests.get(url)
    response.raise_for_status()
    filepath = f'{folder_path}{filename}'
    with open(filepath, "wb") as file:
        file.write(response.content)
    return filepath


def get_random_url_response():
    random_num_comics = random.randint(1, 2600)
    url = f"https://xkcd.com/{random_num_comics}/info.0.json"
    response = requests.get(url)
    response_json = response.json()
    return response_json


if __name__ == '__main__':
    env = Env()
    env.read_env()
    telegram_bot_token = env.str('TELEGRAM_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)

    os.makedirs('images/', exist_ok=True)

    filepath = download_image(get_random_url_response()['img'], 'images/')
    with open(filepath, 'rb') as photo:
        bot.send_message(tg_chat_id, get_random_url_response()['alt'])
        bot.send_photo(tg_chat_id,  photo)
        os.remove(filepath)
