import sqlite3

class SQLData:
	def __init__(self, database):
		self.connection = sqlite3.connect(database, check_same_thread=False)
		self.cursor = self.connection.cursor()

	def user_status(self, user_id):
		with self.connection:
			return self.cursor.execute('''SELECT `status` FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()

	def user_exist(self, user_id):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
			return bool(len(result))

	def add_user(self, username, user_id):
		with self.connection:
			return self.cursor.execute('''INSERT INTO `users` (`username`, `user_id`) VALUES(?,?)''', (username, user_id))

	def update_class(self, cla, user_id):
		with self.connection:
			return self.cursor.execute('''UPDATE `users` SET `classroom` = ? WHERE `user_id` = ?''', (cla, user_id))

	def update_aclass(self, acla, user_id):
		with self.connection:
			return self.cursor.execute('''UPDATE `users` SET `aclassroom` = ? WHERE `user_id` = ?''', (acla, user_id))

	def ex_class(self, user_id):
		with self.connection:
			result = self.cursor.execute('''SELECT `classroom` FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
			for i in result:
				return [i[0] for i in result]

	def ex_aclass(self, user_id):
		with self.connection:
			result = self.cursor.execute('''SELECT `aclassroom` FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
			for i in result:
				return [i[0] for i in result]

	def in_type(self, typec, user_id):
		with self.connection:
			return self.connection.execute('''UPDATE `users` SET `typec` = ? WHERE `user_id` = ?''', (typec, user_id))

	def ex_type(self, user_id):
		with self.connection:
			result = self.connection.execute('''SELECT `typec` FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
			for i in result:
				return [i[0] for i in result]

	def timetable(self, dat, cl):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `mon` WHERE `class` = ?''', (cl,)).fetchall()
			for i in result:
				return "".join(([str(i[1::]) for i in result])).replace('.', '\n').strip("()'").replace("'", "\n").replace(',', ' ').strip('None')

	def close(self):
		self.connection.close()