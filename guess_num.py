import random
print("guess the number")


while True:
    user=input("enter a to play and 'q' to exit: ")
    if user.lower()=="q":
        print("goodbye")
        break
    random_choice=random.randint(1,20)
    try:
        guess=int(input("enter the number you guessed (1-20) : "))
       
    except ValueError:
        print("enter a valid number")
        continue
        
    if abs(guess-random_choice)<=2:
            print("you won because you were close.. hurray","it was:",random_choice)
            break
    else:
        print("you lost it was :",random_choice)
    
        

    