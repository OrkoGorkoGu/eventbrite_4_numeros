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

def progress_algorithm(num, bien, dig_list):
    x = num
    while True:
        cont_guessing = False
        x += 1
        if verify_numero(x):
            # Number is valid
            for dig in str(x):
                if dig not in dig_list:
                    # One of digit in x not found in dig_list
                    cont_guessing = True

            if not cont_guessing:
                # No unnecessary digits used
                if match(num, x)[0] == bien:
                    # this is an okay guess                    
                    return x

def verify_numero(num):    
    # Make sure number has no repeated digits
    return len(str(int(num))) == len(set(str(int(num)))) == 4

def generar_numero(dig_list):
    # Generate number for user to guess
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
        self.dig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

class PlayerGuess(Game):
    def __init__(self):
        Game.__init__(self)
        # Ensure the num is good:
        while True:
            self.num = generar_numero(self.dig_list)
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
    
    def turn(self):
        # Get user feedback
        fb = get_user_feedback(self.guess)

        # Update arrays based on user feedback
        if fb == [0,0]:
            # No numbers are regular, so none will be used
            for i in str(self.guess):
                self.dig_list.remove(i)
            
        elif fb[0] == 4:
            # Computer guessed number
            output("Thanks for playing!")
            self.is_playing = False
            
        # Use Algorithm to generate number
        if self.is_playing:
            self.guess = progress_algorithm(self.guess, fb[0], self.dig_list.copy())

def main():
    game = ComputerGuess()
    while game.is_playing:
        game.turn()
    
if __name__=="__main__":
    main()