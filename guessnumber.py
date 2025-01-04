import random
real_number = random.randint(1,50)
counter = 0
while True:
    guess_number = int(input("Guess the number, 1-50: "))
     


    if guess_number == real_number:
        print("Congratulations you won! ")
        counter += 1
        print(f"It took you {counter} tries")
        break

    elif guess_number < real_number:
        print("To low, try again!")
        counter += 1
    
    elif guess_number > real_number:
        print("To high, try again!")
        counter += 1

     