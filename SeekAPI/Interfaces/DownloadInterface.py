import decimal

from .SeekAPIInterface import SeekAPIInterface

class DownloadInterface(SeekAPIInterface):

	def __init__(self, auth):
		super().__init__(auth);

	def __str__(self):

		return "Default DownloadInterface"

	def __repr__(self):

		return "Default DownloadInterface"

	def download(self, link, fileName):

		r = self.session.get(link + '/download')
		r.raise_for_status()
		open(fileName, 'wb').write(r.content)
		print("File " + fileName + " has been downloaded")

	def getFileTypes(self):

		for blob in self.content_blobs:
			if blob['original_filename'].count(".") > 0:
				self.fileTypes.append(blob['original_filename'].split('.')[1])

	def getSize(self, sizeInB):

		if sizeInB >= 1000000000:
			return (decimal.Decimal(sizeInB) / decimal.Decimal(1000000000)).__str__() + ' GB '
		elif sizeInB >= 1000000:
			return (decimal.Decimal(sizeInB) / decimal.Decimal(1000000)).__str__() + ' MB '
		elif sizeInB >= 1000:
			return (decimal.Decimal(sizeInB) / decimal.Decimal(1000)).__str__() + ' KB '
		else :
			return sizeInB + ' B'