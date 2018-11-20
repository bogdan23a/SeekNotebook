from Interfaces.Auth.Authentication import Authentication
from Interfaces.ReadInterface import ReadInterface

from Interfaces.SeekAPIInterface import SeekAPIInterface

from Classes.Assay import Assay

auth = Authentication()

auth.login()


obj = Assay(auth)
