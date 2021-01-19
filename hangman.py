# William Ikenna-Nwosu (wiknwo)
# 
# For this assignment, your mission is to write a 
# program that plays the game of Hangman
import random

def get_hangman_string():
    randnum = random.randint(0, 9)
    if randnum == 0:
        return "BUOY"
    elif randnum == 1:
        return "COMPUTER"
    elif randnum == 2:
        return "CONNOISSEUR"
    elif randnum == 3:
        return "DEHYDRATE"
    elif randnum == 4:
        return "FUZZY"
    elif randnum == 5:
        return "HUBBUB"
    elif randnum == 6:
        return "KEYHOLE"
    elif randnum == 7:
        return "QUAGMIRE"
    elif randnum == 8:
        return "SLITHER"
    elif randnum == 6:
        return "ZIRCON"
    elif randnum == 7:
        return "TRANSFORMATION"
    return "Error in random number generation"

def main():
    print('Welcome to Hangman!')
    userinputchar = ""
    hangmanstr = get_hangman_string()
    guesscount = len(hangmanstr) + 3
    guessedhangmanstr = ""
    winner = False
    

    # Generating guessed hangman string
    for i in range(0, len(hangmanstr)):
        guessedhangmanstr = guessedhangmanstr + "-"

    # Getting user's guess for hangman string
    while (guesscount != 0) and (not winner):
        
        # Word guessed correctly
        if(guessedhangmanstr == hangmanstr):
            winner = True
            break

        print("The word now looks like this: {}".format(guessedhangmanstr))
        print("You have {} guesses left.".format(guesscount))
        userinputchar = input("Your guess: ")
        guesscount = guesscount - 1

        # Check if character is in hangman string
        # and replace all occurence of guessed character
        # in the guessed hangman string if it is in
        # actual hangman string
        if userinputchar in hangmanstr:
            guessedhangmanstr = list(guessedhangmanstr) # Convert to list because strings in python don't support assignment
            for i in range(0, len(hangmanstr)):
                if hangmanstr[i] == userinputchar:
                    guessedhangmanstr[i] = userinputchar
            guessedhangmanstr = ''.join(guessedhangmanstr) # Convert back to string
            print("That guess is correct")
        else:
            print("There are no {}'s in the word".format(userinputchar))

    
    if not winner:
        print("You're completely hung.")
        print("The word was: {}".format(hangmanstr))
        print("You lose.")

    elif winner:
        print("You win.")

if __name__ == '__main__':
    main()