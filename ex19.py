def cheese_and_crackers(cheese_count, cracker_count):
	print("You have %d cheese" %cheese_count)
	print("You have %d crackers" %cracker_count)
	print("Man that is enough for a party")
	print("Get a blanket")
	

print("We can give numbers to functions directly")
cheese_and_crackers(10,20)

print("OR, we can use variables from our script")
amount_of_cheese = 20
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too.")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)