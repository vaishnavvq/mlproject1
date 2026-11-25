from setuptools import setup,find_packages
from typing import List 


def get_requirements(file_path:str)->List[str]:
    requirement =[]
    with open(file_path) as f:
        requirement = f.readlines()
        requirement = [r.replace('\n','') for r in requirement]
        if '-e .' in requirement:
            requirement.remove('-e .')
        return requirement
setup(
    name ="mlp1",
    version='0.0.1',
    author='vaishnav',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)