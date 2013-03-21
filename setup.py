"""FutureGrid: CMD3

This project is based on material developed by Gregor von Laszewski
Significant potions of it are developed as pat of the CoG Shell and
Cyberaide projects.

"""

from setuptools import setup, find_packages
import sys, os

doclines = __doc__.split("\n")

######################################################################
# VERSION
######################################################################

try:
    version = open("VERSION.txt").read()
except:
    version = open("../VERSION.txt").read()


######################################################################
# CLASSIFIER
######################################################################

classifiers = """\
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: POSIX :: Linux
Programming Language :: Python :: 2.7
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering
Topic :: System :: Clustering
Topic :: System :: Distributed Computing
"""

######################################################################
# VERSION CHECK
######################################################################

if sys.version_info < (2, 7):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

#DISTUTILS_DEBUG=1

######################################################################
# REQUIREMENTS
######################################################################

required_packages = ['setuptools','pip','docopt']

needed_packages = []

for package in required_packages:
    try:
        print "... trying import", package
        __import__(package)
        print "... package found"
    except ImportError:
        print "... needing import", package
        needed_packages.append(package)

print needed_packages

######################################################################
# SETUP
######################################################################

setup(
    install_requires = needed_packages,
    
    name='cmd3',
    version=version,
    description=doclines[0],
    long_description = "\n".join(doclines[2:]),
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='FutureGrid Eucalyptys Log File Analysis',
    author='Gregor von Laszewski',
    maintainer='Gregor von Laszewski',
    maintainer_email="laszewski@gmail.com",
    author_email='laszewski@gmail.com',
    url='https://github.com/futuregrid/cmd3',
    license='Apache 2.0',
    package_dir={'': 'src'},
    packages = find_packages('src'),

    include_package_data=True,
    zip_safe=False,

    package_data = {'cmd3': ['cmd3/plugins']},


    
    entry_points={
        'console_scripts':
            [
             'cm = cmd3.shell:main',
             ]},


    )
