from mljson import *
import search
from utils import *

dict = FetchFormFields()


rack = dict.get("rack")
patt = dict.get("patt")

matches = search.search(rack, patt)

Return({"words": matches})
