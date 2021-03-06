import telebot
from telebot import types
import products_list
# import emoji
token = '1995044732:AAGCGjIXXm5h7hM6deRmNgTSEpE0oCoyxLs'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=4)
    item = types.InlineKeyboardButton('Продукция', callback_data='products')
    item2 = types.InlineKeyboardButton('Мероприятия', callback_data='events')
    item3 = types.InlineKeyboardButton('Контакты', callback_data='contacts')
    markup.add(item, item2, item3)

    bot.send_message(message.chat.id, 'Добрый день и хорошего настроения! Выберите, что Вам необходимо',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'products':
            to_print = products_list.to_print
            text_to_send = products_list.to_string(to_print[1])
            text_to_send = str(text_to_send)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id, text=text_to_send)
        elif call.data == 'events':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id, text='Супер семинар по массажу')
        elif call.data == 'contacts':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id, text='г. Минск,ул. Мележа, д.5, корп.2, оф. 213')


# сортировка по возрастани. list sort()

bot.polling()
