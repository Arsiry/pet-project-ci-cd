# pet-project-ci-cd

[![Quality Gate Status](http://3.144.23.128:9000/api/project_badges/measure?project=sum-two-numbers&metric=alert_status&token=sqb_1248e64573abae406ef0aa50c601fa4631c35c91)](http://3.144.23.128:9000/dashboard?id=sum-two-numbers)

[![Code Smells](http://3.144.23.128:9000/api/project_badges/measure?project=sum-two-numbers&metric=code_smells&token=sqb_1248e64573abae406ef0aa50c601fa4631c35c91)](http://3.144.23.128:9000/dashboard?id=sum-two-numbers)

[![Coverage](http://3.144.23.128:9000/api/project_badges/measure?project=sum-two-numbers&metric=coverage&token=sqb_1248e64573abae406ef0aa50c601fa4631c35c91)](http://3.144.23.128:9000/dashboard?id=sum-two-numbers)

Simple python "pet" project for sum of two numbers calculation and reading from a file and displaying its contents.

Task 1: Learn and apply CI/CD principles and tools

Task 2: Learn to work with Python packages

## Content
* `project_sum_two_numbers\`, simple python project (sum of two numbers calculating)
* `data\`, directory for sample data files 
* `data\sample.txt`, a sample file with text "Hello world!"
* `project_sum_two_numbers\main.py`, the main function and demonstration code
* `project_sum_two_numbers\__init__.py`, imports and makes the function sum_of_two_numbers from main.py accessible
* `unit_tests.py`, unit tests for python code
* `setup.py`, python package description
* `requirements.txt`, file with prod dependencies
* `requireents-dev.txt`, file with dev dependencies
* `sonar-project.properties`, settings for configuring code analysis in SonarQube
* `Makefile`, make file to check codestyle, run tests, check test coverage
* `.github\workflows\ci.yml`, CI pipeline for automated code linting, code testing and to ensure full test coverage of the code
* `.github\workflows\cd.yml`, CD pipeline for automated build a python package (wheel file), upload package to AWS S3 Bucket

## How to check codestyle
To check codestyle, you need to execute the command in the terminal
```
  make init codestyle
  or
  python -m pylint **/*.py
```

## How to run tests and check test coverage
To run unit tests, you need to execute the command in the terminal
```
  make init test
  or
  python -m unittest discover -s . -p "*tests*.py"
```

## How to execute project
To run the project, you need to execute the command in the terminal
```
  make init
  python project_sum_two_numbers/main.py
```
