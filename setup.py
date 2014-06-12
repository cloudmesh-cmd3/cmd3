#!/usr/bin/env python
# -------------------------------------------------------------------------- #
# Copyright 2008-2010, Gregor von Laszewski                                  #
# Copyright 2010-2013, Indiana University                                    #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# -------------------------------------------------------------------------- #

import os
from setuptools import setup, find_packages
import cmd3

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    version=cmd3.__version__,
    name="cmd3",
    description="cmd3 - A dynamic CMD shell with plugins",
    long_description=read('README.rst'),
    license="Apache License, Version 2.0",
    author="Gregor von Laszewski",
    author_email="laszewski@gmail.com",
    url="https://github.com/cloudmesh/cmd3",
    classifiers=[
         "Intended Audience :: Developers",
         "Intended Audience :: Education",
         "Intended Audience :: Science/Research",
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: MacOS :: MacOS X",
         "Operating System :: POSIX :: Linux",
         "Programming Language :: Python :: 2.7",
         "Topic :: Scientific/Engineering",
         "Topic :: System :: Clustering",
         "Topic :: System :: Distributed Computing",
         "Topic :: Software Development :: Libraries :: Python Modules",
         "Environment :: Console"
         ],
    keywords="cmd commandshell plugins",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cm = cmd3.shell:main',
        ],
    }
 )

"""
import setuptools


setuptools.setup(
    setup_requires=[
        'd2to1',
        'pbr'
    ],
    d2to1=True
)
"""
