#!/usr/bin/env python
import os
from distutils.core import setup
from distutils.command.clean import clean
from distutils.command.install import install
from distutils.dir_util import remove_tree


class InstallNdbUtils(install):
    def run(self):
        install.run(self)
        remove_tree('build')

setup(name='ndbutils',
      version='0.31',
      description="Helper functions for working with gae ndb.",
      py_modules=['ndbutils'],
      cmdclass={'install': InstallNdbUtils}
     )
