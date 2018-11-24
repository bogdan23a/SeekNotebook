from SeekAPI.Interfaces.ReadInterface import ReadInterface
from SeekAPI.Interfaces.ListInterface import ListInterface

class Study(ReadInterface, ListInterface):
	
	def __init__(self, auth):
		super().__init__(auth)

		self.description = ""

		self.creators = []
		self.submitter = []        
		self.people = []
		self.projects = []
		self.investigation = []
		self.studie = []
		self.data_files = []
		self.assays = []
		self.models = []
		self.sops = []
		self.publications = []
		self.documents = []


	def read(self, ID = "None", operation = "studies"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def printAttributes(self):

		
		string = self.title + "\n"
		string += self.description 

		print(string)