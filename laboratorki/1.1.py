import telebot
import requests
import random

token = '7912369351:AAF4IlZpP9reiR3rs8n8rglbc3myH-NI_Pk'
API_KEY = '46cb095b9903c9e08a63ca80c1d57896'
bot = telebot.TeleBot(token)

user_first_name = None

keyworld = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyworld.row('/help')
keyworld.row('/rename')
keyworld.row('/random')
keyworld.row('/weather')
keyworld.row('/location')


@bot.message_handler(commands=['start'])
def send_greeting(message):
    bot.send_message(message.chat.id, 'Привет! Пожалуйста, введи свое имя.')


@bot.message_handler(func=lambda message: user_first_name is None)
def set_name(message):
    global user_first_name
    user_first_name = message.text
    bot.send_message(message.chat.id, f'Спасибо, {user_first_name}! Теперь я буду обращаться к тебе по имени.',
                     reply_markup=keyworld)


@bot.message_handler(commands=['weather'])
def send_weather(message):
    city = 'Томск'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=ru&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        bot.send_message(message.chat.id, 'Город не найден или ошибка API.')
        return

    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    bot.send_message(message.chat.id,
                     f'Погода в {city}:\nТемпература: {temperature}°C\nОписание погодных условий: {weather_description}')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Информация о командах:\n/help - Выдает информацию о командах',
                     reply_markup=keyworld)


@bot.message_handler(commands=['rename'])
def rename_command(message):
    bot.send_message(message.chat.id, 'Введите новое имя, которым я буду к вам обращаться:')


@bot.message_handler(
    func=lambda message: user_first_name is not None and message.text not in ['/help', '/rename', '/random', '/weather',
                                                                              '/location'])
def change_name(message):
    global user_first_name
    user_first_name = message.text
    bot.send_message(message.chat.id, f'Имя обновлено на {user_first_name}!', reply_markup=keyworld)


@bot.message_handler(commands=['random'])
def send_random_photo(message):
    photo_links = [
        ('https://upload.wikimedia.org/wikipedia/ru/0/0f/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%A7%D0%B5%D1%85%D0%BE%D0%B2%D1%83_%28%D0%A2%D0%BE%D0%BC%D1%81%D0%BA%29.jpg',
         'Памятник Чехову.'),
        ('https://upload.wikimedia.org/wikipedia/commons/2/21/%D0%A1%D0%BA%D0%B2%D0%B5%D1%80_%D0%BD%D0%B0_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%BE%D0%B1%D0%BE%D1%80%D0%BD%D0%BE%D0%B9_%D0%BF%D0%BB%D0%BE%D89%B8.jpg',
         'Новособорная площадь'),
        ('https://harmonia.tomsk.ru/files/pamyatniki/polus1.jpg', 'Мемориал Создателям космической техники'),
    ]
    link = random.choice(photo_links)
    bot.send_photo(message.chat.id, link[0], caption=link[1])


@bot.message_handler(commands=['location'])
def location_command(message):
    location_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    location_menu.row('/chekhov')
    location_menu.row('/square')
    location_menu.row('/memorial')

    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=location_menu)
    @bot.message_handler(commands=['chekhov'])
    def chekhov_command(message):
        bot.send_message(message.chat.id, 'Памятник Чехову...', reply_markup=keyworld)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Команда не распознана. Используйте /help для получения помощи.')


bot.infinity_polling()