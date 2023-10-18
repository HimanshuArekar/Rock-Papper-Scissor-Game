import random


rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

invalid = ('''
   ___ _ __ _ __ ___  _ __
 / _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |
 \___|_|  |_|  \___/|_| ''')

game_on = True
while game_on:
    user = int(input("Enter the number for following,\n0 for 'rock'\n1 for 'paper'\n2 for 'scissor'\n Enter="))
    if user == 0:
        print("User choose rock ", rock)
    elif user == 1:
        print("User choose paper ", paper)
    elif user == 2:
        print("User choose scissors ", scissors)
    else:
        print("User choose invalid input", invalid)

    # logic for user
    list = [0, 1, 2]
    computer = random.choice(list)
    if computer == 0:
        print("computer choose rock ", rock)
    if computer == 1:
        print("computer choose paper ", paper)
    if computer == 2:
        print("computer choose scissors ", scissors)

    if user >=3 or user < 0:
        print("User choose invalid input, you lose the game 😭")
    elif user == 0 and computer == 2:
        print("You win the game 😍")
    elif user == 2 and computer == 0:
        print("You lose the game 😭")
    elif user > computer:
        print("You win the game 😍")
    elif computer > user:
        print("You lose the game 😭")
    elif computer == user:
        print("The game is draw🤜🤛")

    massage = input("Do you want to continue the game? type 'y' for 'yes' and 'n' for 'no'=  ").upper()
    if massage == "N":
        print("thank you for playing game")
        game_on = False



# method 2
# import  random
#
# rock = ('''
# rock
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''')
# paper = ("""
# paper
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)
#
# scissors = ("""
# scissors
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
#
# invalid = ('''
#   ___ _ __ _ __ ___  _ __
#  / _ \ '__| '__/ _ \| '__|
# |  __/ |  | | | (_) | |
#  \___|_|  |_|  \___/|_|
#  ''')
# # store image in on list
# game_image = [rock, paper, scissors]
# # enter the input from user
# user=int(input("What you want to chose?\n 0 for rock \n 1 for paper \n 2 for scissor\n= "))
# if user >= 3 or user < 0:
#     print("You enter the invalid input, you lose the game")
# else:
#     print("You choose:", game_image[user])
#     computer = random.randint(0, 2)
#     print("computer choose:", game_image[computer])
#     if user > computer:
#         print("You win the game")
#     elif user < computer:
#         print("you lose the game")
#     elif user == 0 and computer == 2:
#         print("You win the game")
#     elif user == 2 and computer == 0:
#         print("You lose the game")
#     elif user == computer:
#         print("The game is draw")
#
