def check_even_odd(x):

    #use if/else statement to check if the number is even od odd
    if x % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

#get user imput
num = int(input("enter a whole number: "))

# call the fucntion to run the program
check_even_odd(num)