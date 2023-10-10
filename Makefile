all: 

.FORCE:

tests: .FORCE
	pytest -vv tests

coverage: .FORCE
	coverage run -m pytest
	coverage report -m

