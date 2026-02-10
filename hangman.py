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

while True:
    word=""
    wordlist=[]
    guessedWord =[]
    mistakes = []
    lives = 0
    win = False
    
    word = input("Enter a word to be guessed: ")
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

    
