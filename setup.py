from setuptools import find_packages, setup
from typing import List

PROJECT_NAME = "machine_learning_modular_project"
VERSION ="0.0.1"
AUTHOR_NAME="Salman Rashid"
AUTHOR_EMAIL="salman.rashid@abc.com"
DESCRIPTION="A machine learning project"
REQUIREMENT_FILE_NAME="requirement.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """Returns list of requirements"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = requirement_file.readlines()
        requirement_list = [requirement.replace("\n", "") for requirement in requirements]
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        
        return requirement_list
    
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements()
)