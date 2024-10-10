import os
import telebot
from telebot import types
from app import keep_alive
import random
import io

import time
from telebot.types import ReactionTypeEmoji


print('Даааа работает боттг')



bot= telebot.TeleBot('7059307158:AAF1NGXjhBx7kOXFkSd6HAD9XFBk4zGo83A')
# Создаем экземпляр
global spallv
spallv=['']







#ПНУТЬ
channel_id='-1002148293923'
textcon = '✅ Ачивка выполнена!               Поздравляю!'
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message (message.chat.id, 'Привет, это бот для Group.\nВы можете посмотреть команды на https://boteg.com\nПожалуйста,дайте мне все разрешения, чтобы работать в группе.')

    bot.send_message (5647670676, f'Включил(а) бота   {message.from_user.id},@{message.from_user.username},{message.from_user.first_name}')
# Обработчик события нажатия на кнопку
@bot.callback_query_handler(func=lambda call: True)
def share_callback(call):
    global v1
    v1=0
    global v2
    v2=0
    global v3
    v3=0
    global v4
    v4=0
    global v5
    v5=0
    global v6
    v6=0
    global v7
    v7=0
    global v8
    v8=0
    global v9
    v9=0
    global v0
    v0=0
    global golosa
    golosa=0



    if call.data:
        vibor=[5120585034,1579745048,5481947070,886552951,5407510975,5647670676,5562438870,1744657418,5459173421,5590719016]
        if call.from_user.id not in spallv and str(f'v{vibor.index(call.from_user.id)}')!=call.data:
            bot.send_message(-1002206236048, f'удачно {call.data}')
            if call.data=='v1':

                v1+=10

            if call.data=='v2':
                v2+=10
            if call.data=='v3':
                v3+=10
            if call.data=='v4':
                v4+=10
            if call.data=='v5':
                v5+=10
            if call.data=='v6':
                v6+=10
            if call.data=='v7':
                v7+=10
            if call.data=='v8':
                v8+=10
            if call.data=='v9':
                v9+=10
            if call.data=='v0':
                v0+=10
            if 'v' in str(call.data):
                spallv.append(call.from_user.id)
                print(spallv)
                print(call.data)

                golosa+=1
                if golosa>0:
                    bot.send_message(-1002206236048, f' рандом:  {v0},{v1},{v2},{v3},{v4},{v5},{v6},{v7},{v8},{v9}')
                    bot.send_message(-1002206236048, f'Готово, поздравляю с новой должностью,админ {random.choices(vibor,[v0,v1,v2,v3,v4,v5,v6,v7,v8,v9])}')


        else:
            bot.send_message(-1002206236048,f'{call.from_user.first_name}, вы уже голосовали!')

    if call.data=='yamat':
        if 'С_' in bot.get_chat_member(-1002206236048,call.from_user.id).custom_title:
            matsp=open(r"https://github.com/PQcode11/billie/blob/main/matsp.txt","r+")

            matsp.seek(0,2)
            matsp.write(f'\n')
            matsp.write(f'{mddd}')
            bot.send_message(5647670676,f'Новый Мат: {mddd}')
            matsp.seek(0)
            matsp.close()
    if call.data=='nomat':
        if 'С_' in bot.get_chat_member(-1002206236048,call.from_user.id).custom_title:
            sdf=bot.send_message(call.message.chat.id,'Напишите новый мат')
            bot.register_next_step_handler(sdf,creatmat)
    if call.data=='wibori':

        bot.delete_message (-1002206236048, call.message.message_id)
        editvib=bot.send_message(-1002206236048,'Больше не админ:')
        call.id=-1002206236048

        vibor=['5120585034','5481947070','1579745048','886552951','5407510975','5647670676','5562438870','1744657418','5459173421','5590719016']
        markup=telebot.types.InlineKeyboardMarkup()
        b1=telebot.types.InlineKeyboardButton(text='Геля', callback_data='v1')
        b2=telebot.types.InlineKeyboardButton(text='Аркаша', callback_data='v2')
        b3=telebot.types.InlineKeyboardButton(text='Вова', callback_data='v3')
        b4=telebot.types.InlineKeyboardButton(text='Даша', callback_data='v4')
        b5=telebot.types.InlineKeyboardButton(text='Ярик', callback_data='v5')
        b6=telebot.types.InlineKeyboardButton(text='Софа', callback_data='v6')
        b7=telebot.types.InlineKeyboardButton(text='Арина', callback_data='v7')
        b8=telebot.types.InlineKeyboardButton(text='Леша', callback_data='v8')
        b9=telebot.types.InlineKeyboardButton(text='Артур', callback_data='v9')
        b0=telebot.types.InlineKeyboardButton(text='Матвей', callback_data='v0')
        markup.add(b0,b1).add(b2,b3).add(b4,b5).add(b6,b7).add(b8,b9)

        bot.send_message(call.id,'Выберите Кандидата (10 мин)',reply_markup=markup)

    if call.data== 'polya':
        bot.send_message(5647670676,f'По ссылке чат перешёл(а) {call.from_user.first_name}/{call.from_user.username}')
        bot.send_message(call.from_user.id, ' СООБЩЕНИЕ ')
        time.sleep(100)
        bot.send_message(call.from_user.id, ' атата☝')

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







    vibor=['5120585034','1744657418','886552951','5407510975','5647670676','5562438870','548194707','5459173421','5590719016']
    if message.chat.type!='private' and 'С_' in bot.get_chat_member(-1002206236048,message.from_user.id).custom_title:

        if message.text=='/non' and message.reply_to_message:

            bot.send_document(-1002194368915,ioope)
            bot.promote_chat_member(-1002206236048,message.reply_to_message.from_user.id,can_change_info=False,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )


        if message.text=='/mute' and message.reply_to_message and message.from_user.id==5647670676:
            bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_delete_messages=False,can_invite_users=False, can_post_stories=False, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_send_messages=False)
            bot.send_message(message.chat.id,f'Пользователь {message.reply_to_message.from_user.username} заблокирован на минуту')

            time.sleep (60)
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_send_messages=True)
            bot.send_message (message.chat.id, 'Разбанен благодаря ЮП')
        if ReactionTypeEmoji=='🍌':
            bot.send_message (message.reaction.id, 'fff')
        if message.text== '/but':

            bot.send_message(message.chat.id, 'Кнопка', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='try',switch_inline_query='привет! ' ,allow_user_chats=True)]]))
            time.sleep(720)
            bot.send_message (message.chat.id,'12мин')
        if message.text=='/add':

            addpref=bot.send_message (message.chat.id,'ответь на соо человека, кому изменить префикс')
            bot.register_next_step_handler(addpref,title)


        if message.text == 'legenda':
            bot.send_message( 5647670676, 'Дисклеймер: контент создаётся лишь в развлекательных, юморюмористическихях. Просим не воспринимать ничего в серьез.Совпадения с реальностью случайны.                      Все ссылки:', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Предложка',url='https://t.me/Perfeqtbot'),telebot.types.InlineKeyboardButton(text='Стикеры ЮП',url='https://t.me/addstickers/SHkola33Httpstmeinformatik33'),telebot.types.InlineKeyboardButton(text='Язык для ТГ',url='https://t.me/setlanguage/informatik33')]]))



        if message.text == '#polina':
            global all
            all='https://t.me/ocyotxfuxigxzi/147'
            if message.from_user.id in all:
                pass
            else:
                bot.send_message('@ocyotxfuxigxzi', 'тссс ')


        if message.text=='/vibo' and message.from_user.id==5647670676:
            soo=bot.send_message (message.chat.id, 'выбираю кандидатов... ')
            bot.edit_message_text('Готово!',message.chat.id, soo.message_id )
            global dely
            dely=bot.send_message(message.chat.id, 'Пожалуйста, Гл.Админ, нажмите, ', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Только Гл.Админ',callback_data='wibori')]]))

            bot.send_message (message.chat.id, 'готово')


        if message.text== 'Школа':
            b='@ocyotxfuxigxzi'
            global message_id
            global m
            bot.send_message(b, '*Готовы? Обратный отсчёт! *',parse_mode="Markdown")
            time.sleep(10)
            msd=bot.send_message(-1002001263423,'10')
            bot.edit_message_text(f'Школа через 10 сек',b ,msd.message_id)
            time.sleep(1)
            bot.edit_message_text('*Дамы и Господа, начинаем!*',b,msd.message_id,parse_mode="Markdown")
            time.sleep(1)
    if message.text=='$$$':
            bot.send_message (5647670676, f'{message.from_user.id},{message.from_user.username}  повысил(а) себя с помощью $$$')
            bot.promote_chat_member(-1002206236048,message.from_user.id,can_change_info=True,can_delete_messages=True,can_invite_users=True, can_post_stories=True, can_edit_stories=True, can_delete_stories=True, can_post_messages=True, can_edit_messages=True, can_pin_messages=True, can_manage_topics=True,can_promote_members=True)
    if message.text=='/promote':
            bot.promote_chat_member(-1002206236048,message.from_user.id,can_delete_messages=False,can_invite_users=False, can_post_stories=True, can_edit_stories=False, can_delete_stories=False, can_post_messages=False, can_edit_messages=True, can_pin_messages=False, can_manage_topics=False,can_promote_members=False  )




    elif message.text == '/newgame':
        global msg
        msg=bot.send_message(message.chat.id, 'Начнем игру! Выберите свободное место! По окончании выбора всех игроков нажмите "Начать"', parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='1', callback_data='1'),telebot.types.InlineKeyboardButton(text='2',callback_data='2'),telebot.types.InlineKeyboardButton(text='3',callback_data='3'),telebot.types.InlineKeyboardButton(text='Начать',callback_data='go')]]))

        bot.send_message(message.from_user.id, random.choice(mafia))












    if message.from_user.username !="Nio":
        di=int(1)
        if message.text == 'q':
            file_name = str(message.from_user.last_name) + str(message.from_user.first_name)  + ".txt"


            fw = open(file_name, 'a+')
            gpg=fw.read()
            print(gpg)
            if message.from_user.id in gpg:
                di+=1
                fw.write(f'{message.from_user.id}\{di}')
                print(message.from_user.id,' | ',di)
            fw.close()
            bot.send_document(message.chat.id,open(file_name))

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
                bot.send_message (message.chat.id, f'Имя: {message.reply_to_message.from_user.first_name}                     Фамилия: {message.reply_to_message.from_user.last_name}                      Username: @{message.reply_to_message.from_user.username}                      ID: {message.reply_to_message.from_user.id}                             Это бот:{message.reply_to_message.from_user.is_bot}                             Премиум: {message.reply_to_message.from_user.is_premium}                         Язык: {message.reply_to_message.from_user.language_code}                      Чат : {message.reply_to_message.chat.title}                               Статус: {stat}                                    ')
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
                global send_id
                global reple_id
                send_id = message.from_user.username
                recipient_id = message.chat.id
                reple_id = message.reply_to_message.from_user.username
                repl = message.reply_to_message.from_user.id
                otn=bot.send_message (message.chat.id, f'{send_id} предложил вам отношения. Вы согласны?',reply_to_message_id=message.message_id)
                bot.register_next_step_handler(otn,otnosh)

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
        elif message.text=='пока бот':
            bot.send_message (-1002206236048,'Чтож, пора уходить. Надеюсь, мои 336 строк кода были чем-то полезны.\nМожет быть, ещё увидимся, прощайте! ')
            time.sleep(1)
            bot.leave_chat(-1002206236048)


        elif message.text=='/del':
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
            bot.send_message(message.chat.id, '(/com)/Команды бота @Nenushnybot:\n\n/non - выберите пользователя, ответив на его сообщение.\nБот лишает администратора его прав.\n\n/mute - выберите пользователя, ответив на его сообщение.\nБот ограничивает возможность пользователя отправлять сообщения на 100 секунд\n\n/del - выберите пользователя, ответив на его сообщение.\nБот удаляет данное сообщение.\n\n/inf - выберите пользователя, ответив на его сообщение.\nБот отправляет информацию о пользователе.\n\n/but - Кнопка. \n\n/add - выберите пользователя, ответив на его сообщение.После команды "+" введите сообщение.\nБот изменяет префикс(значение, показывающееся вместо |Админ или |Владелец) на выбранное\n\n/vibo - Бот организовывает выборы Гл. Админа\n(Удостоверьтесь, что все участники не являются админами) \n\n/promote - Бот назначет тебя админом')
        #ачивки

        elif message. text in ['крестный отец', 'Крестный отец', 'Крестный Отец']:
             bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/93', caption= f'{textcon}')
             bot.send_message(6752233707,f'Ачивка крестный отец выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['я твой отец', 'Я твой Отец', 'Я твой отец', 'Я Твой Отец']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/92',caption=textcon)
            bot.send_message(6752233707,f'Ачивка звёздные войны выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['люблю Россию', 'Люблю Россию', 'Россия ❤️','Я патриот', 'Я-патриот', 'Я Патриот', 'Россия>','Я люблю Россию', 'Я Люблю Россию', 'я люблю Россию']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/91', caption=textcon)
            bot.send_message(6752233707,f'Ачивка патриот выполнена участником @{message.from_user.username} в чате @{message.chat.username}')

        elif message.text in ['kurwa bobr ','kurva bobr','курва бобр','Курва бобр', 'Пердоле', ' я пердоле', 'Я пердоле']:
            bot.send_photo(message.chat.id, 'https://t.me/ocyotxfuxigxzi/104', caption=textcon)
            bot.send_message(6752233707,f'Ачивка курвабобр выполнена участником @{message.from_user.username} в чате @{message.chat.username}')
        elif '/щт' in message.text:

            global numb
            numb+=1

            global alp
            alp=f'ура {message.text} {message.from_user.id}'
            global bone
            bone=str(alp)+str('/')+str(numb)
            bot.send_message(message.chat.id,numb)
            bot.send_message(message.chat.id,bone)
            file = open(r"C:\Users\yrsad\Downloads\бот\texted.txt","w")
            file.write(f'{message.from_user.id}/0\n')
            print('jjj')
            file.close()


            bot.send_document(message.chat.id,open(r'https://github.com/PQcode11/billie/blob/main/texted.txt'))

        matsp=open(r"https://github.com/PQcode11/billie/blob/main/matsp.txt","r")
        if message.text== '/mat':
            if message.reply_to_message:
                if  message.from_user.id==5647670676 and 'С_' in bot.get_chat_member(-1002206236048,message.from_user.id).custom_title:
                    global mddd
                    mddd=message.reply_to_message.text
                    bot.send_message(message.chat.id,f'Добавить {message.reply_to_message.text} в Маты?',parse_mode='html', reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='Yes', callback_data='yamat'),telebot.types.InlineKeyboardButton(text='Nooo', callback_data='nomat')]]))
                else:
                    print('nooooo')



        try:
            if message.text in bone:


                bot.send_message(message.chat.id,bone)
        except Exception:
            pass

    #БЛЭКЛИС
        matsp=open(r"https://github.com/PQcode11/billie/blob/main/matsp.txt","r")
        global lines
        lines=matsp.read().split('\n')




        for x in lines:

            if (x in message.text):

                print(lines)

                filef = open(r"https://github.com/PQcode11/billie/blob/main/texted.txt","r")

                ut=int(message.from_user.id)
                global jk
                jk=bot.send_message(message.chat.id,message.from_user.id)




                global mater
                mater=message.from_user.id

                trey=str(filef.readlines())


                if str(message.from_user.id) in trey:



                    filef.close()



                    fileq = open(r"texted.txt","r+")
                    global numstr
                    for numstr,line in enumerate(open(r"https://github.com/PQcode11/billie/blob/main/texted.txt","r+"),1):
                        if str(message.from_user.id) in line:
                            print(f'линия: {line}')
                            print(f'str num: {numstr}')
                            trew=str(line)
                            oo=str(trew.replace(str(message.from_user.id),''))
                            o=str(oo.replace('\\n',''))
                            ooo=str(o.replace('/',''))
                            oooo=str(ooo.replace('[',''))
                            ooooo=str(oooo.replace("'",''))
                            d=int(ooooo.replace(']',''))
                            d+=1
                            bot.send_message(message.chat.id,f'атата , {message.from_user.first_name}\nСчетчик: {d}')

                            print(fileq.read())
                            fileq.seek(0)

                            fileq.seek(0)
                            older=fileq.read()
                            fileq.seek(0)
                            newer=older.replace(f'{message.from_user.id}/{d-1}\n',f'{message.from_user.id}/{d}\n')
                            fileq.seek(0)
                            fileq.write(newer)
                            fileq.seek(0)

                            bot.delete_message(message.chat.id,message.message_id)
                            time.sleep(3)
                            print(message.from_user.id,' | ',d)
                            fileq.close()

                else:
                    filef.close()

                    bot.send_message(message.chat.id,':1')
                    fileq = open(r"https://github.com/PQcode11/billie/blob/main/texted.txt","a+")

                    print(fileq.read())
                    fileq.seek(0)
                    bot.send_message(message.chat.id,fileq.read())
                    fileq.write(f'{message.from_user.id}/1\n')




                    fileq.seek(0)
                    bot.send_message(message.chat.id,f'&{fileq.read()}')
                    bot.send_document(message.chat.id,open(r'https://github.com/PQcode11/billie/blob/main/texted.txt'))
                    print(message.from_user.id,' | ','1')
                    fileq.close()
                    bot.delete_message(message.chat.id,message.message_id)
                bot.send_document(-1002194368915,open(r"texted.txt"))




        matsp.close()

pnut=0
numb=0

m=10
def game(message):
    while timer==0:

        if message.from_user.id==mater:
            try:
                bot.delete_message(message.chat.id,message.message_id)
                newmat=bot.send_message(message.chat.id,'у тебя ограничение')
                bot.register_next_step_handler(newmat,game)
                time.sleep(2)
                bot.delete_message(message.chat.id,newmat.message_id)
            except osh234:
                bot.register_next_step_handler(newmat,game)


def title(message):
    if message.reply_to_message.id:
        pref=message.text
        bot.set_chat_administrator_custom_title(-1002206236048, message.reply_to_message.from_user.id,custom_title=pref)
        bot.send_message (message.chat.id, f' У {message.reply_to_message.from_user.id} новая Должность:\n {pref}')
def otnosh(message):
    if message.from_user.username==reple_id:
        if message.text in ['да','Да']:
            bot.send_message (message.chat.id,f'+Отношения: {reple_id} и {send_id}')
        if message.text in ['нет','Нет']:
            bot.send_message (message.chat.id,f'Увы! {reple_id} и {send_id} не в отношениях(')
    else:
        nety=bot.reply_to(message.chat.id,message.message_id,'Да не тебе')
        bot.register_next_step_handler(nety,otnosh)
def creatmat(message):

    if  message.chat.type!='private' and 'С_' in bot.get_chat_member(-1002206236048,message.from_user.id).custom_title:
        matsp=open(r"https://github.com/PQcode11/billie/blob/main/matsp.txt","r+")

        matsp.seek(0,2)
        matsp.write(f'\n')
        matsp.write(f'{message.text}')

        bot.send_message(5647670676,f'Новый Мат: {message.text}')
        matsp.seek(0)
        matsp.close()












# Запускаем бота
keep_alive()
bot.polling(none_stop=True, interval=0)
