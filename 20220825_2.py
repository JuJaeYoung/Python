hours = int(input('Enter Hours: '))
rates = int(input('Enter Rate: '))

if hours > 40:
    overhours = hours - 40
    print(' ')
    print('Base Pay:',40 * rates)
    print('Bonus Pay:',overhours * rates * 1.5)
    print('Pay:',40 * rates + overhours * rates * 1.5)
else:
    print('Pay:',hours * rates)
