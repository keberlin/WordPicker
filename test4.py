#!/usr/bin/python

import search

rack = 'chelsay'
patts = ['$...$','$....$']

matches = search.search2(rack, patts)

if not matches:
  print 'None found'
else:
  for match in matches:
    print match
