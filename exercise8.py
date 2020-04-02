#This is a program that prompts the user for a start and an end number.
#starting from the start number the program will count until it reaches the end number.

#Prompt the user for a number to start counting from.
count = int(input('Start from number: '))

#Prompt the user for a number to stop counting on.
result = int(input('Stop at number: '))

#Create a while statement that will count from the first variable to the second variable as long as the first variable is less than or equal to the second variable.
while count <= result:
    print (count)
    count = count + 1


