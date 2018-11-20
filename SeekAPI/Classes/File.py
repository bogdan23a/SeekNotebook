from ..Interfaces.ReadInterface import ReadInterface
from ..Interfaces.ListInterface import ListInterface
from ..Interfaces.DownloadInterface import DownloadInterface

class File(ReadInterface, ListInterface, DownloadInterface):

	def __init__(self, auth):
		super().__init__(auth)
		
		
		self.description = None
		self.latest_version = None
		self.versions = []
		self.content_blobs = []

		self.creators = []
		self.submitter = []
		self.people = []
		self.projects = []
		self.investigations = []
		self.studies = []
		self.assays = []
		self.publications = []
		self.events = []

		self.fileTypes = []

	def __str__(self):

		string = self.title + " (version: " + self.latest_version.__str__() + ")" 

		string += "\n\tContent Blobs:"
		for blob in self.content_blobs:
			string += self.getSize(blob['size']) + " | "
		string = string[:-2]

		string += "\n\tFile types:"
		for fileType in self.fileTypes:
			string += fileType + " | "
		string = string[:-2]

		return string

	def __repr__(self):

		string = self.title + " (version: " + self.latest_version.__str__() + ")" 

		string += "\n\tContent Blobs:"
		for blob in self.content_blobs:
			string += self.getSize(blob['size']) + " | "
		string = string[:-2]

		string += "\n\tFile types: "
		for fileType in self.fileTypes:
			string += fileType + " | "
		string = string[:-2]

		return string

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

		string = self.title + " (version: " + self.latest_version.__str__() + ")" 
		if self.description != None:
			string += "\n\n" + self.description
		string += "\nContent Blobs:"
		for blob in self.content_blobs:

			# TODO - what if size is not available
			if blob['size'] is not None:
				string += "\n" + blob['link'] + " - " + self.getSize(blob['size']) + "\n"
		string = string[:-2]

		# TODO - what if file has no type
		
		string += "\nFile types: "
		for fileType in self.fileTypes:
			string += fileType + " | "
		string = string[:-2]

		print(string)