from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

# Figure out project requirements
install_reqs = parse_requirements('./requirements.txt', session=PipSession())
requires = [str(ir.req) for ir in install_reqs]

# Configure setup
setup(
    name="Toy-Robot-Code-Challenge",
    version=version,
    description='Toy Robot Code Challenge',
    long_description=open('README.md', encoding='utf8').read(),
    author='Stefanny Bucag',
    author_email='msibucag@gmail.com',
    packages=find_packages(exclude=('tests', 'examples')),
    install_requires=requires
)
