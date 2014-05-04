try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A script to calculate peyote stich design options.',
    'author': 'Greg Aitkenhead',
    'url': 'URL where project will be available.',
    'download_url': 'Where to download it.',
    'author_email': 'none',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bead_calculator'],
    'scripts': [],
    'name': 'BeadCalculator'
}

setup(**config)
