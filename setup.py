from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this will return list of requirements.txt
    '''    
    requirements = []
    with open(file_path) as obj:
        requirement = obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'ml-project',
    version='0.0.1',
    author='harsh',
    author_email='karmathecoder@gmail.com',
    packages= find_packages(),
    # install_requires = ['pandas','numpy']
    install_requires = get_requirements('Requirements.txt')
) 