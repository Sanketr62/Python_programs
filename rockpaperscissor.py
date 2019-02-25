import random
l=("r","p","s")
while True:
	#Take input from the the user
	u=input("enter your choice, press n to discontinue")
	#to exit
	if u=='n':
		print("game over")
		exit()
	#input from the computer
	c=random.choice(l)
	print("computer chooses",c)

	#compare the computer and the user choice
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		print("computer wins")

	if u=="r" and c=="s":
		print("you win")

	if u=="p" and c=="r":
		print("you win")

	if u=="p" and c=="s":
		print("computer wins")

	if u=="s" and c=="r":
		print("computer wins")

	if u=="s" and c=="p":
		print("you win")