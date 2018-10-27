import requests
import json
import string
import getpass
import pandas
import decimal
from cryptography.fernet import Fernet

_GLOBAL__password_key = Fernet.generate_key()

class Authentication:

	def __init__(self):

		self.__username = "";
		self.__cipheredPassword = "";
		self.__passwordKey = _GLOBAL__password_key
		self.__cipher_suite = Fernet(self.__passwordKey)

	def login(self):

		self.__username = input('Username: ')

		self.__cipheredPassword = self.__cipher_suite.encrypt(getpass.getpass("Password: ").encode("utf-8"))

	def getUsername(self):

		return self.__username

	def getPassword(self):

		return self.__cipheredPassword

	# def decodePassword(self):




class SeekAPIInterface:

	

	def __init__(self, username = None, password = None):

		self.base_url = 'http://www.fairdomhub.org/'
		self.headers = {"Content-type": "application/vnd.api+json",
		"Accept": "application/vnd.api+json",
		"Accept-Charset": "ISO-8859-1"}

		self.username = username
		self.password = password

		self.session = self.Auth()

	def __str__(self):

		return "You have reached the SeekAPIInterface object"

	def __repr__(self):

		return "You have reached the SeekAPIInterface object"

	def remove_non_printable(self, text):

		return ''.join(i for i in text if i in string.printable)

	def Auth(self):

		session = requests.Session()
		session.headers.update(self.headers)

		self.__cipher_suite = Fernet(_GLOBAL__password_key)
		
		if self.username == None and self.password == None:

			me = Authentication()
			me.login()

			self.username = me.getUsername()
			self.password = me.getPassword()

		session.auth = (self.username, self.__cipher_suite.decrypt(self.password).decode("utf-8"))

		return session

		

	
class ListInterface(SeekAPIInterface):

	def __init__(self, username = None, password = None):
		super().__init__(username, password)
		self.ID = ''
		self.Type = ""
		self.attributes = {}
		self.title = ""
		self.description = ""

		self.relationships = {}

		self.links = {}
		self.json = {}

	def readListJSON(self, operation):
		r = self.session.get(self.base_url + operation)
		r.raise_for_status()

		self.json = r.json();

	def parseListJSON(self):

		print('')




class ReadInterface(SeekAPIInterface):


	def __init__(self, username = None, password = None):

		super().__init__(username, password)
		self.ID = None
		self.Type = None
		self.title = None
		self.attributes = {}
		self.relationships = {}

		self.links = {}
		self.json = {}

	def readJSON(self, operation, ID):

		r = self.session.get(self.base_url + operation + '/' + ID)
		r.raise_for_status()
		self.json = r.json()

	def parseJSON(self):
		self.parseID()
		self.parseType()
		self.parseAttributes()
		self.parseRelationships()
		self.parseLinks()

		
	def parseID(self):

		self.ID = self.json['data']['id']

	def parseType(self):
		
		self.Type = self.json['data']['type']


	def parseAttributes(self):
		
		self.attributes = self.json['data']['attributes']
		self.title = self.attributes['title']
		
	def parseDescription(self):
		
		self.description = self.attributes['description']

	def parseVersion(self):

		self.latest_version = self.attributes['latest_version']

	def parseContentBlobs(self):

		for content_blob in self.attributes['content_blobs']:
			self.content_blobs.append({'link' : content_blob['link'], 'original_filename': content_blob['original_filename'], 'size' : content_blob['size']})

	def parseRelationships(self):

		self.relationships = self.json['data']['relationships']

	def parseCreators(self):

		for creator in self.relationships['creators']['data']:
			self.creators.append(creator['id'])

	def parseSubmitters(self):

		for submitter in self.relationships['submitter']['data']:
			self.submitter.append(submitter['id'])

	def parseOrganisms(self):

		for organism in self.relationships['organisms']['data']:
			self.organisms.append(organism['id'])

	def parsePeople(self):

		for person in self.relationships['people']['data']:
			self.people.append(person['id'])
	
	def parseProjects(self):

		for project in self.relationships['projects']['data']:
			self.projects.append(project['id'])

	def parseInvestigations(self):

		for investigation in self.relationships['investigations']['data']:
			self.investigations.append(investigation['id'])

	def parseInvestigation(self):

		self.investigation = self.relationships['investigation']['data']['id']
	 
	def parseStudies(self):

		for study in self.relationships['studies']['data']:
			self.studies.append(study['id'])

	def parseStudy(self):

		self.study = self.relationships['study']['data']['id']

	def parseDataFiles(self):

		for file in self.relationships['data_files']['data']:
			self.data_files.append(file['id'])

	def parseModels(self):

		for model in self.relationships['models']['data']:
			self.models.append(model['id'])
	
	def parseSOPs(self):

		for sop in self.relationships['sops']['data']:
			self.sops.append(sop['id'])

	def parsePublications(self):

		for publication in self.relationships['publications']['data']:
			self.publications.append(publication['id'])
	
	def parseDocuments(self):

		for document in self.relationships['documents']['data']:
			self.documents.append(document['id'])

	def parseEvents(self):

		for event in self.relationships['events']['data']:
			self.events.append(event['id'])

	def parseLinks(self):

		self.links = self.json['data']['links']


	def printRelationships(self):

		self.readRelationships()

		string = "";
		if hasattr(self, 'creator') and self.creators != []:
			string += 'Creators: '
			for creator in self.creators:
				string += creator.__str__() + ' | '
			string = string[:-2]

		if hasattr(self, 'submitter') and self.submitter != []:
			string += '\nSubmitter: '
			for submitter in self.submitter:
				string += submitter.__str__() + ' | '
			string = string[:-2]

		if hasattr(self, 'organisms') and self.organisms != []:
			string += '\nOrganisms: '
			for organism in self.organisms:
				string += organism + ' | '
			string = string[:-2]

		if hasattr(self, 'people') and self.people != []:
			string += '\nPeople: '
			for person in self.people:
				string += person.__str__() + ' | '
			string = string[:-2]

		if hasattr(self, 'projects') and self.projects != []:
			string += '\nProjects: '
			for project in self.projects:
				string += project + ' | '
			string = string[:-2]

		if hasattr(self, 'investigation') and self.investigation != None:
			string += '\nInvestigation: ' + self.investigation

		if hasattr(self, 'investigations') and self.investigations != None:
			string += '\nInvestigations: '
			for investigation in self.investigations:
				string += investigation + ' | '
			string = string[:-2]
	
		if hasattr(self, 'study') and self.study != None:
			string += '\nStudy: ' + self.study

		if hasattr(self, 'studies') and self.studies != None:
			string += '\nStudies: '
			for study in self.studies:
				string += study + ' | '
			string = string[:-2]

		if hasattr(self, 'data_files') and self.data_files != []:
			string += '\nData Files: '
			for file in self.data_files:
				string += file.__str__() + ' | '
			string = string[:-2]

		if hasattr(self, 'models') and self.models != []:
			string += '\nModels: '
			for model in self.models:
				string += model + ' | '
			string = string[:-2]

		if hasattr(self, 'sops') and self.sops != []:
			string += '\nSOPs: '
			for sop in self.sops:
				string += organism + ' | '
			string = string[:-2]

		if hasattr(self, 'publications') and self.publications != []:
			string += '\nPublications: '
			for publication in self.publications:
				string += publication + ' | '
			string = string[:-2]

		if hasattr(self, 'documents') and self.documents != []:
			string += '\nDocuments: '
			for document in self.documents:
				string += document + ' | '
			string = string[:-2]

		if hasattr(self, 'events') and self.events != []:
			string += '\nEvents: '
			for event in self.events:
				string += event + ' | '
			string = string[:-2]

		print(string)
	
	def readRelationships(self): 

		if hasattr(self, 'creators'):
			creators = self.creators
			self.creators = []
			for creatorName in creators:
				creator = Person(self.username, self.password)
				creator.read(creatorName)
				self.creators.append(creator)

		if hasattr(self, 'submitter'):
			submitter = self.submitter
			self.submitter = []
			for submitterName in submitter:
				sub = Person(self.username, self.password)
				sub.read(submitterName)
				self.submitter.append(sub) 

		if hasattr(self, 'people'):
			people = self.people
			self.people = []
			for personName in people:
				person = Person(self.username, self.password)
				person.read(personName)
				self.people.append(person)

		if hasattr(self, 'data_files'):
			data_files = self.data_files
			self.data_files = []
			for fileName in data_files:
				file = File(self.username, self.password)
				file.read(fileName)
				self.data_files.append(file)




class DownloadInterface(SeekAPIInterface):

	def __init__(self, username = None, password = None):
		super().__init__(username, password);



	def download(self, link, fileName):

		r = self.session.get(link + '/download')
		r.raise_for_status()
		open(fileName, 'wb').write(r.content)
		print("File " + fileName + " has been downloaded")




class Search(ReadInterface):

	def __init__(self, username = None, password = None):

		super().__init__(username, password)

		self.searchChoices =["assays",
        "content_blobs",
        "data_files",
        "documents",
        "events",
        "models",
        "organisms",
        "people",
        "presentations",
        "programmes",
        "projects",
        "publications",
        "sample_types",
        "sops",
        "studies",
        "all"]

		self.results = []

		self.searchType = []
		self.json = {}

		self.searchTerm = input("Enter your search: \n")

		choice = None
		while choice not in self.searchChoices:
		    choice = input("Please enter one of: " + ', '.join(self.searchChoices))

		self.searchType = choice

	# def __str__(self):

	# def __repr__(self):

	def read(self):

		self.readJSON()
		self.parseJSON()

	def readJSON(self):
		payload = {'q': self.searchTerm, 'search_type': self.searchType}

		r = requests.get(self.base_url + 'search', headers=self.headers, params=payload)

		r.raise_for_status()

		self.json = r.json()

	def parseJSON(self):

		for item in self.json['data']:
			self.results.append({'id': item['id'], 'type': item['type'], 'title': item['attributes']['title']})

	def printResults(self):

		string = "\n"
		for entry in self.results:
			string += entry['title'] + "\n"
		print(string)

	def getID(self, title):

		for entry in self.results:
			if entry['title'] == title:
				return entry['id']

	def getType(self, title):

		for entry in self.results:
			if entry['title'] == title:
				return entry['type']




class Assay(ReadInterface, ListInterface):

	def __init__(self, username = None, password = None):

		super().__init__(username, password)


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


	

class Person(ReadInterface, ListInterface):

	def __init__(self, username = None, password = None):
		super().__init__(username, password)
		self.title = None

	def __str__(self):

		return self.attributes['title']
	def __repr__(self):

		return self.attributes['title']


	def read(self, ID = "None", operation = "people"):

		# Check if the request made is actually a list request
		if(ID == "None"):
			self.readListJSON(operation)
			self.parseListJSON()
		else:
			self.readJSON(operation, ID)
			self.parseJSON()



	
class File(ReadInterface, ListInterface, DownloadInterface):

	def __init__(self, username = None, password = None):
		super().__init__(username, password)
		
		
		self.description = None
		self.latest_version = None
		self.versions = []
		# self.size = None
		# self.content_blobLinks = []
		# self.content_blobFiles = []
		self.content_blobs = []

		self.creators = []
		self.submitter = []
		self.people = []
		self.projects = []
		self.investigations = []
		self.studies = []
		self.assasys = []
		self.publications = []
		self.events = []

	def __str__(self):

		return self.title

	def __repr__(self):

		return self.title

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
		self.parsePublications()
		self.parseEvents();

	def printAttributes(self):

		string = self.title + " (version: " + self.latest_version.__str__() + ")" 
		if self.description != None:
			string += "\n\n" + self.description
		string += "\nContent Blobs:"
		for blob in self.content_blobs:
			string += "\n" + blob['link'] + " - " + self.getSize(blob['size']) + "\n"
		string = string[:-2]

		print(string)

	def getSize(self, sizeInB):

		if sizeInB >= 1000000000:
			return (decimal.Decimal(sizeInB) / decimal.Decimal(1000000000)).__str__() + ' GB '
		elif sizeInB >= 1000000:
			return (decimal.Decimal(sizeInB) / decimal.Decimal(1000000)).__str__() + ' MB '
		elif sizeInB >= 1000:
			return (decimal.Decimal(sizeInB) / decimal.Decimal(1000)).__str__() + ' KB '
		else :
			return sizeInB + ' B'


