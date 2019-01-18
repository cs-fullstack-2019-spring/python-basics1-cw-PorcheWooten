
def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()



# Create a function with two variables.
# One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.


def problem1():
    name1= "My name is:"
    name2 = "Chey"
    print(name1, name2)


# Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.
def problem2():
    exCred= int(input("Enter earned extra credit "))
    if (exCred<5):
            print("That's not enough extra credit")
    elif (exCred>20):
        print("That's too much extra credit")



# Create a function to ask a user to enter a password.
# Enter a password. Ask user to reenter password.
# Check to see if they are correct.
def problem3():
    userPW= input("Enter a password ")
    userPW2= input("Reenter password ")
    if(userPW == userPW2):
        print("CORRECT")
    else:
        print("Try Again!!")


# Create a function to ask for two card numbers.
# If it equals 21 print BLACKJACK!,
# if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”

def problem4():
    card1= int(input("Enter card 1 numbers "))
    card2= int(input("Enter card 1 numbers "))
    cards= card1 + card2
    if(cards == 21):
        print("BLACKJACK!!")
    elif(cards>21):
        print("BUST!!")
    elif(cards<21):
        print("The total is " + str(cards))

if __name__ == '__main__':
    main()
