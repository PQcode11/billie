import os

import telebot
from telebot import types

import random

import time






bot= telebot.TeleBot('7059307158:AAF1NGXjhBx7kOXFkSd6HAD9XFBk4zGo83A')
# Создаем экземпляр бота




blacklist =['БЛЯ','бля','Бля', 'Сука', 'СУКА', 'ебать', 'ЕБАТЬ','Ебать', 'ебат', 'Ебат', 'хуй', 'Хуй', 'ХУЙ','хуя', 'Хуя', 'пизд', 'Пизд', 'ПИЗД', 'нах', 'Нах', 'НАХ', 'пидор','suk','суk', 'blя', 'eba', 'Blя', 'пидор', 'ПИДОР', 'епат', 'епатт', 'пидорас', 'nah', 'Наh', 'Xуй', 'xyй', 'Хyй','хyй', 'xyй',]




#ПНУТЬ
channel_id='-1002148293923'
textcon = '✅ Ачивка выполнена!               Поздравляю!'
@bot.message_handler(commands=['start'])
def main(message):

    bot.send_message (message.chat.id, 'Вы подписаны! Добавьте меня в любой чат!  ')

# Обработчик события нажатия на кнопку
@bot.callback_query_handler(func=lambda call: True)
def share_callback(call):
    mafia=['mafia', 'doctor', 'none', 'police']

    people=['@AIDS_AI','@cranberry458','@soffdivv','вова','@Alex_280_Valor','@ArisaPtuhova','@The_end_68','@Dariaddd87','@PQYoutube']
    if call.data== 'vibor':
        bot.send_message(call.id,'начнем!')

        bot.promote_chat_member(call.id,call.from_user.id, can_manage_chat=False, can_delete_messages=False, can_manage_video_chats=False, can_restrict_members=False, can_promote_members=False, can_change_info=False, can_invite_users=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False)
        new=bot.send_message(call.id,random.choise(people))

        bot.promote_chat_member(call.id,new, can_manage_chat=True, can_delete_messages=True, can_manage_video_chats=True, can_restrict_members=True, can_promote_members=True, can_change_info=True, can_invite_users=True, can_post_messages=True, can_edit_messages=True, can_pin_messages=True, can_manage_topics=True)
        bot.send_message(call.id,f'Поздравляю,{new}!')
    if call.data== 'dasha':
        bot.send_message(5647670676,f'По ссылке dasha перешёл(а) {call.from_user.first_name}/{call.from_user.username}')







@bot.message_handler(commands=['up'])
def handle_up_command(message):
    if bot.get_chat_member(-1002148293923, message.from_user.id).status != 'left':
    # Получаем имя пользователя



    # Присваиваем переменной x значение username
        repler_id = message.reply_to_message.from_user.username



        global x
        x = repler_id



    # Отправляем сообщение с подтверждением
        bot.send_message(message.chat.id, f"Пользователь @{x} повышен до X.",reply_to_message_id=message.message_id)



@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    mafia=['mafia','police', 'none', 'doctor']

    if message.text == 'выборы!!!':
        bot.send_message(message.chat.id, 'Главный админ,нажми', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Только Гл.Админ',callback_data='vibor')]]))



    elif message.text == '/newgame':
        global msg
        msg=bot.send_message(message.chat.id, 'Начнем игру! Выберите свободное место! По окончании выбора всех игроков нажмите "Начать"', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='1', callback_data='1'),telebot.types.InlineKeyboardButton(text='2',callback_data='2'),telebot.types.InlineKeyboardButton(text='3',callback_data='3'),telebot.types.InlineKeyboardButton(text='Начать',callback_data='go')]]))

        bot.send_message(message.from_user.id, random.choice(mafia))












    if message.from_user.username !="Nio":


        if message.text == '/inf':
            if message.reply_to_message:
                if bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'creator':
                    global stat
                    stat = 'Создатель чата'
                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'administrator':

                    stat = 'Админ'
                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'member':

                    stat = 'Участник'
                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'left':

                    stat = 'Покинул группу'

                elif bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status == 'banned':

                    stat = 'Забанен'
                bot.send_message (message.chat.id, f'Имя: {message.reply_to_message.from_user.first_name}                     Фамилия: {message.reply_to_message.from_user.last_name}                      Username: @{message.reply_to_message.from_user.username}                      ID: {message.reply_to_message.from_user.id}                             Это бот:{message.reply_to_message.from_user.is_bot}                             Премиум: {message.reply_to_message.from_user.is_premium}                         Язык: {message.reply_to_message.from_user.language_code}                      Чат : {message.reply_to_message.chat.title}                               Статус: {stat} ')
            else:
                bot.send_message (message.chat.id, 'Чтобы использовать команду, ответьте на сообщение пользователя')









        elif message.text in ['пнуть',"Пнуть"]:
            if message.reply_to_message:
                global pnut
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username
                pnut+=1
                bot.send_message(recipient_id, f'@{sender_id} пнул(а) @{repler_id}! ', reply_to_message_id=message.message_id)
                if pnut == 20:
                    bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/94', caption= f'{textcon}')




        #ПОЦЕЛОВАТЬ
            bot.delete_message(message.chat.id,message.message_id)
        elif message.text in ['поцеловать',"Поцеловать"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} поцеловал(а) @{repler_id}!', reply_to_message_id=message.message_id)
        #УБИТЬ
            bot.delete_message(message.chat.id,message.message_id)

        elif message.text in ['убить',"Убить"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(message.chat.id, f'@{sender_id} убил(а) @{repler_id}!', reply_to_message_id=message.message_id)

        elif message.text in ['+Отн',"+отн"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username
                repl = message.reply_to_message.from_user.id
                bot.send_message (repl, f'{sender_id} предложил вам отношения. Вы согласны?',reply_to_message_id=message.message_id)
                if message.text in ['Да', 'да','ДА']:
                    if message.from_user.username == repler_id:
                        bot.send_message (message.chat.id,f'+Отношения: {repler_id} и {sender_id}')
        elif message.text in ['Иди на',"иди на"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} послал(а) @{repler_id}!', reply_to_message_id=message.message_id)

        elif message.text in ['удачи',"Удачи"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} пожелал(а) удачи 🤞 @{repler_id}!', reply_to_message_id=message.message_id)
        #РАССТРЕЛЯТЬ
            bot.delete_message(message.chat.id,message.message_id)
        elif message.text in ['расстрелять',"Расстрелять"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username

                bot.send_message(recipient_id, f'@{sender_id} расстрелял(а) @{repler_id}!', reply_to_message_id=message.message_id)
            bot.delete_message(message.chat.id,message.message_id)
        #ОБНЯТЬ
        elif message.text in ['обнять',"Обнять"]:
            if message.reply_to_message:
                sender_id = message.from_user.username
                recipient_id = message.chat.id
                repler_id = message.reply_to_message.from_user.username
                bot.send_message(recipient_id, f'@{sender_id} обнял(а) @{repler_id}!', reply_to_message_id=message.message_id)

            bot.delete_message(message.chat.id,message.message_id)
        #УДАЛЯЕМ СОО


        elif message.text == '/del':
            if message.reply_to_message:

                if message.from_user.id== 5647670676:
                    last_message_id = message.reply_to_message.message_id
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.delete_message(message.chat.id, last_message_id)
            #ДУЭЛЬ
        elif message.text in ['дуэль','Дуэль']:
            duel1_id = message.from_user.username
            duel2_id = message.reply_to_message.from_user.username
            recipient_id = message.chat.id
            bot.send_message(recipient_id, f'@{duel1_id} вызвал(а) на дуэль @{duel2_id}!', reply_to_message_id=message.message_id)
        elif message.text== '/com':
            bot.send_message(message.chat.id, 'Все команды бота:             @khronosbottg')
        #ачивки

        elif message. text in ['крестный отец', 'Крестный отец', 'Крестный Отец']:
             bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/93', caption= f'{textcon}')
             bot.send_message(6752233707,f'Ачивка крестный отец выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['я твой отец', 'Я твой Отец', 'Я твой отец', 'Я Твой Отец']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/92',caption=textcon)
            bot.send_message(6752233707,f'Ачивка звёздные войны выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['люблю Россию', 'Люблю Россию', 'Россия ❤','Я патриот', 'Я-патриот', 'Я Патриот', 'Россия>','Я люблю Россию', 'Я Люблю Россию', 'я люблю Россию']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/91', caption=textcon)
            bot.send_message(6752233707,f'Ачивка патриот выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['kurwa bobr ','kurva bobr','курва бобр','Курва бобр', 'Пердоле', ' я пердоле', 'Я пердоле']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/104', caption=textcon)
            bot.send_message(6752233707,f'Ачивка курвабобр выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

    #БЛЭКЛИС
        global d

        for x in blacklist:

            if (x in message.text):




                d+=1

                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id,f'тссс не матерись, {message.from_user.first_name},             Счетчик: {d}')



d=0
pnut=0
m=10











# Запускаем бота

bot.polling(none_stop=True, interval=0)

