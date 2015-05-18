#!/usr/bin/env python
# ----------------------------------------------------------------------- #
# Copyright 2008-2010, Gregor von Laszewski                               #
# Copyright 2010-2013, Indiana University                                 #
# #
# Licensed under the Apache License, Version 2.0 (the "License"); you may #
# not use this file except in compliance with the License. You may obtain #
# a copy of the License at                                                #
#                                                                         #
# http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
# ------------------------------------------------------------------------#

version = "1.8.0"

from setuptools.command.test import test as TestCommand
from setuptools.command.install import install
import os
from setuptools import setup, find_packages
import shutil

try:
    from cloudmesh_base.util import banner
except:
    os.system("pip install cloudmesh_base")

from cloudmesh_base.util import banner    
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cloudmesh_base.util import auto_create_version
from cloudmesh_base.util import auto_create_requirements

banner("Installing Cmd3")

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


requirements = parse_requirements('requirements.txt')


auto_create_version("cmd3", version)

class SetupYaml(install):
    """Copies a cmd3 yaml file to ~/.cloudmesh."""

    description = __doc__

    def run(self):
        banner("Setup the cmd3.yaml file")

        cmd3_yaml = path_expand("~/.cloudmesh/cmd3.yaml")

        if os.path.isfile(cmd3_yaml):
            print ("ERROR: the file {0} already exists".format(cmd3_yaml))
            print
            print ("If you like to reinstall it, please remove the file")
        else:
            print ("Copy file:  {0} -> {1} ".format(path_expand("etc/cmd3.yaml"), cmd3_yaml))
            Shell.mkdir("~/.cloudmesh")

            shutil.copy("etc/cmd3.yaml", path_expand("~/.cloudmesh/cmd3.yaml"))



class UploadToPypi(install):
    """Upload the package to pypi. -- only for Maintainers."""

    description = __doc__

    def run(self):
        auto_create_version("cmd3", version)
        os.system("make clean")
        os.system("python setup.py install")
        os.system("python setup.py bdist_wheel")
        banner("Build Distribution")
        os.system("python setup.py sdist --format=bztar,zip upload")

class InstallBase(install):
    """Install the cmd3 package."""

    description = __doc__

    def run(self):
        banner("Install Cmd3")
        install.run(self)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


home = os.path.expanduser("~")

#home + '/.cloudmesh'
#print [ (home + '/.cloudmesh/' + d, [os.path.join(d, f) for f in files]) for d, folders, files in os.walk('etc')],
#sys.exit()

data_files= [ (home + '/.cloudmesh/' + d.lstrip('cmd3/'),
                [os.path.join(d, f) for f in files]) for d, folders, files in os.walk('cmd3/etc')]


import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('cmd3/etc'):
  for filename in fnmatch.filter(filenames, '*'):
    matches.append(os.path.join(root, filename).lstrip('cmd3/'))
data_dirs = matches

#
# Hack because for some reason requirements does not work
#
# os.system("pip install -r requirements.txt")

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)
    
setup(
    version=version,
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
    install_requires=requirements,
    include_package_data=True,
    data_files= data_files,
    package_data={'cmd3': data_dirs},
    entry_points={
        'console_scripts': [
            'cm = cmd3.shell:main',
            'cm-generate-command = cmd3.generate:generate',
        ],
    },
    tests_require=['tox'],
    cmdclass={
        'install': InstallBase,
        'yaml': SetupYaml,
        'pypi': UploadToPypi,
        'test': Tox
    },
)

