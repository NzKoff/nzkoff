# -*- coding: utf-8 -*-
import telebot
import config
import time
import sqlite3
'''import os'''

bot = telebot.TeleBot(config.token)

conn = sqlite3.connect('general.db')
c = conn.cursor()
data = c.execute("SELECT * FROM event").fetchall()
print(data)

def sqlbase(username, chatid):
	try:
		conn = sqlite3.connect('bot.db')
		c = conn.cursor()
		data = c.execute("SELECT chatid FROM bot").fetchall()
		key = 0
		for line in data:
			if line[0] == chatid:
				key = 1
		if key == 0:
			c.execute("INSERT INTO bot(username, chatid, flag1, flag2, flag3, flag4, flag5 , flag6, flag7, answer,teamnum) values ('{0}', '{1}',\
	         '{2}', '{2}', '{2}', '{2}', '{2}', '{2}', '{2}', '{2}', '{3}')".format(username, chatid, 'No',0))
		conn.commit()
		c.close()
		conn.close()
	except:
		print("Ошибка в sqlbase")

def sqltask(chatid):
	conn = sqlite3.connect('bot.db')
	c = conn.cursor()
	MyFlagKey = False
	data = c.execute("SELECT flag1,flag2,flag3,flag4,flag5,flag6,flag7,teamnum FROM bot WHERE chatid ={0}".format(chatid)).fetchall()
	for k in range(0,7):
		if data[0][k] == 'No':
			bot.send_message(421033102, "Команда №{0}. Прошла этап №{1}.".format(data[0][7],k+1))
			bot.send_message(179736804, "Команда №{0}. Прошла этап №{1}.".format(data[0][7],k+1))
			c.execute("UPDATE bot SET flag{0} ='{1}' WHERE chatid={2}".format(str(k+1), 'Yes', chatid))
			bot.send_message(chatid, "Молодцы! Вы смогли! Вы сдали уже {0} флагов из 7.\nВам осталось: {1}".format(k+1,7-k-1))
			conn.commit()
			if k == 6:
				MyFlagKey = True
			else:
				kdk = data[0][7]+k+1
				if (kdk > 7):
					kdk -= 7
				bot.send_message(chatid, "Ваш следующий этап:")
				bot.send_photo(chatid, "https://ctflife.000webhostapp.com/maps/3_etazh_{0}.png".format(kdk))
			break
	if MyFlagKey == True:
		teamnum = data[0][7]
		data = c.execute("SELECT flag FROM answer WHERE teamnum ={0}".format(teamnum)).fetchall()
		c.execute("UPDATE bot SET answer ='{0}' WHERE chatid={1} and teamnum = {2}".format(data[0][0], chatid, teamnum))
		#bot.send_message(chatid, "Ваш ключ для следующего этапа: '{0}'.\nНе удаляйте его!".format(data[0][0]))
		bot.send_message(chatid, "Вы прошли все испытания! Теперь у вас есть бумажные ключи, отправляйтесь с ними в актовый зал!")
	conn.commit()
	c.close()
	conn.close()

@bot.message_handler(commands=['help'])
def send_message(message):
	try:
		hi = "Доступные команды:\n/start - введение\n/flag - сдать ответ после секции" \
	         "\n/time - узнать время\n/team - выбрать команду (Написан номер в послании)\n/help - помощь"
		bot.send_message(message.chat.id, hi)
	except:
		print("Ошибка в time")
	sqlbase(message.chat.username,message.chat.id)

@bot.message_handler(commands=['start'])
def send_message(message):
	try:
	    hi = "Ваши команды вступили в игру!\n/flag - сдать ответ после секции\n/time - узнать время\n/team - выбрать команду (Написан номер в послании)\n/help - помощь"
	    bot.send_message(message.chat.id, hi)
	except:
		print("Ошибка в start")    
	sqlbase(message.chat.username,message.chat.id)

@bot.message_handler(commands=['time'])
def get_time(message):
	try:
		if time.localtime()[4]<10:
			TIME = "Время: " + str(time.localtime()[3]) + ":0" + str(time.localtime()[4]) + "\nДата: " \
			+ str(time.localtime()[2]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[0])
		else:
			TIME = "Время: " + str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + "\nДата: " \
			+ str(time.localtime()[2]) + "." + str(time.localtime()[1]) + "." + str(time.localtime()[0])
		bot.send_message(message.chat.id, TIME)
		#bot.send_photo(message.chat.id, "http://img.ii4.ru/images/2017/12/17/907799_web.png")
	except:
		print("Ошибка в time")
	sqlbase(message.chat.username,message.chat.id)

@bot.message_handler(commands=['team'])
def get_flag(message):
	sqlbase(message.chat.username,message.chat.id)
	try:
		chislo = int(message.text[-1])
		if (chislo>0 and chislo<8):
			conn = sqlite3.connect('bot.db')
			c = conn.cursor()
			c.execute("UPDATE bot SET teamnum ={0} WHERE chatid='{1}' and teamnum = {2}".format(chislo, message.chat.id, 0))
			data = c.execute("SELECT teamnum FROM bot WHERE chatid ='{0}'".format(message.chat.id)).fetchall()
			bot.send_message(message.chat.id, "Номер вашей команды - {0}.\nВаша первая станция:".format(data[0][0]))
			#bot.send_photo(message.chat.id, "http://img.ii4.ru/images/2017/12/17/{0}_web.png".format(data[0][0]))
			bot.send_photo(message.chat.id, "https://ctflife.000webhostapp.com/maps/3_etazh_{0}.png".format(data[0][0]))
			conn.commit()
			c.close()
			conn.close()
		else:
			bot.send_message(message.chat.id, "Введите в team значение от 1 до 7 через пробел.\nПример: '/team 1'")
	except:
		bot.send_message(message.chat.id, "Введите в team значение от 1 до 7 через пробел.\nПример: '/team 1'")

@bot.message_handler(commands=['addmessage'])
def get_flag(message):
	sqlbase(message.chat.username,message.chat.id)
	try:
		addmessage = message.text[12:]
		conn = sqlite3.connect('bot.db')
		c = conn.cursor()
		c.execute("INSERT INTO flags(flag) values ('{0}')".format(addmessage))
		conn.commit()
		c.close()
		conn.close()
		bot.send_message(message.chat.id, "Вы успешно добавили флаг: {0}".format(addmessage))
	except:
		bot.send_message(message.chat.id, "Произошла ошибка, попробуйте ещё раз.")

@bot.message_handler(commands=['addanswer'])
def get_flag(message):
	sqlbase(message.chat.username,message.chat.id)
	try:
		idnumberr = int(message.text[11])
		addanswer = message.text[13:]
		conn = sqlite3.connect('bot.db')
		c = conn.cursor()
		c.execute("INSERT INTO answer(flag,teamnum) values ('{0}',{1})".format(addanswer,idnumberr))
		conn.commit()
		c.close()
		conn.close()
		bot.send_message(message.chat.id, "Вы успешно добавили answer: {0}".format(addanswer))
	except:
		bot.send_message(message.chat.id, "Произошла ошибка, попробуйте ещё раз.")

@bot.message_handler(commands=['sendallmessage'])
def get_flag(message):
	sqlbase(message.chat.username,message.chat.id)
	try:
		sendallmessage = message.text[16:]
		conn = sqlite3.connect('bot.db')
		c = conn.cursor()
		data = c.execute("SELECT chatid FROM bot").fetchall()
		for line in data:
			bot.send_message(line[0], sendallmessage)
		conn.commit()
		c.close()
		conn.close()
	except:
		bot.send_message(message.chat.id, "Произошла ошибка, попробуйте ещё раз.")

@bot.message_handler(commands=['flag'])
def get_flag(message):
	sqlbase(message.chat.username,message.chat.id)
	try:
		mesflag = message.text[6:]
		conn= sqlite3.connect('bot.db')
		c = conn.cursor()
		data = c.execute("SELECT teamnum, answer FROM bot WHERE chatid ='{0}'".format(message.chat.id)).fetchall()
		if data[0][0] == 0:
			bot.send_message(message.chat.id, "Сначала выберите команду, для этого к Игротехам!")
		elif data[0][1] == 'No':
			data = c.execute("SELECT id FROM flags WHERE flag ='{0}'".format(mesflag)).fetchall()
			if (data[0][0]>0 and data[0][0]<100):
				c.execute("UPDATE flags SET flag = '{0}' WHERE flag='{1}'".format('FlagUsedGoNext :)', mesflag))
				conn.commit()
				c.close()
				conn.close()
				sqltask(message.chat.id)
			else:
				conn.commit()
				c.close()
				conn.close()
				bot.send_message(message.chat.id, "Флаг не верный. Возможно он был уже был использован\nПерепроверьте, в случае ошибки подойдите к Игротеху.")
		else:
			#bot.send_message(message.chat.id, "Вы уже ввели все флаги и получили свой ответ: '{0}'".format(data[0][1]))
			bot.send_message(message.chat.id, "Вы уже получили все ответы. Возвращайтесь в актовый зал!")
	except:
		bot.send_message(message.chat.id, "Флаг не верный. Возможно он был уже был использован\nПерепроверьте, в случае ошибки подойдите к Игротеху.")


if __name__ == '__main__':
    bot.polling(none_stop=True)