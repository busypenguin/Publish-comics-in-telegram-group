# Автоматическая отправка картинок 

Проект создан для автоматизации отправки комиксов Телеграм ботом в Телеграм канал. 

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```

### Переменные окружения

Создайте файл .env и запишите туда переменные окружения (TELEGRAM_BOT_TOKEN, TG_CHAT_ID) и их значения.

TELEGRAM_BOT_TOKEN вы получаете после создания телеграм-бота.
TG_CHAT_ID это путь к вашей группе в телеграме.

Например:

```TELEGRAM_BOT_TOKEN=87979801:AAHtAqqKhDexAHU1Hpaf3ukijguPBKA```

(это выдуманный токен)

### Запуск

Можете запустить код, написав в терминале:

```python3 main.py```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).