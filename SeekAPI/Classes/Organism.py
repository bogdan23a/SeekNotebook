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

	def read(self, ID = "None", operation = "sops"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def parseJSON(self):

		super().parseJSON()
		self.parseOrganismAttributes()
		self.parseOrganismRelationships()

	def parseOrganismAttributes(self):

		# self.parseDescription()
		# self.parseVersion()
		# self.parseContentBlobs()
        self.parseConceptUri()

	def parseSOPRelationships(self):

		# self.parseCreators()
		# self.parseSubmitters()
		# self.parsePeople()
		self.parseProjects()
		# self.parseInvestigations()
		# self.parseStudies()
		self.parseAssays()
		# self.parsePublications()
        self.parseModels()

		self.getFileTypes()

	def printAttributes(self):

		
		string = self.title + " ( " + self.concept_uri. + ")" 

		print(string)