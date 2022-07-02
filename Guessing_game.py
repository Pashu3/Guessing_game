import random
number = random.randint(1,10)
player_name = input ('Name of the player: ')
for i in range (0,3):
    user = int(input("Guess the number between 1 to 10 : "))
    if user == number:
        print("Hurray !!")
        print(f"Mr/Ms/Mrs {player_name}...You have guessed the right number in {i+1} attempts and its {number}.")
        break
    elif user > number:
        print("the guess is greater than the number !! try again....")
    elif user < number:
        print("the guess is less than the number !! try again....")
