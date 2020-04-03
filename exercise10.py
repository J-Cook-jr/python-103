# This program prints a star pattern square the size of the users choice.

# The following block of code prompts the user to enter a number and defines the first variable as a default variable.
row = int(input('Enter any number to define the size of your square: '))
r = 0

# The following line of code tells the program to loop through variable r as long as it's less than row.
while r < row:

    # This block defines the second variable as a default and tells the program to loop through the variable as long as its less than row.
    l = 0
    while l < row:

        # This block will run the second variable, adding it to an integer and printing out the * characters that will make up each row of the square.
        l = l + 1
        print('*' , end= '')

# This last block of code loops back to the first default variable, completing each row and column, ultimately  completing the square.
    r = r + 1
    print(' ')