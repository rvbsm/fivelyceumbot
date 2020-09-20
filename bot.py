from config import *
from messages import *
from func import *
from sqlite import SQLData
from datetime import datetime
import telebot
from telebot import types
import logging
import os
from flask import Flask, request

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN, threaded=False)
server = Flask(__name__)

db = SQLData('db/data.db')
tt = SQLData ('db/timetable.db')

@bot.message_handler(commands=['start'])
def start(message):
	user_id = message.from_user.id
	if not db.user_exist(user_id):
		db.add_user(message.from_user.username, user_id)
		bot.send_message(user_id, HELLO_FIRST.format(message.from_user.first_name), reply_markup=menu_button(), parse_mode='HTML')
	elif db.user_exist(user_id):
		bot.send_message(user_id, START_TEXT.format("".join(db.ex_class(user_id))), reply_markup=menu_button(), parse_mode='HTML')
	else:
		bot.send_message(user_id, ERROR)

@bot.message_handler(commands=['settings'])
def settings(message):
	user_id = message.from_user.id
	bot.send_message(user_id, SETTINGS_TEXT, reply_markup=settings_button())

@bot.message_handler(content_types=['text'])
def message(message):
	user_id = message.from_user.id
	if message.text == TIMETABLE_BUTTON or message.text == ATIMETABLE_BUTTON:
		if message.text == TIMETABLE_BUTTON and "".join(db.ex_class(user_id)) == 'Nope':
			db.in_type('0', user_id)
			bot.send_message(user_id, CLASS_TEXT, reply_markup=class_button())
		elif message.text == TIMETABLE_BUTTON and "".join(db.ex_class(user_id)) != 'Nope':
			db.in_type('0', user_id)
			bot.send_message(user_id, 'На когда?', reply_markup=when_button())
		elif message.text == ATIMETABLE_BUTTON and "".join(db.ex_aclass(user_id)) == 'Nope':
			db.in_type('1', user_id)
			bot.send_message(user_id, CLASS_TEXT, reply_markup=aclass_button())
		elif message.text == ATIMETABLE_BUTTON and "".join(db.ex_aclass(user_id)) != 'Nope':
			db.in_type('1', user_id)
			bot.send_message(user_id, 'На когда?', reply_markup=when_button())

	elif message.text in CLASS_LIST or message.text in ACLASS_LIST:
		if message.text in CLASS_LIST:
			db.update_class(message.text, user_id)
			bot.send_message(user_id, 'На когда?', reply_markup=when_button())
		elif message.text in ACLASS_LIST:
			db.update_aclass(message.text.strip('.'), user_id)
			bot.send_message(user_id, 'На когда?', reply_markup=when_button())
	elif message.text == 'Сегодня':
		send_table(message, datetime.today().weekday())
	elif message.text == 'Завтра':
		if datetime.today().weekday() == 6:
			send_table(message, 0)
		else:
			send_table(message, datetime.today().weekday() + 1)
	elif message.text == SETTINGS_BUTTON:
		settings(message)
	elif message.text == CHANGE_CLASS_BUTTON:
		bot.send_message(user_id, CLASS_TEXT, reply_markup=class_button())
	elif message.text == BACK_BUTTON:
		start(message)

def send_table(message, day):
	user_id = message.from_user.id
	if day != 6:
		if db.ex_type(user_id)[0] == 0:
			bot.send_message(user_id, TIMETABLE_TEXT.format("".join(db.ex_class(user_id)), date(day), tt.timetable(tdate(day), ''.join(db.ex_class(user_id)))), reply_markup=menu_button(), parse_mode='HTML')
		elif db.ex_type(user_id)[0] == 1:
			bot.send_message(user_id, TIMETABLE_TEXT.format("".join(db.ex_aclass(user_id)), date(day), tt.timetable(tdate(day), ''.join(db.ex_aclass(user_id)))), reply_markup=menu_button(), parse_mode='HTML')
			db.update_aclass('Nope', user_id)
	elif day == 6:
		bot.send_message(user_id, SUNDAY_TEXT.format(date(day)), reply_markup=menu_button(), parse_mode='HTML')

"""@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200

@server.route("/")
def webhook():
	bot.remove_webhook()
	bot.set_webhook(url='https://{}.herokuapp.com/'.format(APP_NAME) + TOKEN)
	return "Bot is working", 200"""

if __name__ == '__main__':
#	server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
	bot.polling(none_stop=True)