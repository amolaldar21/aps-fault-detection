from setuptools import find_packages,setup

def get_requirements():...



setup(

    name='sensor',
    version='0.0.1',
    author='ineuron',
    author_email='amol21.seo@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),


    )