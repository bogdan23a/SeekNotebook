from SeekAPI.Interfaces import ReadInterface, ListInterface

class SOP(ReadInterface, ListInterface, DownloadInterface):

	def __init__(self, username = None, password = None):
		super().__init__(username, password)
		
		
		self.description = None
		self.latest_version = None
		self.versions = []
		self.content_blobs = []
		self.tags = []
		self.policy = []

		self.creators = []
		self.submitter = []
		self.people = []
		self.projects = []
		self.investigations = []
		self.studies = []
		self.assays = []
		self.publications = []

		self.fileTypes = []

	def read(self, ID = "None", operation = "data_files"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def parseJSON(self):

		super().parseJSON()
		self.parseDataFileAttributes()
		self.parseDataFileRelationships()

	def parseDataFileAttributes(self):

		self.parseDescription()
		self.parseVersion()
		self.parseContentBlobs()

	def parseDataFileRelationships(self):

		self.parseCreators()
		self.parseSubmitters()
		self.parsePeople()
		self.parseProjects()
		self.parseInvestigations()
		self.parseStudies()
		self.parseAssays()
		self.parsePublications()
		self.parseEvents()

		self.getFileTypes()

	def printAttributes(self):

		string = self.title + " (current version: " + self.latest_version.__str__() + ")" 
		if self.description != None:
			string += "\n\n" + self.description
		string += "\nContent Blobs:"
		for blob in self.content_blobs:
			string += "\n" + blob['link'] + " - " + self.getSize(blob['size']) + "\n"
		string = string[:-2]


		string += "\nFile types: "
		for fileType in self.fileTypes:
			string += fileType + " | "
		string = string[:-2]

		print(string)