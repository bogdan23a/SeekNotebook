import getpass


class Authentication(tuple):

	def __new__(self):

		_username = input('Username: ')
		_password = getpass.getpass("Password: ")

		return tuple.__new__(Authentication, (_username, _password))

