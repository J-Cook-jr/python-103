#Print a 5 x 5 block of '*' characters.

#Define two variables: One variable tells the computer how many rows and the other will be a default variable.
row = int(5)
r = 0

#This line tells the computer to loop through the r variable as long as it's less than row.
while r < row:

#Define another variable: This variable will create your rows. This is also defined as a default variable.
    l = 0

#This line tells the computer to loop through the l variable as long as it's less than row and then it prints the * character.
    while l < row:
        l = l + 1
        print(' * ' , end = " ")


    r = r + 1
    print( " " )
        








