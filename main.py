from connection_tg import *


@bot.message_handler(commands=['start'])
def start_message(message):
    mess_text = 'Здарова, Пес!'
    bot.send_message(message.chat.id, mess_text)


# @bot.message_handler(commands=['help'])
# def print_menu(message):
#     message_text = 'Вот, что умеет этот бот:\n' \
#                    '/help - отображает список доступных команд\n\n' \
#                    '❌ изменить тип - Изменит тип на предлагамый.\n\n' \
#                    '✅ сыграть в рулетку [дк] - Возможность поднять ставку 2х.\n\n'
#     bot.send_message(message.chat.id, message_text)


@bot.message_handler(content_types=['text'])
def special_text(message):
    mention = f'[Дядя](tg://user?id={message.from_user.id})'
    bot.send_message(message.chat.id,
                     f'{mention}, шо тобі?',
                     parse_mode="markdown")
    print(message.from_user.id)


if __name__ == '__main__':
    # schedule.every().day.at("01:00").do(function_to_run_every_day)
    # threading.Thread(target=schedule_checker).start()

    bot.polling(none_stop=True)
