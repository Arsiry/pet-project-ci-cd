"""
Package description
"""

from setuptools import setup, find_packages

setup(
    name='project_sum_two_numbers',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'project_sum_two_numbers': ['data/sample.txt']  
    },
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sum_two_numbers=project_sum_two_numbers.main:main",  
        ]
    },
    description='A simple Python package for summing two numbers.',
    author='Anastasiia Trofymova',
    author_email='anastasiiatrofymova@gmail.com',
    url='https://github.com/Arsiry/pet-project-ci-cd',
)
