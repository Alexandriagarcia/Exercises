#Dictionary of Ma. Alexandria P. Garcia

Ages = {}


Ages['Alexis'] = 20
Ages['Alex'] = 22
Ages['Albert Jr.'] = 25
Ages['Merlyn'] = 54
Ages['Alberto'] = 59

if Ages.has_key('Alexis'):
    print "Alexis is in the dictionary. She is", \
Ages['Alexis'], "Years Old"

else:
    print "Alexis is not in the dictionary"


print "The following people are in the dictionary:"
print Ages.keys()


keys = Ages.keys()


print "People are aged the following:", \
Ages
values = Ages.values()


print keys
keys.sort()
print keys

print values
values.sort()
print values


print "The dictionary has", \
len(Ages), "entries in it"