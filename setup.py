from setuptools import setup, find_packages

# Currently, toy robot do not have required packages yet but placing this for the future needed packages
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# Figure out project requirements
install_reqs = parse_requirements('./requirements.txt')
requires = install_reqs

# Configure setup
setup(
    name="Toy-Robot-Code-Challenge",
    version='0.0.1',
    description='Toy Robot Code Challenge',
    long_description=open('README.md', encoding='utf8').read(),
    author='Stefanny Bucag',
    author_email='msibucag@gmail.com',
    packages=find_packages(exclude=('tests', 'examples')),
    install_requires=requires
)
