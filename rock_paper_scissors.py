#!/usr/bin/env python2 
#the above is the path to the python intepreter

#I present to you: Rock, paper, scissors: THE VIDEO GAME

#random module determines what move the computer will throw
#time module is used to utilise dates and times
import random
import time

#sets each move to a specific number so that once slected it is 
#equated to a specific variable
rock = 1
paper = 2
scissors = 3

#specifying the rules of the game
names = { rock: 'Rock', paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock, scissors: paper }

#keeps track of scores 
player_score = 0
computer_score = 0


#greets the player 
#while loop is to allow the players to keep playing 
#as many times as the player wishes
def start():
    print 'Lets play a game of Rock, Paper, Scissors.'
    while game():
       #pass statement allows the while loop to stop once finished 
       pass
    scores()


#called upon by the start function
#determines the player move by calling upon the move() function
#passes the moves and stores them as intergers into the result function
def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again()


#put into a while loop
#used to obtain the an integer between one and three from the player
#player variable to b created from the player's input
#next are theinstructions given to the player \n adds a line break
def move():
    while True:
	print
	player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move")
        #try statement is used to clean up code and handle errors or exceptions
        try:
            player = int(player)
            #checks whether 1,2 or 3 are the moves
            if player in (1,2,3):
		return player
	except ValueError:
             pass
        print "oops! I didn't understand that. Please enter 1, 2 or 3."


#only takes the player and computer variables
#creates a countdown to the result
#sleep pauses the execution of the code in no. of secs
def result(player,computer):
    print "1..."
    time.sleep(1)
    print '2...'
    time.sleep(1)
    print "3!"
    time.sleep(0.5)
   
#prints out what the computer played
#looks up the numbers in the move() function then inserts it to where{0} is
print "Computer threw {0}".format(computer_score)

#calls the scores set earlier
#the global function allows the variable to be changed
#especially after having been appended by scores
global player_score, computer_score

#checks if the results are the same
if player_score == computer_score:
    print "tie game"	
#checks whether its a win or a loss
else:
    if rules[player] == computer:
        print "your victory has been assured!"
    else:
        print "the computer laughs as you realise you have been defeated!"
        computer_score += 1

#the play_again function
#just like the moe function hich asks user for input
def play_again():
    answer = raw_input("would you like to play again?  y/n: ")
    #checks to see what the response is
    if answer in ("y", "yes", "Yes", "Of course!"):
         return answer
    #we assume the player does not want to keep playing
    #prints a goodbye message and causes the game function not to restart
    else:
         print "Thank you very much for playing our game! See you next time!"

#after the game is over we move to the score function
#this code won't save the scores though
def scores():
    global player_score, computer_score
    print "High Scores"
    print "player ", player_score
    print "computer ", computer_score

#enables it to be run differently, ie either in the command line or importing it to another script
if __name__ == "__main__":
    start()
