try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A script to calculate peyote stich design options.',
    'author': 'Greg Aitkenhead',
    'url': 'https://github.com/HarryLoofah/bead-calculator',
    'download_url': 'https://github.com/HarryLoofah/bead-calculator.git',
    'author_email': 'none',
    'version': '0.1',
    'install_requires': ['nose'],
    'license': ['MIT'],
    'packages': ['bead_calculator'],
    'scripts': [],
    'name': 'BeadCalculator'
}

setup(**config)
