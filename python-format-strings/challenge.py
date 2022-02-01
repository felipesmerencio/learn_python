first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
# 5

# Second challenge


# Third challenge
# 16

print(f'{first_value.title().strip():>22}')
print(f'{second_value.capitalize().replace("-","").strip()}')
print(f'{third_value.replace(" ","").replace("-","").swapcase():>29}')

# Fourth challenge - use only the print() function (no f-strings)
#fourth_challenge = '{}#{}#{}!'.format(fourth_value,fifth_value,sixth_value)
#print(fourth_challenge)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')


# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
# temp_1 = '        {}'.format(fourth_value)
# temp_2 = '        {}'.format(fifth_value)
# temp_3 = '        {}'.format(sixth_value)
# print(temp_1)
# print(temp_2)
# print(temp_3)
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')