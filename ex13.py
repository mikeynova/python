from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

question = raw_input('Your first answer was %r say something else: ' )

print "%r" % second

print question