import urllib
import urllib.request

type(urllib)
type(urllib.request)

urllib.__path__   # C:\Users\mkozi\AppData\Local\Programs\Python\Python37-32\lib\urllib
urllib.request.__path__

import sys
sys.path  # list of directories python searches for modules
for path in sys.path:
  print(path)

import os
os.getcwd()

import path_test # folder not on sys.path
sys.path.append('01_OrganizingPrograms/not_searched')
import path_test # now is found
path_test.found()
## Can also use environment variable PYTHONPATH to set the list of paths searched by python
## see: https://docs.python.org/3.7/library/sys.html#sys.path

## Create a package - create a directory on sys.path than include a file named '__init__.py' in directory
import sys
sys.path.append('01_OrganizingPrograms')
# or sys.path.extend(['01_OrganizingPrograms'])
import reader
type(reader)
reader.__file__
reader.__path__


import sys
sys.path.extend(['01_OrganizingPrograms'])
# before adding Reader to __init__
import reader.reader
reader.reader.__file__
r = reader.reader.Reader('01_OrganizingPrograms/reader/reader.py')
r.read()
# after adding Reader to __init__
import reader
r = reader.Reader('01_OrganizingPrograms/reader/reader.py')
r.read()

import sys
sys.path.append('01_OrganizingPrograms')
import reader.compressed
type(reader.compressed)

import sys
sys.path.append('01_OrganizingPrograms')
import reader
import reader.compressed
import reader.compressed.gzipped
import reader.compressed.bzipped

import sys
sys.path.append('01_OrganizingPrograms')
import reader
import reader.compressed
import reader.compressed.gzipped
import reader.compressed.bzipped
 r = reader.reader.Reader('test.bz2')
 r.read()
 r.close()
 r = reader.reader.Reader('test.gz')

 import sys
 for mod in sys.modules.keys():
   print

from reader.compressed import *
locals()
for local in locals():
  print local
# should show 'bz2_opener', 'gz_opener'

# Namespace packages - PEP420: https://www.python.org/dev/peps/pep-0420/

# executable directories
#   pass a path to python: > python path1
#   add a __main__.py file to a directory (ie path1)
#     for example: >python reader_executable __main__.py
#   the directory passed on the command line is automatically added to the python path
# Executable zip files
#   python can read zipped files
#   for example:  01_OrganizingPrograms> python reader_executable.zip repl-script.py

# recommended project layout: https://app.pluralsight.com/player?course=python-beyond-basics&author=austin-bingham&name=python-beyond-basics-m01&clip=9&mode=live
#     or see coures zip file (python-beyond-basics.zip) section 02, file organizing-larger-programs-slides.pdf, slide 23

# Singletons
#   Since python modules are only executed once when imported, properties defined at the module level are singletons
#   See directory 'singleton'