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

		if hasattr(self, 'description'):
			self.parseDescription()
		
		if hasattr(self, 'version'):
			self.parseVersion()

		if hasattr(self, 'concept_uri'):
			self.parseConceptUri()

		if hasattr(self, 'content_blobs'):
			self.parseContentBlobs()
		
		if hasattr(self, 'avatar'): # TODO 
			pass

		if hasattr(self, 'web_page'): # TODO
			pass

		if hasattr(self, 'wiki_page'): # TODO
			pass
			
		if hasattr(self, 'policy'): # TODO
			pass
		

	def parseDescription(self):
		
		self.description = self.attributes['description']

	def parseVersion(self):

		self.latest_version = self.attributes['latest_version']

	def parseConceptUri(self):

		self.concept_uri = self.attributes['concept_uri']

	def parseContentBlobs(self):

		for content_blob in self.attributes['content_blobs']:
			self.content_blobs.append({'link' : content_blob['link'], 'original_filename': content_blob['original_filename'], 'size' : content_blob['size']})

	def parseRelationships(self):

		self.relationships = self.json['data']['relationships']

		if hasattr(self, 'creators'):
			self.parseCreators()

		if hasattr(self, 'submitters'):
			self.parseSubmitters()

		if hasattr(self, 'organisms'):
			self.parseOrganisms()

		if hasattr(self, 'people'):
			self.parsePeople()
		
		if hasattr(self, 'projects'):
			self.parseProjects()

		if hasattr(self, 'investigations'):
			self.parseInvestigations()

		if hasattr(self, 'investigation'):
			self.parseInvestigation()
		
		if hasattr(self, 'study'):
			self.parseStudy()

		if hasattr(self, 'studies'):
			self.parseStudies()

		if hasattr(self, 'data_files'):
			self.parseDataFiles()

		if hasattr(self, 'models'):
			self.parseModels()
		
		if hasattr(self, 'sops'):
			self.parseSOPs()

		if hasattr(self, 'assays'):
			self.parseAssays()

		if hasattr(self, 'publications'):
			self.parsePublications()

		if hasattr(self, 'documents'):
			self.parseDocuments()

		if hasattr(self, 'events'):
			self.parseEvents()


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
		from ..Classes.File import File
		from ..Classes.Organism import Organism
		from ..Classes.Project import Project
		from ..Classes.Model import Model
		from ..Classes.SOP import SOP
		from ..Classes.Investigation import Investigation
		from ..Classes.Study import Study
		from ..Classes.Publication import Publication

		# if (hasattr(self,'creators') and isinstance(self.creators[0], Person) == False) or (hasattr(self, 'projects') and isinstance(self.projects[0], Project) == False):
		# if self.relationships == {}:
		self.readRelationships() # TODO - verification

		string = ""


		if hasattr(self, 'creators') and self.creators != []:
			string += 'Creators: '
			for creator in self.creators:
				string += creator.title + ' | '
			string = string[:-2]

		if hasattr(self, 'submitter') and self.submitter != []:
			string += '\n\n\nSubmitter: '
			for submitter in self.submitter:
				string += submitter.title + ' | '
			string = string[:-2]

		if hasattr(self, 'organisms') and self.organisms != []:
			string += '\n\n\nOrganisms: '
			for organism in self.organisms:
				string += organism.title + ' | '
			string = string[:-2]

		if hasattr(self, 'people') and self.people != []:
			string += '\n\n\nPeople: '
			for person in self.people:
				string += person.title + ' | '
			string = string[:-2]

		if hasattr(self, 'projects') and self.projects != []:
			string += '\nProjects: '
			for project in self.projects:
				string += project.title + ' | '
			string = string[:-2]

		if hasattr(self, 'investigation') and self.investigation != None:
			string += '\n\n\nInvestigation: ' + self.investigation.title

		if hasattr(self, 'investigations') and self.investigations != None:
			string += '\n\n\nInvestigations: '
			for investigation in self.investigations:
				string += investigation.title + ' | '
			string = string[:-2]
	
		if hasattr(self, 'study') and self.study != None:
			string += '\n\n\nStudy: ' + self.study.title

		if hasattr(self, 'studies') and self.studies != None:
			string += '\n\n\nStudies: '
			for study in self.studies:
				string += study.title + ' | '
			string = string[:-2]

		if hasattr(self, 'data_files') and self.data_files != []:
			string += '\n\n\nData Files: '
			for fil in self.data_files:
				string += fil.title + ' | '
			string = string[:-2]

		if hasattr(self, 'models') and self.models != []:
			string += '\n\n\nModels: '
			for model in self.models:
				string += model.title + ' | '
			string = string[:-2]

		if hasattr(self, 'sops') and self.sops != []:
			string += '\n\n\nSOPs: '
			for sop in self.sops:
				string += sop.title + ' | '
			string = string[:-2]

		if hasattr(self, 'assays') and self.assays != []:
			string += '\n\n\nAssays: '
			for assay in self.assays:
				string += assay.title + ' | '
			string = string[:-2]

		if hasattr(self, 'publications') and self.publications != []:
			string += '\nPublications: '
			for publication in self.publications:
				string += publication.title + ' | '
			string = string[:-2]

		if hasattr(self, 'documents') and self.documents != []:
			string += '\n\n\nDocuments: '
			for document in self.documents:
				string += document + ' | '
			string = string[:-2]

		if hasattr(self, 'events') and self.events != []:
			string += '\n\n\nEvents: '
			for event in self.events:
				string += event + ' | '
			string = string[:-2]
		
		
		print(string)
	
	#TODO - Merge readObjects from Search with this
	def readRelationships(self): 

		from ..Classes.Assay import Assay
		from ..Classes.Person import Person
		from ..Classes.File import File
		from ..Classes.Organism import Organism
		from ..Classes.Project import Project
		from ..Classes.Model import Model
		from ..Classes.SOP import SOP
		from ..Classes.Investigation import Investigation
		from ..Classes.Study import Study
		from ..Classes.Publication import Publication

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
				fil = File(self.auth)
				fil.read(fileName)
				self.data_files.append(fil)

		if hasattr(self, 'organisms'):
			organisms = self.organisms
			self.organisms = []
			print("organisms", end="")
			for organismName in organisms:
				print(".", end="")
				organism = Organism(self.auth)
				organism.read(organismName)
				self.organisms.append(organism)
		
		if hasattr(self, 'projects'):
			projects = self.projects
			self.projects = []
			print("projects", end="")
			for projectName in projects:
				print(".", end="")
				project = Project(self.auth)
				project.read(projectName)
				self.projects.append(project)

		if hasattr(self, 'models'):
			models = self.models
			self.models = []
			print("models", end="")
			for modelName in models:
				print(".", end="")
				model = Model(self.auth)
				model.read(modelName)
				self.models.append(model)
		
		if hasattr(self, 'sops'):
			sops = self.sops
			self.sops = []
			print("sops", end="")
			for sopName in sops:
				print(".", end="")
				sop = SOP(self.auth)
				sop.read(sopName)
				self.sops.append(sop)

		if hasattr(self, 'investigations'):
			investigations = self.investigations
			self.investigations = []
			print("investigatons", end="")
			for investigationName in investigations:
				print(".", end="")
				investigation = Investigation(self.auth)
				investigation.read(investigationName)
				self.investigations.append(investigation)

		if hasattr(self, 'investigation'):
			investigation = self.investigation
			self.investigation = None
			print("investigaton", end="")
			print(".", end="")
			inv = Investigation(self.auth)
			inv.read(investigation)
			self.investigation = inv

		if hasattr(self, 'studies'):
			studies = self.studies
			self.studies = []
			print("studies", end="")
			for studyName in studies:
				print(".", end="")
				study = Study(self.auth)
				study.read(studyName)
				self.studies.append(study)

		if hasattr(self, "study"):
			study = self.study
			self.study = None
			print("study", end="")
			# for investigationName in investigations:
			print(".", end="")
			s = Study(self.auth)
			s.read(investigation)
			self.study = s
			
		if hasattr(self, 'publications'):
			publications = self.publications
			self.publications = []
			print("publications", end="")
			for publicationName in publications:
				print(".", end="")
				publication = Publication(self.auth)
				publication.read(publicationName)
				self.publications.append(study)
		
		print('Relationships loaded.\n')
