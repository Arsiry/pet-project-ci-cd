init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

codestyle:
	python -m pylint **/*.py

test:
#	coverage run --source=. -m unittest discover -s . -p "*tests*.py"
#	coverage xml
	python unit_tests.py

build:
	python setup.py sdist bdist_wheel

