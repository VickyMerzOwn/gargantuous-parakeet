import random

def call(li):
	count=0
	for ele in li:
		if (ele[1]=="A") or (ele[1]=="K") or (ele[1]=="Q") or (ele[1]=="J"):
			count+=1
	return(count)

def botplay(cards,play):
	nums=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	playcard=""
	
	if len(play)==0:
		for card in cards:
			if playcard=="" or nums.index(card[1:])>nums.index(playcard[1:]):
				playcard=card
				

	else:

		for card in cards:

			if most_weighted(card,play,play[0]):
				playcard=card
				break

		if playcard=="":
			for card in cards:
				if card[0]==play[0][0] and playcard=="":
					playcard=card
				elif card[0]==play[0][0] and nums.index(card[1:])<nums.index(playcard[1:]):
					playcard=card

		if playcard=="":
			for card in cards:
				if playcard=="" or (card[0]!=play[0][0] and nums.index(card[1:])<nums.index(playcard[1:])):
					playcard=card



	play.append(playcard)
	cards.pop(cards.index(playcard))
	return play



def roundwinner(play):
	nums=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	winner=play[0]
	for p in play:
		if p[0]==play[0][0] and nums.index(p[1:])>nums.index(winner[1:]):
			winner=p

	return play.index(winner)


#I need a function that returns true if upon adding an element (argument) to a list(argument)
#the element is the most weighted element of the list.

def most_weighted(x,li,p):
	nums=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	if x[0]!=p[0]:
		return False
	else:
		for l in li:
			if l[0]==p[0] and nums.index(x[1:])<=nums.index(l[1:]):
				return False

		return True


def scorer(roundwins,calls):
	scores=[]
	for i in range(4):
		score=0
		x=calls[i]
		y=roundwins[i]
		if x>y:
			score=-10*x
		else:
			score=(10*x)+(y-x)
		scores.append(score)

	
		

	return

	 






suits=["S","C","H","D"]
numbers=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
cards=[]

for suit in suits:
	for number in numbers:
		cards.append(suit+number)
random.shuffle(cards)
#card distribution method may be changed to make more dynamic
bot1=cards[0:12]
bot2=cards[13:25]
bot3=cards[26:38]
player=cards[39:51]

#player order
order=[1,2,3,4]
random.shuffle(order)

playerCall=int(input("Call how many turns you can potentially win...").strip())
calls=[]
roundwins=[0,0,0,0]

calls.append(call(bot1))
calls.append(call(bot2))
calls.append(call(bot3))
calls.append(playerCall)

x=True
while x:
	choice=input("Would you like to continue ? \nEnter Yes or No.")
	
	if choice.lower()=="no" or len(player)==0:
		scorer(roundwins,calls)
		x=False
		break

	play=[]

	for o in order:
		if o==1:
			botplay(bot1,play)

		elif o==2:
			botplay(bot2,play)

		elif o==3:
			botplay(bot3,play)

		elif o==4:
			print("Available cards :",player)
			playcard=input("Which card would you like to play ?").strip()
			play.append(playcard)
			player.pop(player.index(playcard))



	i=order[roundwinner(play)]
	#roundwinner gives index of player that won the round wrt play
	#order matches the player with the shuffled list of players and i stores this index

	roundwins[i-1]+=1
