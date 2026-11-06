# Dice_rolling_game

import random
while True:
   choice = input("Roll the dice (y/n): ").lower()

   if choice =='y':
    die1 = random.randint(2,5)
    die2 = random.randint(2,5)
    print(f"{die1},{die2}")

   elif choice == 'n':
    print("Thanks for playing!")
    break
   else:
    print("Invalid message!")