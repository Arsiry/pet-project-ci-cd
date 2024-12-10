# pet-project-ci-cd
Simple python "pet" project for sum of two numbers calculation
Task: Learn and apply CI/CD principles and tools

## Content
* `project_sum_two_numbers.py`, simple python project (sum of two numbers calculating)
* `unit_tests.py`, unit tests
* `requirements.txt`, file with prod dependencies
* `requireents-dev.txt`, file with dev dependencies
* `sonar-project.properties`, settings for configuring code analysis in SonarQube
* `Makefile`, make file to check codestyle, run tests
* `.github\workflows\ci.yml`, CI pipeline for automated code linting, code testing and to ensure full test coverage of the code

## How to check codestyle
To check codestyle, you need to execute the command in the terminal
```
  make init codestyle
```

## How to run tests
To run unit tests, you need to execute the command in the terminal
```
  make init test
```

## how to execute project
To run the project, you need to execute the command in the terminal
```
  make init
  python project_sum_two_numbers.py
```
