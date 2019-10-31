# -*- coding: utf-8 -*-
# serial replace
import re
import sys
import os
import string
from collections import OrderedDict
# print "got " + str(sys.argv)
manual=False
manual = True

path = "./"
filename = "replace-input.txt"
# expand and join path and filename
fileandpath = os.path.join(os.path.expanduser(path), filename)
fileobj = open(fileandpath, 'r') # open for reading
lines = fileobj.readlines() # read all lines into array
fileobj.close()

# clean nobreaking space
printable = set(string.printable)
out = []
for l in lines:
  a = l.decode("utf-8").replace(u"\xc2", "").replace(u"\xa0", " ").encode("utf-8")
  if not a == '\n': out.append(a)
lines = out


if (manual):
  fileobj = open(filename, 'w') # open for writing
  fileobj.write(''.join(lines))
  fileobj.close()
  #print ''.join(lines) # for manual editing
  #print
  #print '###############'
  #print

p0 = (r'\n\n', '\n') # double newline
p1 = (r'[ 0-9]+ $', '') # page number at end
p2 = (r'[0-9]+\.', '#') # first level
p3 = (r'[0-9]+[a-z]+\.*', '##') # second level
p4 = (r'^\(.\)', '###') # third level


leveldict = OrderedDict([p1, p2, p3, p4]) #, p4:''}


lst = lines
for key in leveldict.keys():
  lst = map(lambda x: re.sub(key, leveldict[key], x), lst)

if not manual:
  print "'''Topics'''"
  print ''.join(lst)
  print

