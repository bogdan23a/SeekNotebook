from SeekAPI.Interfaces.ReadInterface import ReadInterface
from SeekAPI.Interfaces.ListInterface import ListInterface

class Model(ReadInterface, ListInterface):
	
	def __init__(self, auth):
		super().__init__(auth)

		self.description = ""
		self.latest_version = ""
		self.content_blobs = []

		self.creators = []
		self.submitter = []        
		self.people = []
		self.projects = []
		self.investigations = []
		self.studies = []
		self.publications = []
		self.assays = []

	def read(self, ID = "None", operation = "models"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def printAttributes(self):

		
		string = self.title + " (version: " + self.latest_version + ")\n"
		string += self.description 

		print(string)