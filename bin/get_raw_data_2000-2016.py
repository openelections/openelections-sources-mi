# SOURCE: http://miboecfr.nictusa.com/cfr/presults/2016GEN.zip
#   note that the year can switch and we can iterate through 1998

import os, urllib, zipfile

# assume were in 'bin/'. move up.
dir = os.chdir('..')

# create new directory, download data
yrs = range(1998, 2018, 2)
base_url = "http://miboecfr.nictusa.com/cfr/presults/%dGEN.zip"

for i in yrs:
  #download zips
  filename = os.path.basename(base_url % i)
  print "downloading", base_url % i, "in directory %s" % os.getcwd()
  urllib.urlretrieve(base_url % i, filename)

  #extract, remove zips
  zip = zipfile.ZipFile(filename)
  zip.extractall('%d' % i)
  os.remove(filename)

print "...done"


