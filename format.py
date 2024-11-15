# snack = '{} and {}'.format('Burger', 'Fries')
# print('\nReplaced:', snack)
# snack = '{1} and {0}'.format('Burger', 'Fries')
# print('Replaced:', snack)

# snack = '%s and %s' % ('Milk', 'Cookies')
# print('\nSubstituted:', snack)

string = 'coding for beginners in easy steps'

print('\nCapitalized:\t', string.capitalize())
print('\nTitled:\t\t', string.title())

print('\nCentered:\t', string.center(30, '*'))
print('\nUppercase:\t', string.upper())
print('\nSwapcase:\t', string.swapcase())
print('\nJoined:\t\t', string.join('**'))
print('\nJustified:\t\t', string.rjust(30, '*'))
print('\nReplaced:\t', string.replace('s', '*'))