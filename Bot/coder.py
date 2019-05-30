import sqlite3

while True:
	try:
		k= ["","","","","","",""]
		x = 1
		print("Здравствуйте, если вы запустили нашу программу, значит, у вас есть семь ключей.\nКоторое нужно вводить по порядку, в зависимости от номера команды.")
		while x == 1:
			key = 0
			conn = sqlite3.connect('bot.db')
			c = conn.cursor()
			data = c.execute("SELECT flag FROM answer").fetchall()
			for i in range(7):
				k[i] = input("Введите {0} слово: ".format(i+1))
				if data[i][0] == k[i]:
					key+=1
			print("")
			print("")
			if key == 7:
				x = 4
			else:
				print("Вы допустили ошибки, попробуйте ещё раз...")
			conn.commit()
			c.close()
			conn.close()
		if (x==4 and key == 7):
			print("Ваш код: 5495")
			break
	except:
		print("Ошибка :)")