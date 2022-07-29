from setuptools import setup, find_packages

from os.path import dirname

with open(f"{dirname(__file__)}/requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(
    name='wikijspy',
    version='0.1.4',
    author='WERTBON1789',
    author_email='jan210404@gmx.de',
    packages=find_packages(),
    license='LICENSE',
    description='A simple wikijs API wrapper',
    long_description="""Github Repository: https://github.com/WERTBON1789/wikijs-api-wrapper""",
    install_requires=install_requires
)
