print("Would you like to continue?")
answer = input()
if answer == "no" or answer == "n":
    print('Exiting')
elif answer == "yes" or answer == "y":
    print('Continuing ...')
    print('Complete!')
else:
    print("Please try again and respond with yes or no")

# x = 0;
# if not x:
#     print('Is empty!')
# else:
#     print("is " + str(x))