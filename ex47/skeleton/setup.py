try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
      'description':"LP3THW_ex47",
      'author': 'chd0t',
      'url': 'https://github.com/chd0t/LP3THW',
      'download_url': 'https://github.com/chd0t/LP3THW/archive/refs/heads/main.zip',
      'author_email': 'chd0t@gitnub.io',
      'version': '0.1',
      'install_requires': ['nose'],
      'packages': ['ex47'],
      'scripts ': [] ,
      'name': 'ex47'
    }

setup(**config)
