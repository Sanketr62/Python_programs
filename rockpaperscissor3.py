import random
l=('r','p','s')
d={'r':'rock','p':'paper','s':'scissor'}
us=0
cs=0

while True:
	#Take input from the the user
	u=input("enter your choice, press n to discontinue")
	if u in d:
		print("user",d[u])
	#to exit
	if u=='n':
		print("game over")
		exit()
	#input from the computer
	c=random.choice(l)
	if c in d:
		print("computer chooses",d[c])
	#compare the computer and the user choice
	if u==c:
		us=us+1
		cs=cs+1
		print("its a tie, your score is",us)
		print("computer's score is",cs)
	elif u=="r" and c=="p":
		cs=cs+3
		print("computer wins,computer's score is",cs)

	if u=="r" and c=="s":
		us=us+3
		print("you win,your score is",us)

	if u=="p" and c=="r":
		us=us+3
		print("you win,your score is",us)

	if u=="p" and c=="s":
		cs=cs+3
		print("computer wins,computer's score is",cs)

	if u=="s" and c=="r":
		cs=cs+3
		print("computer wins,computer's score is",cs)

	if u=="s" and c=="p":
		us=us+3
		print("you win,your score is",us)