import aminofix, datetime, concurrent.futures, pyfiglet
from threading import Thread
from colored import fore, back, style, attr
attr(0)
print(fore.BLUE + style.BOLD)

"""
-----------------
Made by Xsarz
GitHub - https://github.com/xXxCLOTIxXx
Telegram - t.me/DXsarz
-----------------

"""
name = 'AminoSpamer V5.3'
client = aminofix.Client()

def spam_func(sub_client, chatId, message, mess_type):
    try:
        dt_now = datetime.datetime.now()
        while True:
            print(f"[{dt_now}]---[{name}]: Поток спама запущен.")
            with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
                _ = [

                    executor.submit(
                        sub_client.send_message,
                        chatId,
                        message,
                        mess_type) for _ in range(100000)]
    except Exception as ex:
        print(f"[{name}]: Произошла ошибка!\n\n{ex}")



print(pyfiglet.figlet_format(name, font="slant"))
print('\nMade by Xsarz ========= t.me/DXsarz')
print('\n\n--------------------------------')
print('1 - Через почту и пароль')
print('2 - через сид')
print('3 - через номер телефона')
print('По умолчанию стоит способ через почту')
print('--------------------------------')
log = input(f"[{name}]: Каким способом хотите войти?>> ")

if log == '2':
    while True:
        sid = input(f"[{name}]: SID аккаунта>> ")
        try:
            client.login_sid(SID=sid)
            break
        except Exception as ex:
            print(f"\n\n\n[{name}]: Не удалось войти в аккаунт\n{ex}\n\n\n")
elif log == '3':
    while True:
        number = input(f"[{name}]: Номер телефона>> ")
        password = input(f"[{name}]: Пароль >> ")
        try:
            client.login_phone(phoneNumber=number, password=password)
            break
        except Exception as ex:
            print(f"\n\n\n[{name}]: Не удалось войти в аккаунт\n{ex}\n\n\n")
else:
    while True:
        email = input(f"[{name}]: Почта >> ")
        password = input(f"[{name}]: Пароль >> ")
        try:
            client.login(email=email, password=password)
            break
        except Exception as ex:
            print(f"\n\n\n[{name}]: Не удалось войти в аккаунт\n{ex}\n\n\n")



while True:
    try:
        chat = client.get_from_code(input(f"[{name}]: Чат для атаки>>")).json
        chatId = chat['extensions']['linkInfo']['objectId']
        comId = chat['extensions']['linkInfo']['ndcId']
        sub_client = aminofix.SubClient(comId=comId,profile=client.profile)
        print(f"\n\n[{name}]: Данные успешно получены!\n\n")
        break
    except:
        print(f"\n\n[{name}]: Произошла ошибка!\n\n")

message = input("Сообщение >> ")
__ = input(f"[{name}]: Тип Сообщения (0, 109)>>")
if __ == '0':
	mess_type = 0
	print(f'\n[{name}]: Тип сообщения 0 (Обычный)\n\n')
elif __ == '109':
	mess_type = 109
	print(f'\n[{name}]: Тип сообщения 109 (Системный)\n\n')
else:
	mess_type = 0
	print(f'\n[{name}]: Тип сообщения 0 (Обычный)\n\n') 

try:
    client.join_community(comId=comId)
    join_com_ = 'OK.'
except:
    join_com_ = f'ERROR.'

try:
    client.join_chat(chatId=chatId)
    join_chat_ = 'OK.'
except:
    join_chat_ = f'ERROR.'

print(f"[Вход в сообщество]: {join_com_}")
print(f"[Вход в чат]: {join_chat_}")


def start_():
    Thread(target=spam_func, args=(sub_client, chatId, message, mess_type)).start()
    Thread(target=spam_func, args=(sub_client, chatId, message, mess_type)).start()
    Thread(target=spam_func, args=(sub_client, chatId, message, mess_type)).start()
    Thread(target=spam_func, args=(sub_client, chatId, message, mess_type)).start()
    print(f'[{name}]: Для завершения рейда закройте консоль.')
start_()