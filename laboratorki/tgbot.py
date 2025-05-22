import telebot
import requests
import random


token = '7912369351:AAF4IlZpP9reiR3rs8n8rglbc3myH-NI_Pk'
API_KEY = '46cb095b9903c9e08a63ca80c1d57896'
bot = telebot.TeleBot(token)

user_data = {}

main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row('ℹ️ Помощь', '✏️ Сменить имя', '🎲 Случайное фото достопримечательности')
main_keyboard.row('⛅️ Погода', '🏛 Достопримечательности', '🍽 Где поесть', '👥 Создатели')

waiting_for_name = {}

@bot.message_handler(commands=['start'])
def send_greeting(message):
    bot.send_message(message.chat.id, 'Привет! Пожалуйста, введи свое имя.', reply_markup=main_keyboard)
    waiting_for_name[message.chat.id] = True
    user_data[message.chat.id] = {'name': None}

@bot.message_handler(func=lambda message: message.chat.id in waiting_for_name and waiting_for_name[message.chat.id])
def set_name(message):
    if message.text not in ['ℹ️ Помощь', '✏️ Сменить имя', '🎲 Случайное фото достопримечательности',
                          '⛅️ Погода', '🏛 Достопримечательности', '🍽 Где поесть',
                          '⬅️ Назад', '👥 Создатели']:
        user_data[message.chat.id]['name'] = message.text
        waiting_for_name[message.chat.id] = False
        bot.send_message(message.chat.id, f'Спасибо, {message.text}!', reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, введите именно имя, а не выбирайте команды.')

@bot.message_handler(func=lambda message: message.text == 'ℹ️ Помощь')
def help_command(message):
    help_text = '''Информация о функциях:
ℹ️ Помощь - Эта информация
✏️ Сменить имя - позволяет смеенить имя
🎲 Случайное фото достопримечательности - Фото случайной достопримечательности Томска
⛅️ Погода - Погода в Томске
🏛 Достопримечательности - Описание мест, изображённых на фото
🍽 Где поесть - Места с едой
👥 Создатели - информация о создателях'''
    bot.send_message(message.chat.id, help_text, reply_markup=main_keyboard)

@bot.message_handler(func=lambda message: message.text == '✏️ Сменить имя')
def rename_command(message):
    bot.send_message(message.chat.id, 'Введите новое имя:')
    waiting_for_name[message.chat.id] = True

@bot.message_handler(func=lambda message: message.text == '🎲 Случайное фото достопримечательности')
def send_random_photo(message):
    if message.chat.id in user_data and user_data[message.chat.id]['name']:
        photo_links = [
            ('https://upload.wikimedia.org/wikipedia/ru/0/0f/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%A7%D0%B5%D1%85%D0%BE%D0%B2%D1%83_%28%D0%A2%D0%BE%D0%BC%D1%81%D0%BA%29.jpg',
             'Памятник Чехову'),
            ('https://upload.wikimedia.org/wikipedia/commons/2/21/%D0%A1%D0%BA%D0%B2%D0%B5%D1%80_%D0%BD%D0%B0_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%BE%D0%B1%D0%BE%D1%80%D0%BD%D0%BE%D0%B9_%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%B8.jpg',
             'Новособорная площадь'),
            ('https://harmonia.tomsk.ru/files/pamyatniki/polus1.jpg', 'Мемориал Создателям космической техники'),
        ]
        link = random.choice(photo_links)
        bot.send_photo(message.chat.id, link[0], caption=f"{user_data[message.chat.id]['name']}, вот фото случайной достопримечательности:\n{link[1]}", reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, "Сначала введите ваше имя с помощью команды /start", reply_markup=main_keyboard)

@bot.message_handler(func=lambda message: message.text == '⛅️ Погода')
def send_weather(message):
    city = 'Томск'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=ru&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('cod') != 200:
            bot.send_message(message.chat.id, 'Город не найден или ошибка API.')
            return

        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        bot.send_message(message.chat.id,
                        f'{user_data[message.chat.id]['name']}, погода в {city}е:\nТемпература: {temperature}°C\nОписание: {weather_description}')
    except Exception as e:
        bot.send_message(message.chat.id, 'Произошла ошибка при получении данных о погоде.')


#@bot.message_handler(func=lambda message: message.text == '👥 Создатели')
#def credits(message):
    #bot.send_message(message.chat.id, "Бота создавали:\nСавушкин Григорий Данилович\nПожидаев Роман Дмитриевич\nСтуденты группы 632", reply_markup=keyworld)



@bot.message_handler(func=lambda message: message.text == '🏛 Достопримечательности')
def description_command(message):
    description_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    description_menu.row('🏛 Памятник Чехову', '⛲️ Новособорная площадь', '🚀 Мемориал')
    description_menu.row('⬅️ Назад')
    bot.send_message(message.chat.id, 'Выберите достопримечательность:', reply_markup=description_menu)

@bot.message_handler(func=lambda message: message.text == '🏛 Памятник Чехову')
def send_chekhov_address(message):
    bot.send_message(message.chat.id,
                         'Бронзовый памятник Антону Павловичу Чехову, установленный в честь 400-летия Томска на набережной реки Томь. Его авторами являются Леонтий Усов и Максим Петров, а сам памятник был создан на народные деньги!')

@bot.message_handler(func=lambda message: message.text == '⛲️ Новособорная площадь')
def send_square_address(message):
    bot.send_message(message.chat.id,
                         '"Но́во-Собо́рная — Площадь в Томске. Образована проспектом Ленина, проездом к Спортивному переулку, Советской улицей и подъездом к городскому саду от проспекта Ленина. На момент основания Томска (1604) исторический район Подгорная (Нижняя) Елань, где позже появится площадь, представлял собой вековую целину, которую весной 1605 года вспахали и засеяли, превратив в «государеву пашню»"')

@bot.message_handler(func=lambda message: message.text == '🚀 Мемориал')
def send_memorial_address(message):
    bot.send_message(message.chat.id,
                         'Он находится на площади Кирова и был открыт открыт 08.07.2011 года в день 60-летия НПО "Полюс". В композицию мемориала входят памятник Петру Васильевичу Голубеву, основателю НПО "Полюс". Уменьшенный макет ракеты "Протон" (без первой ступени), выполненный в масштабе 1:3 и два спутника. Высота ракеты - 12,8 метра. Скульптором мемориала является Антон Гнедых.')

@bot.message_handler(func=lambda message: message.text == '🍽 Где поесть')
def food_command(message):
    food_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    food_menu.row('🌯 Лучшая шаурма в Томске', '🍜 Азиатская кухня', '🍔 Фуд-корт')
    food_menu.row('⬅️ Назад')
    bot.send_message(message.chat.id, 'Выберите что вы хотите покушать:', reply_markup=food_menu)

@bot.message_handler(func=lambda message: message.text in ['🌯 Лучшая шаурма в Томске'])
def send_bezumno_location(message):
    bot.send_location(message.chat.id, 56.4517, 84.9742)
    bot.send_message(message.chat.id, f'{user_data[message.chat.id]['name']}, тут продается лучшая шаурма в Томске!')

@bot.message_handler(func=lambda message: message.text in ['🍜 Азиатская кухня'])
def send_ramen_location(message):
    bot.send_location(message.chat.id, 56.4780, 84.9502)
    bot.send_message(message.chat.id, f'{user_data[message.chat.id]['name']}, здесь подают очень вкуные блюда азиатской кухни!')


@bot.message_handler(func=lambda message: message.text in ['🍔 Фуд-корт'])
def send_lampochka_location(message):
    bot.send_location(message.chat.id, 56.4647, 84.9572)
    bot.send_message(message.chat.id, f'{user_data[message.chat.id]['name']}, Лампочка - хороший гастрохолл, где есть множество различных заведений!')

@bot.message_handler(func=lambda message: message.text == '⬅️ Назад')
def back_command(message):
    bot.send_message(message.chat.id, 'Возвращаемся в главное меню.', reply_markup=main_keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.id in waiting_for_name and waiting_for_name[message.chat.id]:
        set_name(message)
    else:
        bot.reply_to(message, 'Команда не распознана. Нажмите "ℹ️ Помощь" для информации.', reply_markup=main_keyboard)

bot.infinity_polling()

