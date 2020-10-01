/*Use socket programming to make this game more interactive*/
import random
print("Welcome to the Rock,Paper and Scissor game")
print("Game rules")
print("Rock vs paper = Paper Wins")
print("Paper vs scissor = Scissor wins")
print("Rock vs scissor = Rock wins")

ans = input("To start the game press Y")
while ans == "Y" or ans == "y":
    print("Choose your choice")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    player_choice = int(input())
    while player_choice > 3 or player_choice <1:
        player_choice = int(input("Invalid choice"))

    if player_choice == 1:
        choice = "Rock"
    elif player_choice == 2:
        choice = "Paper"
    else:
        choice = "Scissor"
    print("Your Choice : "+choice)
    computer_choice = random.randint(1,3)
    while computer_choice == player_choice:
        computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_c = "Rock"
    elif computer_choice == 2:
        computer_c = "Paper"
    else:
        computer_c = "Scissor"
    print("My choice : "+computer_c)

    if (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1):
        result = "Paper"
    elif (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 2):
        result = "Scissor"
    else:
        result = "Rock"
    if choice == result:
        print("YOU WON")
    else:
        print("Hey looser!! YOU LOST")
    print("Want to play Again?")
    print("Press y for yes and n for no")
    ans = input()
    if ans == "NO" or ans == "no":
        break
print("Thanks for playing the game")
print("Good bye....")
