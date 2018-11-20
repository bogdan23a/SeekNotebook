from .SeekAPIInterface import SeekAPIInterface


class ListInterface(SeekAPIInterface):

	def __init__(self, auth):
		super().__init__(auth)
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


