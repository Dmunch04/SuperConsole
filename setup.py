import multiprocessing
from setuptools import setup

with open ('README.md', 'r') as README:
    Description = README.read ()

setup (
    name = 'superconsole',
    version = '0.0.1',
    packages = ['superconsole'],
    author = 'Munchii',
    author_email = 'contact@munchii.me',
    license = 'MIT',
    description = 'Expanded console for Python',
    long_description = Description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Dmunch04/SuperConsole',
    install_requires = [
        'colorama',
        'DavesLogger'
    ],
    classifiers = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
    ],
    keywords = 'expanded console for python'
)
