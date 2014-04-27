try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Bead Counter',
    'author': 'Greg Aitkenhead',
    'url': 'URL where project will be available.',
    'download_url': 'Where to download it.',
    'author_email': 'gregaitkenhead@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bead_counter'],
    'scripts': [],
    'name': 'Bead Counter'
}

setup(**config)