import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'gitrdone',
    version = '0.0.1',
    author = 'Kalan MacROw',
    author_email = 'kalanm@gmail.com',
    description = ('A tool to make using git repositories as templates easy.'),
    license = 'MIT',
    keywords = 'git template giter8',
    url = 'https://github.com/kmacrow/gitrdone',
    packages = ['gitrdone'],
    long_description = read('README'),
    install_requires = ['mustache==0.1.4'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Environment :: Console'
    ],
    entry_points = {
        'console_scripts': [
            'gitrdone = gitrdone.CLI:main'
        ]
    }
)
