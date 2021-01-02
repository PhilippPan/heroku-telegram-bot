# -*- coding: utf-8 -*-
#import redis
import os
import telebot
# import some_api_lib
import random

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)

# Указываем токен
bot = telebot.TeleBot('1418295425:AAFnAQAcOiwCnHfJYBWckmN6hbAmmrTQfJY')

# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Заготовки для трёх предложений
first = ["ответ 11", "ответ 12", "ответ 13", "ответ 14", "ответ 15"]


# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    admin_id = 319203907
    if message.text == "Привет" or message.text == "привет" or message.text == "/start":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, я бот для выезда #f2f_starlight. Могу тебе подсказать что-то, если  будут вопросы. Напиши сам вопрос или...")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждой кнопки
        key_schedule = types.InlineKeyboardButton(text='Расписание', callback_data='schedule')
        # И добавляем кнопку на экран
        keyboard.add(key_schedule)
        key_daylyverse = types.InlineKeyboardButton(text='Стих дня', callback_data='verse')
        keyboard.add(key_daylyverse)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='выбери, что нужно', reply_markup=keyboard)
    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")
    elif message.from_user.id == admin_id and str(message.text).startswith("!! "):
        to_id = str(message.text).split(" ")[1]
        bot.send_message(to_id, str(message.text).lstrip("!! " + to_id))
    else:
        bot.send_message(319203907, str(message.from_user.id))
        bot.send_message(319203907, " отправил вам сообщение: " + str(message.text))


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
# Если нажали на одну из 12 кнопок — выводим инфу
def callback_worker(call):
    def showMenu():
        keyboard = types.InlineKeyboardMarkup()

        key_schedule = types.InlineKeyboardButton(text='Расписание', callback_data='schedule')
        keyboard.add(key_schedule)

        key_verse = types.InlineKeyboardButton(text='Стих дня', callback_data='verse')
        keyboard.add(key_verse)

        msg = "\nВыбери, что нужно"
        bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)

    if call.data == "schedule":
        #                    Формируем ответ
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()

        key_d1 = types.InlineKeyboardButton(text='День 1', callback_data='d1')
        keyboard.add(key_d1)

        key_d2 = types.InlineKeyboardButton(text='День 2', callback_data='d2')
        keyboard.add(key_d2)

        key_d3 = types.InlineKeyboardButton(text='День 3', callback_data='d3')
        keyboard.add(key_d3)

        key_d4 = types.InlineKeyboardButton(text='День 4', callback_data='d4')
        keyboard.add(key_d4)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        msg = 'Выбери день'
        bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)

    if call.data == "d1":
        msg = '''Раписание на 1 день (04.01.2021)\n
        12:00 - Регистрация 
        13:00 - Открытие 
        14:00 - Обед 
        15:00 - Библейский час 
        16:00 - ДТПС - духовное, творческое, практика, спорт 
        17:00 - Спорт, Свободное время 
        18:00 - Богослужение 
        19:00 - Ужин 
        19:30 - Командное время 
        20:30 - Праздничное открытие 
        22:00 - Снек 
        23:00 - Сказка на ночь 
        23:30 - Отбой'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "d2":
        msg = '''Раписание на 2 день (05.01.2021)\n
        08:45	Зарядка 
        09:00 - Подъем флага 
        09:15 - Личное чтение 
        09:30 - Завтрак 
        10:00 - Утреннее служение 
        11:30 - Библейский час 
        12:30 - Перерыв 
        13:00 - Игра 
        14:00 - Обед 
        15:00 - Командное время 
        16:00 - ДТПС - духовное, творческое, практика, спорт 
        17:00 - Спорт, свободное время 
        18:00 - Богослужение 
        19:00 - Ужин 
        20:45 - Спектакль
        22:00 - Снек 
        23:00 - Сказка на ночь 
        23:30 - Отбой'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "d3":
        msg = '''Раписание на 3 день (06.01.2021)\n
        08:45 - Зарядка 
        09:00 - Подъем флага 
        09:15 - Личное чтение 
        09:30 - Завтрак 
        10:00 - Утреннее служение 
        11:30 - Библейский час 
        12:30 - Перерыв 
        13:00 - Игра 
        14:00 - Обед 
        15:00 - Командное время 
        16:00 - ДТПС - духовное, творческое, практика, спорт  
        17:00 - Спорт, свободное время, репетиция
        18:00 - Богослужение 
        19:00 - Ужин 
        20:00 - Вечер Хвалы 
        22:30 - Рождественский вечер 
        00:00 - Сказка на ночь 
        00:30 - Отбой'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "d4":
        msg = '''Раписание на 4 день (07.01.2021)\n
        09:30 - Личное чтение 
        09:50 - Подъем флага 
        10:00 - Завтрак 
        11:00 - Утреннее служение 
        11:30 - Библейский час 
        12:00 - Закрытие 
        14:00 - Обед 
        15:00 - Отъезд :('''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "verse":
        msg = "Стих на 1 день:\n Ин 3:16 Ин 10:10\nСтих на 2 день:\n Рим 3:23 Рим 6:23\nСтих на 3 день:\n Ин 14:6 Рим 5:8 1 Кор 15:3-6\nСтих на 4 день:\n Откр 3:20 Ин 1:12 Еф 2:8-9"
        #                    Формируем ответ
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()

        key_d1 = types.InlineKeyboardButton(text='День 1', callback_data='vd1')
        keyboard.add(key_d1)

        key_d2 = types.InlineKeyboardButton(text='День 2', callback_data='vd2')
        keyboard.add(key_d2)

        key_d3 = types.InlineKeyboardButton(text='День 3', callback_data='vd3')
        keyboard.add(key_d3)

        key_d4 = types.InlineKeyboardButton(text='День 4', callback_data='vd4')
        keyboard.add(key_d4)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        msg = 'Выбери день'
        bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)

    if call.data == "vd1":
        msg = '''Золотые стихи на 1 день (04.01.2021)\n
        Ибо так возлюбил Бог мир, что отдал Сына Своего Единородного, дабы всякий верующий в Него, не погиб, но имел жизнь вечную.
        (от Иоана 3:16)
         
        Вор приходит только для того, чтобы украсть, убить и погубить. Я пришел для того, чтобы имели жизнь и имели с избытком.
        (от Иоана 10:10)'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "vd2":
        msg = '''Золотые стихи на 2 день (05.01.2021)\n
        Потому что все согрешили и лишены славы Божией
        (Римлянам 10:10)
         
        Ибо возмездие за грех - смерть, а дар Божий - жизнь вечная во Христе Иисусе, Господе нашем
        (Римлянам 6:23)'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "vd3":
        msg = '''Золотые стихи на 3 день (06.01.2021)\n
        Иисус сказал ему: Я есмь путь и истина и жизнь; никто не приходит к Отцу, как только через Меня.
        (от Иоанна 14:6)
         
        Но Бог Свою любовь к нам доказывает тем, что Христос умер за нас, когда мы были еще грешниками.
        (Римлянам 5:8)
         
        Ибо я первоначально преподал вам, что и сам принял, то есть, что Христос умер за грехи наши, по Писанию, и что Он погребен был, и что воскрес в третий день, по Писанию, и что явился Кифе, потом двенадцати; потом явился более нежели пятистам братий в одно время, из которых большая часть доныне в живых, а некоторые и почили
        (1-ое Коринфянам 15:3-6)'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "vd4":
        msg = '''Золотые стихи на 4 день (07.01.2021)\n
        Се, стою у двери и стучу: если кто услышит голос Мой и отворит дверь, войду к нему, и буду вечерять с ним, и он со Мною.
        (Откровение 3:20)
         
        А тем, которые приняли Его, верующим во имя Его, дал власть быть чадами Божиими,
        (от Иоанна 1:12)
         
        Ибо благодатью вы спасены через веру, и сие не от вас, Божий дар: не от дел, чтобы никто не хвалился.
        (Ефесянам 2:8,9)'''
        bot.send_message(call.message.chat.id, msg)
        showMenu()

    if call.data == "menu":
        showMenu()


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)

