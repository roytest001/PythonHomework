#coding=utf-8
print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"
door = raw_input("> ")
if door == "1":
	print "There's giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear run away." % bear 

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins"
	print "3. Understanding revolvers yelling melodies."

	instanity = raw_input("> ")
	if instanity == "1" or instanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The instanity rots your eyes into pools of mucks. Good job!"
else:
	print "You sumble around and fall on a knife and die. Good job!"