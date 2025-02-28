init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

codestyle:
	python -m pylint **/*.py

test:
	coverage run --source=project_sum_two_numbers -m unittest discover -s . -p "*tests*.py"
	coverage xml

build:
	python setup.py sdist bdist_wheel

upload:
	aws s3 cp dist/*.whl s3://project-sum-two-numbers-wheels/
