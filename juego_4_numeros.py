import random

def output(text):
    print(text)

def match(x, y):
    # Compares two numbers, given as strings
    # Returns array with number of correct and regular digits
    bien = 0
    reg = 0

    for i in range(4):
        if str(x)[i] == str(y)[i]:
            bien += 1
        elif str(y)[i] in str(x):
            reg += 1
    
    return [bien, reg]

def progress_algorithm(guessList, fbList):    
    # set candidate to previous guess
    cand = 0

    while True:
        cand += 1
        if verify_numero(cand):
            # Number is valid
            if len(guessList) == 1:
                # llegamos a la segunda adivinanza
                while True:
                    cand += 1
                    if match(cand, guessList[0]) == [0,0] and verify_numero(cand):
                        return cand
            
            for idx in range(len(guessList)):
                # Compare with feedbacks from previous guesses too (checks validity of guess)
                if not (match(guessList[idx], cand) == fbList[idx]):
                    break
                elif idx == len(guessList) - 1:
                    # Reached end
                    # # this is an okay guess
                    return cand

def verify_numero(num):   
    # Make sure number has no repeated digits and is four digits
    return len(str(int(num))) == len(set(str(int(num)))) == 4

def generar_numero():
    # Generate number for user to guess
    dig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    num = ''

    for i in range(4):
        if i==0:
            # First digit cannot be zero
            while True:
                dig = dig_list[random.randint(0, len(dig_list) - 2)]
                if dig != 0:
                    break
        else:
            dig = dig_list[random.randint(0, len(dig_list) - 1)]
        num += dig 
        dig_list.remove(dig)
    
    return int(num)

def give_user_feedback(num, guess):
    m = match(num, guess)
    s = "Bien: %s\nRegular: %s" %(m[0], m[1])
    output(s)
    return m

def get_user_feedback(guess):
    s = 'Mi adivinanza es %s' %guess
    output(s)
    bien = int(input("Cuántos están bien?"))
    reg = int(input("Cuántos son regulares?"))
    return [bien, reg]

class Game():
    def __init__(self):
        self.is_playing = True       

class PlayerGuess(Game):
    def __init__(self):
        Game.__init__(self)
        # Ensure the num is good:
        while True:
            self.num = generar_numero()
            if verify_numero(self.num):
                break

    def user_input(self):
        # Ask user to make a guess
        s = "Enter a four-digit guess:"

        while True:            
            guess = input(s)
            if verify_numero(guess):
                break
        return guess

    def turn(self):
        guess = self.user_input()

        give_user_feedback(self.num, guess)

        if match(self.num, guess) == [4,0]:
            # User Guessed number
            output("You Win!")
            self.is_playing = False

class ComputerGuess(Game):
    def __init__(self):
        Game.__init__(self)
        # User thinks of number
        s = "Think of a four-digit number"
        output(s)

        self.guess = 1023
        self.guessList = []
        self.fbList = []
    
    def turn(self):
        # Get user feedback
        fb = get_user_feedback(self.guess)
        self.guessList.append(self.guess)
        self.fbList.append(fb)

        if fb[0] == 4:
            # Computer guessed number
            output("Thanks for playing!")
            self.is_playing = False
        
        # Use Algorithm to generate number
        if self.is_playing:
            self.guess = progress_algorithm(self.guessList, self.fbList)
            
def main():
    game = ComputerGuess()
    while game.is_playing:
        game.turn()
        
    game = PlayerGuess()
    while game.is_playing:
        game.turn()
    
if __name__=="__main__":
    main()