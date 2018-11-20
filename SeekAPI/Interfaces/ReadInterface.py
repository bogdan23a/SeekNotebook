from .SeekAPIInterface import SeekAPIInterface

# from ..Classes.Assay import Assay
# from ..Classes.Person import Person


class ReadInterface(SeekAPIInterface):


	def __init__(self, auth):

		super().__init__(auth)

		self.ID = None
		self.Type = None
		self.title = None
		self.attributes = {}
		self.relationships = {}

		self.links = {}
		self.json = {}

	def __str__(self):

		return "Default ReadInterface"

	def __repr__(self):

		return "Default ReadInterface"

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

	def parseAssays(self):

		for assay in self.relationships['assays']['data']:
			self.assays.append(assay['id'])

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


	# TODO - Merge this with printResults from Search
	def printRelationships(self):

		from ..Classes.Assay import Assay
		from ..Classes.Person import Person

		
		if isinstance(self.creators[0], Person) == False:
			self.readRelationships()

		string = ""


		if hasattr(self, 'creators') and self.creators != []:
			string += 'Creators: '
			for creator in self.creators:
				string += creator.title + ' | '
			string = string[:-2]

		if hasattr(self, 'submitter') and self.submitter != []:
			string += '\nSubmitter: '
			for submitter in self.submitter:
				string += submitter.title + ' | '
			string = string[:-2]

		if hasattr(self, 'organisms') and self.organisms != []:
			string += '\nOrganisms: '
			for organism in self.organisms:
				string += organism + ' | '
			string = string[:-2]

		if hasattr(self, 'people') and self.people != []:
			string += '\nPeople: '
			for person in self.people:
				string += person.title + ' | '
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
				string += file.title + ' | '
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

		if hasattr(self, 'assays') and self.assays != []:
			string += '\nAssays: '
			for assay in self.assays:
				string += assay.title + ' | '
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
	
	#TODO - Merge readObjects from Search with this
	def readRelationships(self): 

		from ..Classes.Assay import Assay
		from ..Classes.Person import Person
		from ..Classes.File import File

		print('\nLoading relationships! Please wait...\n')

		if hasattr(self, 'assays'):
			assays = self.assays
			self.assays = []
			print("assays", end="")
			for assayName in assays:
				print(".", end="")
				assay = Assay(self.auth)
				assay.read(assayName)
				self.assays.append(assay)

		if hasattr(self, 'creators'):
			creators = self.creators
			self.creators = []
			print("creators", end="")
			for creatorName in creators:
				print(".", end="")
				creator = Person(self.auth)
				creator.read(creatorName)
				self.creators.append(creator)

		if hasattr(self, 'submitter'):
			submitter = self.submitter
			self.submitter = []
			print("submitter", end="")
			for submitterName in submitter:
				print(".", end="")
				sub = Person(self.auth)
				sub.read(submitterName)
				self.submitter.append(sub) 

		if hasattr(self, 'people'):
			people = self.people
			self.people = []
			print("people", end="")
			for personName in people:
				print(".", end="")
				person = Person(self.auth)
				person.read(personName)
				self.people.append(person)

		if hasattr(self, 'data_files'):
			data_files = self.data_files
			self.data_files = []
			print("data_files", end="")
			for fileName in data_files:
				print(".", end="")
				file = File(self.auth)
				file.read(fileName)
				self.data_files.append(file)

		print('Relationships loaded.\n')
