fahrenheit = input('What is the temperature in fahrenheit?')

if not (fahrenheit.isnumeric()):
    print('Input is not a number.')
    exit()
    
celsius = int((int(fahrenheit) - 32) * 5/9)
print('Temperature in celsies is ' + str(round(celsius)))