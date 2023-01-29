import random

def ManiRPS():
    player_score = 0
    computer_score = 0
    print("Welcome to ManiRPS!")
    print("1. Casual Mode")
    print("2. Ranked Mode")
    print("3. Quit")
    mode = input("Choose a mode: ")

    while mode != "3":
        if mode == "1":
            print("Casual Mode")
            print("Rock, paper, or scissors? (q to quit)")
            choice = input().lower()
            if choice == "q":
                mode = "3"
                continue
            elif choice == "rock":
                computer_choice = random.choice(["rock", "paper", "scissors"])
                print("Player chose " + choice + " and computer chose " + computer_choice + ".")
                if computer_choice == "rock":
                    print("Tie!")
                elif computer_choice == "paper":
                    print("Computer wins!")
                else:
                    print("Player wins!")
            elif choice == "paper":
                computer_choice = random.choice(["rock", "paper", "scissors"])
                print("Player chose " + choice + " and computer chose " + computer_choice + ".")
                if computer_choice == "rock":
                    print("Player wins!")
                elif computer_choice == "paper":
                    print("Tie!")
                else:
                    print("Computer wins!")
            elif choice == "scissors":
                computer_choice = random.choice(["rock", "paper", "scissors"])
                print("Player chose " + choice + " and computer chose " + computer_choice + ".")
                if computer_choice == "rock":
                    print("Computer wins!")
                elif computer_choice == "paper":
                    print("Player wins!")
                else:
                    print("Tie!")
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
            try_ranked = input("Do you want to try ranked mode? (y/n)").lower()
            if try_ranked == "y":
                mode = "2"
                player_score = 0
                computer_score = 0
                continue
            elif try_ranked == "n":
                play_again = input("Do you want to play again? (y/n)").lower()
                if play_again == "y":
                    continue
                elif play_again == "n":
                    mode = "3"
                else:
                    print("Invalid input. Please enter y or n.")
        elif mode == "2":
            print("Ranked Mode")
            print("Rock, paper, or scissors? (q to quit)")
            choice = input().lower()
            if choice == "q":
                mode = "3"
                continue
            elif choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                continue
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print("Player chose " + choice + " and computer chose " + computer_choice + ".")
            if computer_choice == choice:
                print("Tie!")
            elif (choice == "rock" and computer_choice == "scissors") or (choice == "scissors" and computer_choice == "paper") or (choice == "paper" and computer_choice == "rock"):
                print("Player wins!")
                player_score += 1
            else:
                print("Computer wins!")
                computer_score += 1
            print("Player: " + str(player_score) + "  Computer: " + str(computer_score))
            if player_score == 5:
                print("Player wins!")
                play_again = input("Do you want to play again? (y/n)").lower()
                if play_again == "y":
                    player_score = 0
                    computer_score = 0
                    continue
                elif play_again == "n":
                    mode = "3"
                else:
                    print("Invalid input. Please enter y or n.")
            elif computer_score == 5:
                print("Computer wins!")
                play_again = input("Do you want to play again? (y/n)").lower()
                if play_again == "y":
                    player_score = 0
                    computer_score = 0
                    continue
                elif play_again == "n":
                    mode = "3"
                else:
                    print("Invalid input. Please enter y or n.")
    print("Thanks for playing ManiRPS!")

ManiRPS()
