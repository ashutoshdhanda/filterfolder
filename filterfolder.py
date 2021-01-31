# make list of all names only

# delete every element in this list, that has come twice

# if the name does not have a copy, viz. if the name exists only once in the list, then put this name in another list

# add the extension jpg or png to each element of the list to get a 'to-delete-list'

# delete every file in the folder that falls in the 'to-delete-list'
import os
from os import listdir
from os.path import isfile, join

# Get absolute path
mypath = os.path.dirname(os.path.abspath(__file__))

# make list of all names only
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# separate filename and extension
filenames = []
for file in onlyfiles:
	a, b = os.path.splitext(file)
	print("file="+a)
	print("extension="+b)
	filenames.append(a)
#list all elements that have occured just once
newlist = set([x for x in filenames if filenames.count(x) == 1])

#remove the python script and classes file from deletion list.
pythonscript = "filterfodler"
datasetclasses = "classes"
newlist.remove(pythonscript)
newlist.remove(datasetclasses)
#append file-extension to every element and deleted it.
has = [s + ".jgp" for s in newlist]
for x in has:
	os.remove(x)