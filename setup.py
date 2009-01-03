#!/usr/bin/env python

"""
Transform a YAML file into a LaTeX Beamer presentation.

Copyright (C) 2009 Arthur Koziel <arthur@arthurkoziel.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

setup(name='yml2tex',
      version='1.2',
      description='Transforms a YAML file into a LaTeX Beamer presentation',
      author='Arthur Koziel',
      author_email='arthur@arthurkoziel.com',
      url='http://code.google.com/p/yml2tex/',
      packages=['yml2tex'],
      scripts=['scripts/yml2tex'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          ],
     )