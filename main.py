import telebot
from telebot import types
import webbrowser
import sqlite3

photo_url = 'https://ibb.co/RjJ0n4V'
photo_url7 = 'https://ibb.co/mX8H3sx'
photo_url2 = 'https://img.freepik.com/free-vector/social-subscription-button-add-more-follower-to-your-web-app_1017-43314.jpg?size=626&ext=jpg&ga=GA1.1.1292351815.1709856000&semt=ais'
photo_url3 = 'https://ibb.co/M9zSK4Y'
photo_url5 = 'https://ibb.co/Ssz8nT1'
photo_url6 = 'https://ibb.co/VSPCZ5V'
photo_url8 = 'https://www.meme-arsenal.com/memes/d5480c4e7d61b84d55c1608182276287.jpg'
photo_url9 = 'https://n1s1.hsmedia.ru/6c/d1/0d/6cd10d502b4bf7ce262819729b66c8ff/3009x2000_0xCSHwB5NS_3143067006704213654.jpg'
photo_url10 = 'https://media.istockphoto.com/id/92482130/ru/%D1%84%D0%BE%D1%82%D0%BE/%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA-%D0%B8%D0%B4%D0%B5%D1%82-%D0%BD%D0%B0-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%B5%D0%BB%D0%BA%D0%B0.jpg?s=612x612&w=0&k=20&c=F929VK62kPdO9V_lTRnHwDctmzk0w14WAran-PlPNz8='
photo_url11 = 'https://ibb.co/cYm87yM'
photo_url12 = 'https://ibb.co/yndRpJ4'
photo_url13 = 'https://ibb.co/MPYBMQm'
photo_url14 = 'https://ibb.co/0JGXCms'
bot = telebot.TeleBot('6800016376:AAH-Xw7xOC-2zTFUHrobxKF3HhIA7y3X1_Q')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет! Извини не буду смотреть")
    markup.add(btn1)
    bot.send_message(message.from_user.id, f"👋 привет, Че смотришь {message.from_user.first_name}!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Привет! Извини не буду смотреть':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Истаграмм Ани')
        btn2 = types.KeyboardButton('Истаграмм Бори')
        btn3 = types.KeyboardButton('Кто это?')
        markup.add(btn1, btn2, btn3, )
        bot.send_photo(message.from_user.id, photo=photo_url8, caption='Быстро подписался на Инстаграмм!!!', reply_markup=markup) #ответ бота

    elif message.text == 'Инстаграмм Ани':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Инстаграмм Ани', url='https://www.instagram.com/anizssz/')
        markup.add(btn1)
        bot.send_photo(message.from_user.id, photo=photo_url7, caption='Вам нужно перейти по ссылке ниже, после вам нужно нажать на кнопку подписаться.', reply_markup=markup)

    elif message.text == 'Инстаграмм Бори':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='instagramm' , url='https://www.instagram.com/theonlyboriska/')
        markup.add(btn1)
        bot.send_photo(message.from_user.id, photo=photo_url, caption='Вам нужно перейти по ссылке ниже, после вам нужно нажать на кнопку подписаться.', reply_markup=markup)

    elif message.text == 'Кто это?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('Да')
        btn5 = types.KeyboardButton('Нет')
        btn6 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn4, btn5,btn6)
        bot.send_photo(message.from_user.id, photo=photo_url3, caption="Тебя это волнует?", reply_markup=markup)

    elif message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7 = types.KeyboardButton('Кто такой Борис?')
        btn8 = types.KeyboardButton('Кто такая Аня?')
        btn9 = types.KeyboardButton('Их знакомство')
        btn10 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn7,btn8,btn9,btn10)
        bot.send_photo(message.from_user.id, photo=photo_url9, caption='Ну тогда выбирай', reply_markup=markup)

    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7 = types.KeyboardButton('Кто такой Борис?')
        btn8 = types.KeyboardButton('Кто такая Аня?')
        btn9 = types.KeyboardButton('Их знакомство')
        btn10 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn7, btn8, btn9, btn10)
        bot.send_photo(message.from_user.id, photo=photo_url10, caption='Мне все равно выбирай', reply_markup=markup)

    elif message.text == 'Их знакомство':
        bot.send_photo(message.from_user.id, photo=photo_url11, caption='')

    elif message.text == 'Кто такой Борис?':
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton('Хобби', callback_data='del6')
        btn2 = types.InlineKeyboardButton('Учеба', callback_data='del7')
        btn3 = types.InlineKeyboardButton('Работа', callback_data='del8')
        markup.add(btn1, btn2, btn3)
        btn4 = types.InlineKeyboardButton('Место проживания', callback_data='del9')
        btn5 = types.InlineKeyboardButton('Другое', callback_data='del10')

        markup.add(btn4, btn5, )
        bot.send_photo(message.from_user.id, photo=photo_url5, caption='Вот как выглядит эта скатина', reply_markup=markup)

    elif message.text == 'Кто такая Аня?':
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton('Хобби', callback_data='del1')
        btn2 = types.InlineKeyboardButton('Учеба', callback_data='del2')
        btn3 = types.InlineKeyboardButton('Работа', callback_data='del3')
        markup.add(btn1, btn2, btn3)
        btn4 = types.InlineKeyboardButton('Место проживания', callback_data='del4')
        btn5 = types.InlineKeyboardButton('Другое', callback_data='del5')

        markup.add(btn4, btn5,)
        bot.send_photo(message.from_user.id, photo=photo_url6, caption='', reply_markup=markup)

    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Инстаграмм Ани')
        button2 = types.KeyboardButton('Инстаграмм Бори')
        button3 = types.KeyboardButton('Кто это?')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'del6':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Удалить сообщение', callback_data='delete')
        markup.add(btn1)
        bot.send_message(callback.message.chat.id, 'Xобби — играть в компьютерные игры. Как взрослые, так и дети любят это теперь. Это стало одним из наиболее популярных хобби в настоящее время. Я думаю, что компьютерная игра очень интересна. Это не только «тратить время», как некоторые люди говорят.\n  Так же занимаюсь Танцами, в возрасте 14 лет мама отправила на лезгинку как бы я не хотел', reply_markup=markup)

    elif callback.data == 'del1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Удалить сообщение', callback_data='delete')
        markup.add(btn1)
        bot.send_photo(callback.message.chat.id, photo=photo_url14, caption='Хобби – Лезгинка это не только хобби, но и страсть, которая наполняет жизнь энергией и радостью. Этот танец стал неотъемлемой частью самовыражения и способом выразить себя через движение и ритм.', reply_markup=markup)

    elif callback.data == 'del2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Удалить сообщение', callback_data='delete')
        markup.add(btn1)
        bot.send_message(callback.message.chat.id,'Учеба — С 1 по 9 класс училась в Средне общеобразовательной школе им.В.Ленина. После окончания школы поступилай в Профессиональный лицей №37. Профессия повар. ', reply_markup=markup)

    elif callback.data == 'del3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Удалить сообщение', callback_data='delete')
        markup.add(btn1)
        bot.send_photo(callback.message.chat.id, photo=photo_url12, caption='Работа — Топ Модель!😲 😳 в студии Up_models.kg помимо модельного агенста, капеечка падает с танцев😎.', reply_markup=markup)

    elif callback.data == 'del4':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Удалить сообщение', callback_data='delete')
        markup.add(btn1)
        bot.send_message(callback.message.chat.id, 'Место проживания — Родилась 1 Июля 2007 году в городе Бишкек. Проживает в Ленинском районе. ', reply_markup=markup)


    elif callback.data == 'del5':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Удалить сообщение', callback_data='delete')
        markup.add(btn1)
        bot.send_photo(callback.message.chat.id, photo=photo_url13, caption='А че еще рассказать. \nЕе улыбка — это чудо, которое делает мир лучшим. \nЕе волосы пахнут счастьем. \nЕе внешность сравнима с ангелом. \nЕе глаза — два редких алмаза. \n   Надеюсь, тебе так же хорошо со мной, как мне всегда хорошо с тобой Анечка, люблю тебя 😘❤  ', reply_markup=markup)

    elif callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
bot.polling(none_stop=True, interval=0)