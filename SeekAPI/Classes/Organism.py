from SeekAPI.Interfaces.ReadInterface import ReadInterface
from SeekAPI.Interfaces.ListInterface import ListInterface
from SeekAPI.Interfaces.DownloadInterface import DownloadInterface

class Organism(ReadInterface, ListInterface, DownloadInterface):
	
	def __init__(self, auth):
		super().__init__(auth)
		
		self.concept_uri = []

		self.projects = []
		self.assays = []
		self.models = []

		self.fileTypes = []
	
	def __str__(self):

		return self.title
	
	def __repr__(self):

		return self.title

	def read(self, ID = "None", operation = "organisms"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def printAttributes(self):

		
		string = self.title + " ( " + self.concept_uri + ")" 

		print(string)