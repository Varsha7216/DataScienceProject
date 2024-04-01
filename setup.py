from setuptools import find_packages,setup

def get_requirement(file_path):
    reuirements=[]
    hypen_e_dot="-e ."
    with open(file_path)as file_object:
        reuirements=file_object.readlines()
        reuirements=[req.replace("\n","") for req in reuirements]
        if hypen_e_dot in reuirements:
            reuirements.remove(hypen_e_dot)
    return reuirements

setup(
    name="DataScienceProject",
    version="0.0.1",
    author="Varsha",
    author_email="varshakumari.6594@gmail.com",
    package=find_packages(),
    install_requires=get_requirement('requirement.txt')
)