from random import randrange
import random

def user_num():
    a = input("Enter number between 1 and 10: ")
    return a
    
def ran_num():
    b = random.randint(1,10)
    return b

def compare_num():
    a = int(user_num())
    b = ran_num()
    print("User guess :",a)
    print("Random Number :",b)
    if a > b :
        print("User guess is too high")
    elif a < b:
        print("User guess is too low")
    else a==b:
        # print ("user guess is correct")
        


compare_num()

        

        
        
    

