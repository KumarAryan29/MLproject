# This setup.py is responsible for creating my machine learining application as a package(like numpy, pandas, seaborn, etc is a package) and we can also install this package in our projects to use it.

from setuptools import find_packages, setup
# Find_packages is used to find all the packages that are being used in the projects. So, for this we will create a new folder named src(source) and inside it create a file named as __init__.py. So, finally whenever find_packages run in setup.py, it will just see in how many folder we have this __init__.py .

from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:        # This function will return the list of requirements.
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# It is a meta data information of entire project.
setup(
    name = "MLproject",
    version='0.0.1',
    author='Aryan',
    author_email="giet.aryan227@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')     # Requirements will be passed in a list.
)