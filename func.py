from messages import *
from datetime import datetime
from telebot import types

def menu_button():
	menu = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
	timetab = types.KeyboardButton(TIMETABLE_BUTTON)
	anothertab = types.KeyboardButton(ATIMETABLE_BUTTON)	
	settings = types.KeyboardButton(SETTINGS_BUTTON)
	menu.add(timetab, anothertab, settings)
	return menu

def settings_button():
	set_menu = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
	change = types.KeyboardButton(CHANGE_CLASS_BUTTON)
	back = types.KeyboardButton(BACK_BUTTON)
	set_menu.add(change, back)
	return set_menu

def when_button():
	when = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
	today = types.KeyboardButton('Сегодня')
	tomorrow = types.KeyboardButton('Завтра')
	when.add(today, tomorrow)
	return when

def class_button():
	classes = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
	itembtn9a = types.KeyboardButton('9-А')
	itembtn9b = types.KeyboardButton('9-Б')
	itembtn9v = types.KeyboardButton('9-В')
	itembtn10a = types.KeyboardButton('10-А')
	itembtn10b = types.KeyboardButton('10-Б')
	itembtn10v = types.KeyboardButton('10-В')
	itembtn11a = types.KeyboardButton('11-А')
	itembtn11b = types.KeyboardButton('11-Б')
	itembtn11v = types.KeyboardButton('11-В')
	classes.add(itembtn9a, itembtn10a, itembtn11a, itembtn9b, itembtn10b, itembtn11b, itembtn9v, itembtn10v, itembtn11v)
	return classes

def aclass_button():
	classes = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
	itembtn9a = types.KeyboardButton('9-А.')
	itembtn9b = types.KeyboardButton('9-Б.')
	itembtn9v = types.KeyboardButton('9-В.')
	itembtn10a = types.KeyboardButton('10-А.')
	itembtn10b = types.KeyboardButton('10-Б.')
	itembtn10v = types.KeyboardButton('10-В.')
	itembtn11a = types.KeyboardButton('11-А.')
	itembtn11b = types.KeyboardButton('11-Б.')
	itembtn11v = types.KeyboardButton('11-В.')
	classes.add(itembtn9a, itembtn10a, itembtn11a, itembtn9b, itembtn10b, itembtn11b, itembtn9v, itembtn10v, itembtn11v)
	return classes

def tdate(x):
	if x == 0:
		week = 'Mon'
	elif x == 1:
		week = 'Tue'
	elif x == 2:
		week = 'Wed'
	elif x == 3:
		week = 'Thu'
	elif x == 4:
		week = 'Fri'
	elif x == 5:
		week = 'Sat'
	return week

def date(x):
	if x == 0:
		week = 'Понедельник'
	elif x == 1:
		week = 'Вторник'
	elif x == 2:
		week = 'Среда'
	elif x == 3:
		week = 'Четверг'
	elif x == 4:
		week = 'Пятница'
	elif x == 5:
		week = 'Суббота'
	elif x == 6:
		week = 'Воскресенье'
	return week