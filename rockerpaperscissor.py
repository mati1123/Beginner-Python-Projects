import random
computer_score = 0
player_score = 0
options = ["rock","paper","scissors"]
while True:
    player = input("Choose  rock, paper or scissors: ").lower()
    computer_choice = random.choice(options)

    print(f"You chose: {player}")
    
    print(f"Computer chose: {computer_choice}")

    if player == computer_choice:
        print(f"Both choose {player}. So it is a tie!")
    
    elif player == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            player_score += 1
        else:
            print("Paper covers rock! You lose!")
            computer_score += 1
    
    elif player == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            player_score += 1
        else:
            print("Scissors cuts paper! You lose!")
            computer_score += 1
    
    elif player == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            player_score += 1
        else:
            print("Rock smashes scissors! You lose!")
            computer_score += 1
    
    print(f"Current score - you: {player_score}, Computer: {computer_score} ")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f"Final score - You: {player_score}, Computer: {computer_score}")
        print("Thank you for playing! ")
        break




