#Author: Aadam Ali

#The next few lines asks the user for inputs in order to start the game
playerOne = input("Please enter player one's name: ").lower()
playerTwo = input("Please enter player two's name: ").lower()

#The word is used as an array itself instead of having to create another array and storing it
word = str(input("Please enter the word you would like: "))

#This array keeps track of the letters that are already guessed like the traditional hangman game
guessedLetters = []
#This will display the length of word as blank spaces without showing any letters
blankWord = ['_']*len(word)

#This method allows the guessing player to guess letters
def checkWord():
    #this converts the word to a string so that it can be printed and shown
    letters = str(len(word))
    print ("The word is, " + letters + " letters long!")
    #Counters used below
    count = 0
    num = 0
    #prints the blank
    print(blankWord)
    #This loop allows 26 guesses because there are 26 letters in the alphabet
    while count <= 26:
        playerGuess = str(input("Please guess a letter: "))
        #This allows the player to quit when guessing
        midGameQuit(playerGuess)
        #appends the guessed letters to displayer to the guessing player
        guessedLetters.append(playerGuess)
        #Checks if the letter is in the word
        if playerGuess in word:
            print("The letter, " + playerGuess + " is in the word!")
            #This method is called to show where in the word the letter is
            showLetter(playerGuess)
            #If all letters are guessed correctly it calls this method
            youWon()
        else:
            if playerGuess not in word:
                num = num + 1
                #This method is called when the player guesses incorrectly
                youLose(num)
        print("The letters you have guessed are: " + str(guessedLetters))
        count = count + 1
    #exit after 26 guesses
    exit()

#@param playerGuess
#This method allows a player to quit whenever they want
def midGameQuit(playerGuess):
    if playerGuess == 'quit':
        exit()

#This method allows the players to quit within the first few inputs
def allowQuit():
    if word == "quit":
        exit()
    elif playerOne == "quit":
        exit()
    elif playerTwo == "quit":
        exit()

#@param playerGuess
#This method takes in one parametre in order show letters guessed correctly by player
def showLetter(playerGuess):
    #loops through the word
    for i in range(0, len(word)):
        #Checks if guess is in word
        if playerGuess == word[i]:
            #Inserts letter in the correct position in word
            blankWord[i] = playerGuess
    print(blankWord)

#This method checks to see if the word is complete
def youWon():
    count = 0
    for i in range(0, len(word)):
        #If there are blanks then count will not be 0
        if blankWord[i] == '_':
            count = count +1
    #If no blanks then the player wins
    if count == 0:
        print('Congratz you won the game!')
        exit()

#@param num
#This method will determine when a player loses the game
def youLose(num):
    #As num approches 6 it will show a man which is the traditional hangman game
    if num == 1:
        print("O")
    elif num == 2:
        print ("O\n" +
               "|")
    elif num == 3:
        print ( " O\n" +
               "\|")
    elif num == 4:
        print ( " O\n" +
               "\|/")
    elif num == 5:
        print ( " O\n" +
               "\|/\n" +
               "/")
    else:
        #When the number of incorrect guesses is 6 then you lose the game
        if num == 6:
            print (" O\n" +
                  "\|/\n" +
                   " /\.")
            print("Sorry you lost!")
            exit()

#Allows program to be run
def run():
    allowQuit()
    checkWord()
#runs the program
run()







