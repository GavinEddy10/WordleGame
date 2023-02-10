import random
from termcolor import colored
# need to install packages to run code with colored terminal
# to run, need to edit class run configurations:
# apply check mark next to emulate terminal in output code in edit configurations, to get colors


class Wordle:
    def __init__(self):
        self.winningWord = self.getGameWord().upper()
        self.guessList = []
        self.currentGuess = ""

    def validGuess(self, guess):
        if len(guess) < 5:
            return False
        else:
            for i in guess:
                if not i.isalpha():  # true if string
                    return False
            return True


    def getGameWord(self):
        wordList = ["trial", "widow", "bloat", "flirt", "crazy", "pinky", "hands", "ruled", "reset"]
        return wordList[random.randint(0, 8)]

    def strContainsChar(self, Letter, Guess):
        for letter in Guess:
            if Letter == letter:
                return True
        return False

    def getAllOrangeLetters(self):
        orangeLetters = []
        for Guess in self.guessList:
            for letter in Guess:
                letter = letter.upper()
                if self.strContainsChar(letter, self.winningWord):
                    orangeLetters.append(letter)
        return orangeLetters

    def getAllUsedLetters(self):
        usedletters = []
        for Guess in self.guessList:
            for letter in Guess:
                letter = letter.upper()
                usedletters.append(letter)
        return usedletters

    def getAllGreenLetters(self):
        greenletters = []
        for Guess in self.guessList:
            index = 0
            for letter in Guess:
                letter = letter.upper()
                if letter == self.winningWord[index: index + 1]:  # goes through each index of wining game word and guess letter same time
                    greenletters.append(letter)
                index += 1
        return greenletters

    def letterInList(self, list, letter):
        for Guess in list:
            if self.strContainsChar(letter, Guess):
                return True
        return False

    def printGameBoard(self):
        print()
        greenletters = self.getAllGreenLetters()
        orangeletters = self.getAllOrangeLetters()

        for Guess in self.guessList:
            i = 0  # index of letter during second for loop
            for curLetter in Guess:
                curLetter = curLetter.upper()

                if curLetter == Guess[4:5]:  # if last letter in word #needed to do with print next line
                    if curLetter == self.winningWord[i:i+1]:
                        print(colored(curLetter, 'green'))
                    elif self.letterInList(orangeletters,curLetter):
                        print(colored(curLetter, 'orange'))
                    else:
                        print(curLetter)
                else:
                    # self.letterInList(greenletters, curLetter)
                    if curLetter == self.winningWord[i:i+1]:
                        print(colored(curLetter, 'green') + " ", end="")
                        # works print("reached")
                    elif self.letterInList(orangeletters, curLetter):
                        print(colored(curLetter, 'yellow') + " ", end="")
                    else:
                        print(curLetter + " ", end="")
                i += 1
            print()

        for i in range(6 - len(self.guessList)):
            print("_ _ _ _ _")
        print()

    def isString(self): #returns
        if len(self.currentGuess) == 5:
            for i in self.currentGuess:
                if not i.isalpha():
                    return False
            return True
        return False

    def printLettersUsed(self):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z"]

        greenLetters = self.getAllGreenLetters()
        orangeLetters = self.getAllOrangeLetters()
        usedLetters = self.getAllUsedLetters()

        # print("green letters " + str(greenLetters))
        # print("orange letters " + str(orangeLetters))
        # print("guesses " + str(self.guessList))
        # print("used letters " + str(usedLetters))

        for letter in alphabet:
            if self.letterInList(greenLetters, letter):
                print(colored(letter, 'green') + " ", end="")
            elif self.letterInList(orangeLetters, letter):
                print(colored(letter, 'yellow') + " ", end="")
            elif self.letterInList(usedLetters, letter):
                print(colored(letter, 'light_grey') + " ", end="")
            else:
                print(letter + " ", end="")
        print()

    def runGame(self):
        # fix get green letters,
        print(
            "Welcome to Wordle. You win if you guess the 5 letter word in less than or equal to 6 tries. When a letter ")
        print(
            "lights up green, it means you guessed one of the correct letters in the correct spot. If a letter lights up ")
        print(
            "yellow, it means you guessed a correct letter but it is in the wrong spot. Printed below is an alphabet, ")
        print("helping show you what letters you've used, and which ones are correct and incorrect. ")

        self.printGameBoard()

        # game loop
        while len(self.guessList) < 6:
            self.currentGuess = input("What is your " + str(len(self.guessList) + 1) + " guess? ")
            while not self.validGuess(self.currentGuess):  # while string has nonletters/spaces
                print("Make sure you have no spaces, entered valid letters, and string is 5 characters long. ")
                self.currentGuess = input("What is your guess?")
            self.guessList.append(self.currentGuess)

            self.printGameBoard()
            self.printLettersUsed()

            if self.currentGuess.upper() == self.winningWord:
                print("WON")
                break

        if self.currentGuess == self.winningWord:
            print("You Guessed the correct word! Game Over")
        else:
            print("Game Over you didn't get the word. The word was; " + self.winningWord)


# main code
wordle = Wordle()
wordle.runGame()
