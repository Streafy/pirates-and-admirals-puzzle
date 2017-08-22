import os


boatOnTheRight = True
boatOnTheLeft = False
boatSide = ''

piratesOnTheRightSide = 3
piratesOnTheLeftSide = 0
admiralsOnTheRightSide = 3
admiralsOnTheLeftSide = 0

gameLog = []
isLogging = True

number = 0


def check_sides():
    if (piratesOnTheRightSide > admiralsOnTheRightSide) and (admiralsOnTheRightSide >= 1):
        return False
    if (piratesOnTheLeftSide > admiralsOnTheLeftSide) and (admiralsOnTheLeftSide >= 1):
        return False
    return True


def check_is_enough_units(side, admiral, pirate, num=0):
    if side == 'right':
        if admiral and pirate:
            if admiralsOnTheRightSide == 0 or piratesOnTheRightSide == 0:
                return False
        elif admiral:
            if admiralsOnTheRightSide < num:
                return False
        elif pirate:
            if piratesOnTheRightSide < num:
                return False
    elif side == 'left':
        if admiral and pirate:
            if admiralsOnTheLeftSide == 0 or piratesOnTheLeftSide == 0:
                return False
        elif admiral:
            if admiralsOnTheLeftSide < num:
                return False
        elif pirate:
            if piratesOnTheLeftSide < num:
                return False
    return True


def current_situation():
    os.system('clear')
    print('\tCurrent situation:\n')
    print('A' * admiralsOnTheLeftSide, 'P' * piratesOnTheLeftSide, '\___/' * int(boatOnTheLeft), '===================',
          '\___/' * int(boatOnTheRight), 'A' * admiralsOnTheRightSide, 'P' * piratesOnTheRightSide)


current_situation()

while (piratesOnTheLeftSide != 3 or admiralsOnTheLeftSide != 3) and check_sides():

    nextTurn = input('\nEnter the next command(type help for list of commands):  ')

    if nextTurn == 'a':
        try:
            number = int(input('Enter the number of admirals you want to transport:  '))
        except ValueError:
            os.system('clear')
            current_situation()
            print('Enter the correct value!')
            continue

        if number > 2 or number < 1:
            while number > 2 or number < 1:
                print('Enter the correct number!')
                number = int(input('Enter the number of admirals you want to transport:  '))

        if boatOnTheRight:
            boatOnTheRight = False
            boatOnTheLeft = True
            boatSide = 'right'
            if check_is_enough_units(boatSide, True, False, number):
                admiralsOnTheLeftSide += number
                admiralsOnTheRightSide -= number
            else:
                os.system('clear')
                current_situation()
                print('\nYou don\'t have enough admirals, please enter the correct number.')
                continue

        else:
            boatOnTheRight = True
            boatOnTheLeft = False
            boatSide = 'left'
            if check_is_enough_units(boatSide, True, False, number):
                admiralsOnTheLeftSide -= number
                admiralsOnTheRightSide += number
            else:
                os.system('clear')
                current_situation()
                print('\nYou don\'t have enough admirals, please enter the correct number.')
                continue
    elif nextTurn == 'p':
        try:
            number = int(input('Enter the number of pirates you want to transport:  '))
        except ValueError:
            os.system('clear')
            current_situation()
            print('\nEnter the correct value!')
            continue

        if number > 2 or number < 1:
            while number > 2 or number < 1:
                print('Enter the correct number')
                number = int(input('Enter the number of pirates you want to transport:  '))

        if boatOnTheRight:
            boatOnTheRight = False
            boatOnTheLeft = True
            boatSide = 'right'
            if check_is_enough_units(boatSide, False, True, number):
                piratesOnTheLeftSide += number
                piratesOnTheRightSide -= number
            else:
                os.system('clear')
                current_situation()
                print('\nYou don\'t have enough pirates, please enter the correct number.')
                continue

        else:
            boatOnTheRight = True
            boatOnTheLeft = False
            boatSide = 'left'
            if check_is_enough_units(boatSide, False, True, number):
                piratesOnTheLeftSide -= number
                piratesOnTheRightSide += number
            else:
                os.system('clear')
                current_situation()
                print('\nYou don\'t have enough pirates, please enter the correct number.')
                continue
    elif nextTurn == 'b':

        if boatOnTheRight:
            boatOnTheRight = False
            boatOnTheLeft = True
            boatSide = 'right'
            if check_is_enough_units(boatSide, True, True):
                admiralsOnTheLeftSide += 1
                admiralsOnTheRightSide -= 1
                piratesOnTheLeftSide += 1
                piratesOnTheRightSide -= 1
            else:
                os.system('clear')
                current_situation()
                print('\nYou don\'t have enough pirates or admirals, please enter the correct number.')
                continue

        else:
            boatOnTheRight = True
            boatOnTheLeft = False
            boatSide = 'left'
            if check_is_enough_units(boatSide, True, True):
                admiralsOnTheLeftSide -= 1
                admiralsOnTheRightSide += 1
                piratesOnTheLeftSide -= 1
                piratesOnTheRightSide += 1
            else:
                os.system('clear')
                current_situation()
                print('\nYou don\'t have enough pirates or admirals, please enter the correct number.')
                continue

    elif nextTurn == 'exit':
        exit()

    elif nextTurn == 'el':
        isLogging = True

    elif nextTurn == 'dl':
        isLogging = False

    elif nextTurn == 'wl':
        print('\n\tGame log:\n', *gameLog, '\n')
        wait = input()

    elif nextTurn == 'help':
        print('\n\tAvailable commands:\n', 'a - move admirals', 'p - move pirates', 'b - move admirals and pirates',
              'exit - close the program', 'el - enable logs', 'dl - disable logs', 'wl - print logs', sep='\n')
        wait = input('')

    if isLogging:
        if nextTurn == 'a' or nextTurn == 'p':
            nextLog = nextTurn + str(number)
            gameLog.append(nextLog)
        else:
            gameLog.append(nextTurn)

    current_situation()

if check_sides():
    print('\nYou win!')
else:
    print('\nYou lost...')

if isLogging:
    wl = input('\nDo you want to see game log?(y/n)  ')
    if wl.lower() == 'y' or wl.lower() == 'yes':
        print('\n\tGame log:\n', *gameLog, '\n')
