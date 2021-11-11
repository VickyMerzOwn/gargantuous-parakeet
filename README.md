# gargantuous-parakeet
A 4 player card game

There are a total of 52 cards distributed into four suits - spades, hearts, diamonds and clubs. Each set has 13 cards - 
[Ace, King, Queen, Joker, 10, 9, 8, 7, 6, 5, 4, 3, 2] arranged in the descending order of weightage i.e. “Ace” is the most powerful card whereas “2” is the least powerful one.
It would be a four player game where the user will be playing with three other computer simulated bots.

Steps of the game:

1. First, all the cards are distributed randomly to all four of the players.

2. The user can see only his/her cards.

3. Each player makes a “call” of how many turns they can potentially win. The bots place the “call” in the following simple manner - they check how many of “Ace”,  ”King”, ”Queen” and “Joker” cards they have from each suit and give those many “calls”. For instance, if a bot has the “Ace” and “King” of spades and “Queen” of hearts, then it would give “call” = 2+1=3. User can give calls as per his/her choice.

4. After “calls” are made, the game starts from a random player and goes in a clockwise fashion. The user can choose where to be placed in the circle.

5. If a bot is the first player to play in a turn - it will choose the highest weighted card it has and play it. If the user is the first player, he/she can choose any of his/her cards. 
Before playing the card, the user will be shown the cards he/she possesses at that point, from each suit.

6. For the next player onwards, if a bot is playing, it will choose a higher weighted card if available to it from the same suit, otherwise it will give the lowest weighted card from the same suit. If cards from that particular suit are not available, it will choose the lowest weighted card available to it, from any other suit. Example - if the player1 has played “King” of “Spades”, if the player2 has “Ace” of “Spades”, it will play it; otherwise it will play the lowest weighted card it has from “Spades”; if no “Spades” card is available to it, the lowest weighted card will be played.
If the user is playing, he/she can choose the card himself/herself.

7. After each turn is over, decide the winner as the player playing the highest weighted card of the suit the turn had begun with. The winner starts the next turn.
8. Continue the game until all cards are played.

9. Score the players as the following - if the player has given a “call” for winning x number of turns and actually won y number of turns - then, if x> y, score=-10x, otherwise, score=10x+(y-x)

10. Ask the user if he/she would like to continue. If the user wants to finish it, show the final scores.

