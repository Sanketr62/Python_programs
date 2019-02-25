import random

p = 0
d = 0
snl = {9:23,4:55,6:26,56:5,66:20,34:1,76:92,55:78,80:99,14:51,19:29,12:4}
def rolldice():
		return random.randint(1,6)

#Get 1 or 6 on the dice to enter the game.
while True:
	r = input("Pres r to roll the dice,q to quit : ")
	if r == 'r':
		d = rolldice()
		print("You got",d)

		if d == 6 or d == 1:
			print("Congratulatons, you're in the game!")
			break
		else:
			print("you need to get 1 or 6 to the start the game. Try again.")
	elif r == 'q':
		exit()
while True:
	r = input("press r to roll, q to quit :")
	if r == 'r':
		d = rolldice()
		print("you got",d)
		p = p + d
		if p == 100:
			print("Hurray! you won!")
			exit()
		if p > 100:
			p = p - d
			print("you need to get", 100-p,"to reach home.")
		print("your new position is",p)
		if p in snl:
			if p < snl[p]:
				print("wow you got a ladder.")
			else:
				print("Oooops, you got swallowd by a huge snake.")

			p = snl[p]
			print("move to",p)
	elif r == 'q':
			exit()