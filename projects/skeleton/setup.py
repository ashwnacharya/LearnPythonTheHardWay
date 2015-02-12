try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': ' pygame',
	'author': 'ashwin'
	'url':'http://github.com/ashwnacharya',
	'author_email': 'my Email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['pygame'],
	'scripts': [],
	'name': 'pygame'
}

setup(**config)