from ..Interfaces.ReadInterface import ReadInterface
from ..Interfaces.ListInterface import ListInterface

class Assay(ReadInterface, ListInterface):

	def __init__(self, auth):

		super().__init__(auth)


		self.description = None
		self.assayClass = {}
		self.assayType = {}
		self.technology ={}


		self.creators = []
		self.submitter = []
		self.organisms = []
		self.people = []
		self.projects = []
		self.investigation = None
		self.study = None
		self.data_files = []
		self.models = []
		self.sops = []
		self.publications = []
		self.documents = []

	def __str__(self):

		return self.title

	def __repr__(self):

		return self.title

	def read(self, ID = "None", operation = "assays"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()

	def parseJSON(self):

		super().parseJSON()
		self.parseAssayAttributes()
		self.parseAssayRelationships()

		
	def parseAssayAttributes(self):

		self.parseDescription()

		self.assayClass['title'] = self.attributes['assay_class']['title']
		self.assayClass['description'] = self.attributes['assay_class']['description']
		self.assayType['label'] = self.attributes['assay_type']['label']
		self.assayType['uri'] = self.attributes['assay_type']['uri']
		

		self.technology['label'] = self.attributes['technology_type']['label']
		self.technology['uri'] = self.attributes['technology_type']['uri']


	def parseAssayRelationships(self):

		self.parseCreators()
		self.parseSubmitters()
		self.parseOrganisms()
		self.parsePeople()
		self.parseProjects()
		self.parseInvestigation()
		self.parseStudy()
		self.parseDataFiles()
		self.parseModels()
		self.parseSOPs()
		self.parsePublications()
		self.parseDocuments()


	def printAttributes(self):

		string = self.title + " ( " + self.assayClass['title'] + ") " 
		if self.assayType['label'] != None:
			string += self.assayType['label']
		if self.technology['label'] != None:
			string += ", " + self.technology['label']
		if self.description != None:
			string += "\n\n" + self.description
		print(string)
