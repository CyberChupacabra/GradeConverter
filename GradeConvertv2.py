#Program used to translate a grade given as a percentage, to a grade given as a letter
#Written by S. Zepeda

#Def global constants:
PERCENT = 1
FRACTION = 2
EXIT = 3

def main():
    #Set loop variable.
    Loop = 'y'
    while Loop == 'y' or 'Y':
        #Get user option
        option = getuser()
        #Set Letter
        Letter = ''
        #logic gate
        if option == PERCENT:
            G = Pcent()
            Letter = convert(G)
        elif option == FRACTION:
            G = Frac()
            Letter = convert(G)
        elif option == EXIT:
            exit()
        #Display results
        print(f'You got a(n) {Letter}.')
        Loop = input('Do you want to check another grade? (y/n): ')
        while Loop not in ['n', 'N', 'y', 'Y']:
            Loop = input('Do you want to check another grade? (y\n): ')
        if Loop in ['n', 'N']:
            exit()

def getuser():
    #Choose how grade is recieved
    print(f'Zepeda\s Grade Caluclator')
    print('-------------------------')
    print('What form is the grade?')
    print('1. As a percentage')
    print('2. As a point fraction')
    print('3. Terminate Program')
    #Get option
    try:
        choice = int(input('Enter Choice: '))
    #Trip validation loop in event of err value
    except ValueError:
        choice = 7
    #Validate choice
    while choice < PERCENT or choice > EXIT:
        choice = int(input('ERROR! Enter valid choice: '))
    #return variable
    return choice

def convert(G):
    #Logic Gate
    if 0 > G or 100 < G:
        LG is False
    elif G >= 100:
        return 'A+'
    elif 94 <= G <= 100:
        return 'A'
    elif 90 <= G <= 93:
        return 'A-'
    elif 87 <= G <= 89:
        return 'B+'
    elif 83 <= G <= 86:
        return 'B'
    elif 80 <= G <= 82:
        return 'B-'
    elif 77 <= G <= 79:
        return 'C+'
    elif 73 <= G <= 76:
        return 'C'
    elif 70 <= G <= 72:
        return 'C-'
    elif 67 <= G <= 69:
        return 'D+'
    elif 63 <= G <= 66:
        return 'D'
    elif 60 <= G <= 62:
        return 'D-'
    elif 59 >= G:
        return 'F'

def Pcent():
    #Get info
    G = float(input('What percentage did you recive?: '))
    #Return Grade
    return G

def Frac():
    #Get info
    Fn = float(input('How many points did you recive?: '))
    Fd = float(input('How many points total?: '))
    #Perform division
    G = (Fn / Fd) * 100
    #Return Grade
    return G

#Call main function
main()
