print("You enter a dark room with two doors. Do you go through door 1 or door 2?")

door = input('> ')

if door == '1':
	print('There is a giant bear here eating a cake. What do you do?')
	print('1. Take the cake')
	print('2. Scream at the bear.')
	
	bear = input('> ')
	
	if bear == '1':
		print("The bear eats your face. Good Job")
	elif bear == '2':
		print("The bear eats your feet. GOod Job")
		
	else:
		print("Well, doing %s is probably better. Bear runs away" %bear)
		
elif door == "2":
	print("You stare into the endless abyss at Cthulu's retina")
	print("1. BLueberries")
	print("2. Yellow Jacket clothespins")
	print("3. Understanding revolvers yelling melodies")

	insanity = input("> ")
	
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by mind of Jello. GOod Job!")
	else:
		print("The insantity rots your eyes into a pool of muck. Good Job!")

else:
	print("You stumble around and fall on a knife and die. Good job!")
