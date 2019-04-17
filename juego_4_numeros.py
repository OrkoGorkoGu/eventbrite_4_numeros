def match(x, y):
    # Compares two numbers, given as strings
    # Returns array with number of correct and regular digits
    bien = 0
    reg = 0

    for i in range(4):
        if x[i] == y[i]:
            bien += 1
        elif y[i] in x:
            reg += 1
    
    return [bien, reg]

def main():
    pass

if __name__=="main":
    main()