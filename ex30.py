people = 30
cars = 40
trucks = 15

if cars > people:
	"""Would Print"""
	print "We should take the cars."
elif cars < people:
	"""Won't print"""
	print "We should not take the cars."
else:
	"""Whon't print"""
	print "We can't decide"

if trucks > cars:
	"""Won't print"""
	print "That's too many trucks."
elif trucks < cars:
	"""Would print"""
	print "Maybe we could take the trucks."
else:
	"""Won't print"""
	print "We still can't decide."

if people > trucks:
	"""Would print"""
	print "Alright, lets just take the trucks."
else: 
	"""Won't print"""
	print "Fine, let's stay home then.s"