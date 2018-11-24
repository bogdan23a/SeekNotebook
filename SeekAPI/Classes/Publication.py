from ..Interfaces.ReadInterface import ReadInterface
from ..Interfaces.ListInterface import ListInterface

class Publication(ReadInterface, ListInterface):

	def __init__(self, auth):

		super().__init__(auth)


		self.abstract = None
		self.journal = {}
		self.publishDate = {}
		self.abstract ={}


		self.people = []
		self.projects = []
		self.investigations = []
		self.studies = []
		self.assays = []
		self.data_files = []
		self.models = []
		self.publications = []
		self.presentations = []
		self.events = []

	def __str__(self):

		return self.title

	def __repr__(self):

		return self.title

	def read(self, ID = "None", operation = "publications"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def printAttributes(self):

		string = self.title
		# string += "\n\n" + self.abstract
		print(string)
