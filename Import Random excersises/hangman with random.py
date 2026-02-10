import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
randomwords = ['ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ']
while True:
    word=""
    wordlist=[]
    guessedWord =[]
    mistakes = []
    lives = 0
    win = False
    
    #word = input("Enter a word to be guessed: ")
    word = random.choice(randomwords)
    print("\n\n\n\n\n")
    word = word.upper()
    
    for letter in word:
        wordlist += letter
        if letter == " " or letter == "-":
            guessedWord += letter
        else:
            guessedWord += "_"
    while True:        
        print(HANGMANPICS[lives])
        if mistakes:
            print("Incorrect guesses:",", ".join(mistakes))
        print(" ".join(guessedWord))
        guess = input("Guess any letter: ").upper()
        if len(guess) == 1:
            if guess in mistakes or guess in guessedWord:
                print("You already guessed this character")
            elif guess in wordlist:
                
                for i in range(len(wordlist)):
                    if wordlist[i] == guess:
                        guessedWord.pop(i)
                        guessedWord.insert(i,guess)
            else:
                mistakes += guess
                lives += 1
        else:
            print("Invalid guess: enter only 1 character")
        if wordlist == guessedWord:
            print("Congrats you guessed the word correctly")
            break
        elif lives == 7:
            print("You ran out of guesses. \n The word was", word.upper())
            break
        
        
    if input("Would you like to play again?(y/n): ") == "n":
        break
    
