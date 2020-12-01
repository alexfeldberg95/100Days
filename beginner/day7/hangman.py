import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def hangman():

	#generate random word

	
	end_of_game = False
	word_list = ["ardvark", "baboon", "camel"]
	chosen_word = random.choice(word_list)
	word_length = len(chosen_word)

	lives = 6 #one life per body part
	#Testing code
	# print(f'Pssst, the solution is {chosen_word}.')

	display = []
	for _ in chosen_word:
    	display.append("_")
    print(display)

	while not end_of_game:
  		guess = input("Guess a letter: ").lower()

  		#Check guessed letter
  		for position in range(word_length):
	    	letter = chosen_word[position]
	    	print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
	    	if letter == guess:
	        	display[position] = letter
	        else:
	        	print("Oh no! That letter is not in the word, you lose a life!")
	        	print(stages[lives])
	        	lives -= 1

  		print(display)

  	if lives > 0:
		print("Congratulations! You won!")
	else:
		print(f"Sorry, you lost! The word was: {chosen_word}")


hangman()




while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


