from SeekAPI.Interfaces.ReadInterface import ReadInterface
from SeekAPI.Interfaces.ListInterface import ListInterface

class Project(ReadInterface, ListInterface):
	
	def __init__(self, auth):
		super().__init__(auth)
		
		self.avatar = ""
		self.description = ""
		self.web_page = ""
		self.wiki_page = ""
		self.policy = ""

		self.organisms = []
		self.people = []
		self.institutions = []
		self.programmes = []
		self.investigations = []
		self.studies = []
		self.data_files = []
		self.sops = []
		self.publications = []
		self.presentations = []
		self.events = []
		self.documents = []
		self.assays = []
		self.models = []

	def read(self, ID = "None", operation = "projects"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def printAttributes(self):

		
		string = self.title + " ( " + self.wiki_page + ")\n"
		string += self.description 

		print(string)