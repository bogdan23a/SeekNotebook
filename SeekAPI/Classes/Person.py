from ..Interfaces.ReadInterface import ReadInterface
from ..Interfaces.ListInterface import ListInterface

class Person(ReadInterface, ListInterface):

	def __init__(self, auth):

		super().__init__(auth)

		self.title = None

	def __str__(self):

		return self.title
	def __repr__(self):

		return self.title


	def read(self, ID = "None", operation = "people"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def parseJSON(self):

		super().parseJSON()

		self.description = self.attributes['description']