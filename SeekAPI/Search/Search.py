from operator import itemgetter

from ..Interfaces.ReadInterface import ReadInterface

class Search(ReadInterface):

	def __init__(self, auth):

		super().__init__(auth)

		self.searchChoices =["assays",
        "data_files",
        "events",
        "institutions",
        "investigations",
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

		self.assays = []
		self.content_blobs = []
		self.data_files = []
		self.documents = []
		self.events = []
		self.institutions = []
		self.investigations = []
		self.models = []
		self.organisms = []
		self.people = []
		self.presentations = []
		self.programmes = []
		self.projects = []
		self.publications = []
		self.sample_types = []
		self.sops = []
		self.studies = []

		self.results = []
		self.searchType = []
		self.json = {}

		self.searchTerm = input("Enter your search: \n")

		choice = None
		while choice not in self.searchChoices:
		    choice = input("Please enter one of: " + ', '.join(self.searchChoices))

		self.searchType = choice

	def __str__(self):

		return "Search for " + self.searchTerm
	def __repr__(self):

		return "Search for " + self.searchTerm

	def read(self):

		self.readJSON()
		self.parseJSON()
		self.readObjects()
		# self.printResults()


	def readJSON(self):
		payload = {'q': self.searchTerm, 'search_type': self.searchType}

		r = self.session.get(self.base_url + 'search', headers=self.headers, params=payload)

		r.raise_for_status()

		self.json = r.json()

	def split(self):

		for item in self.results:
			Type = item['type'].lower()
			if Type == 'assays':
				self.assays.append(item)
			elif Type == 'data_files':
				self.data_files.append(item)
			elif Type == 'events':
				self.events.append(item)
			elif Type == 'institutions':
				self.institutions.append(item)
			elif Type == 'investigations':
				self.investigations.append(item)
			elif Type == 'models':
				self.models.append(item)
			elif Type == 'people':
				self.people.append(item)
			elif Type == 'presentations':
				self.presentations.append(item)
			elif Type == 'programmes':
				self.programmes.append(item)
			elif Type == 'projects':
				self.projects.append(item)
			elif Type == 'publications':
				self.publications.append(item)
			elif Type == 'sample_types':
				self.sample_types.append(item)
			elif Type == 'sops':
				self.sops.append(item)
			elif Type == 'studies':
				self.studies.append(item)

	def parseJSON(self):

		for item in self.json['data']:
			self.results.append({'id': item['id'], 'type': item['type'], 'title': item['attributes']['title']})

		sortedResult = sorted(self.results, key=itemgetter('type'))

		self.results = sortedResult

		self.split()


	# TODO - Merge readObjects into ReadInterface / readRelationships
	def readObjects(self):
		from ..Classes.Assay import Assay
		from ..Classes.Person import Person
		from ..Classes.File import File

		print("\nLoading relationships! Please wait...\n")
		print("assays", end="")
		if self.assays != []:
			assays = self.assays
			self.assays = []
			for assay in assays:
				print(".", end="")
				requestAssay = Assay(self.auth)
				requestAssay.read(assay['id'])
				self.assays.append(requestAssay)
		print("people", end="")
		if self.people != []:
			people = self.people
			self.people = []
			for person in people:
				print(".", end="")
				requestPerson = Person(self.auth)
				requestPerson.read(person['id'])
				self.people.append(requestPerson)
		print("data files", end="")
		if self.data_files != []:
			data_files = self.data_files
			self.data_files = []
			for data_file in data_files:
				print(".", end="")
				requestFile = File(self.auth)
				requestFile.read(data_file['id'])
				self.data_files.append(requestFile)
		print("\n\nRelationships loaded!\n")

	# TODO - Merge this with printRelationships from ReadInterface
	def printResults(self):

		string = "\n"
		
		if self.assays != []:
			string += "ASSAYS\n\n"

			for assay in self.assays:
				string += assay.__str__() + '\n\n'

		if self.people != []:
			string += "PEOPLE\n\n"

			for person in self.people:
				string += person.__str__() + '\n\n'

		if self.data_files != []:
			string += "DATA FILES\n\n"

			for file in self.data_files:
				string += file.__str__() + '\n\n'

		print(string)

	def getID(self, title):

		for entry in self.results:
			if entry['title'] == title:
				return entry['id']

	def getType(self, title):

		for entry in self.results:
			if entry['title'] == title:
				return entry['type']