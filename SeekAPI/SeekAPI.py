import requests
import json
import string
import pandas
import decimal
from operator import itemgetter

from SeekAPI.Auth import Authentication

class SeekAPIInterface(object):

	

	def __init__(self, auth):

		self.base_url = 'http://www.fairdomhub.org/'
		self.headers = {"Content-type": "application/vnd.api+json",
		"Accept": "application/vnd.api+json",
		"Accept-Charset": "ISO-8859-1"}

		self.auth = auth

		self.session = self.Auth()

	def __str__(self):

		return "You have reached the SeekAPIInterface object"

	def __repr__(self):

		return "You have reached the SeekAPIInterface object"

	def remove_non_printable(self, text):

		return ''.join(i for i in text if i in string.printable)

	def Auth(self):

		session = requests.Session()
		session.headers.update(self.headers)

		if self.auth == None:

			print("Please log in here:\n")
			self.auth = Authentication()
			self.auth.login()

		session.auth = self.auth

		return session