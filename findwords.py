#!/usr/bin/python

import logger
from mljson import *
import search
from utils import *

dict = FetchFormFields()

logger.info('%s: %s' % (os.path.basename(__file__), repr(dict)))

rack = dict.get('rack')
patt = dict.get('patt')

matches = search.search(rack, patt)

Return({'words': matches})
