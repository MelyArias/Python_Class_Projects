#Name: Mely Arias

import random
import math

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")
print()

done=False
miles_traveled=0
thirst=0
camel_tiredness=0
native_dist_traveled=-20
drinks=3
chance = random.randrange(20)  #This is storing the chance of finding an oasis

while not done:                #This will loop as long as the user has not lost or has not quit the game
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    answer=input("Your choice? ")
    print()

    if answer.upper()=="Q":
        done=True

    elif answer.upper()=="E":
        print("Miles traveled:",miles_traveled)
        print("Drinks in Canteen:", drinks)
        print("The natives are",abs(miles_traveled-native_dist_traveled),"miles behind you" ) #This line is printing the difference of how far the natives are from the user
        print()
        
    elif answer.upper()=="D":
        camel_tiredness=0
        print("The camel is happy")
        random_num = random.randrange(10, 17)
        native_dist_traveled += random_num

    elif answer.upper()=="C":
        random_num = random.randrange(10,20) #stored a random number of miles in this variable
        miles_traveled += random_num
        print("You have traveled ",miles_traveled,"miles")
        thirst +=1
        camel_tiredness += random.randrange(1,3)
        native_dist_traveled += random.randrange(10,17)

    elif answer.upper()=="B":
        random_num = random.randrange(5,12)
        miles_traveled+=random_num
        print("You have traveled",miles_traveled,"miles")
        native_dist_traveled += random.randrange(10,17)

    elif answer.upper()=="A":
        if drinks>0:
            drinks=drinks-1
            thirst=0
        else:
            print("Error")

    if thirst>4 and thirst<6:
        print("You are thirsty")
    elif  thirst>6:
        print("You died of thirst!!")
        done=True

    if not done and camel_tiredness>5 and camel_tiredness<8:
        print("Your camel is getting tired")
    elif not done and camel_tiredness>8:
        print("Your camel is dead")

    if miles_traveled==native_dist_traveled or native_dist_traveled>miles_traveled:
        print("Sorry the natives have caught you")
        done = True
    elif miles_traveled-native_dist_traveled<15:
        print("The natives are getting close!!")

    if not done and chance == 7: #This is checking whether chance is equal to the random number.
        print("You have found an oasis") #This means that the user will have a 1 in 20 chance of finding the oasis.
        drinks += 1
        thirst = 0
        camel_tiredness = 0
    if not done and miles_traveled>=200:
        print("YOU WON!!!")
        done=True




