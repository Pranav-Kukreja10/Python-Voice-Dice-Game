#imports
from playsound import playsound
import random
import pyttsx3

print("""🎲✨ Welcome to the Ultimate Pig Dice Challenge! ✨🎲

You play with a single die and two or more players.
On your turn, roll the die as many times as you wish, adding up your rolls.
If you roll a 1, you lose all points for that turn and your turn ends.
At any time, you can 'hold'. The points you rolled that turn are added to your score.
First player to reach 100 points wins!
Good luck and have fun!
      """)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id) 
else:
    engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)
engine.setProperty('volume', 1.0)

intro_text = """
Welcome to the Pig Dice Game!
You play with a single die and two or more players.
On your turn, roll the die as many times as you wish, adding up your rolls.
If you roll a 1, you lose all points for that turn and your turn ends.
At any time, you can 'hold'. The points you rolled that turn are added to your score.
First player to reach 100 points wins!
Good luck and have fun!
"""

engine.say(intro_text)
engine.runAndWait()

def roll():
    # playsound('roll.wav')
    return random.randint(1, 6)

print("🎲✨ Welcome to the Ultimate Pig Dice Challenge! ✨🎲")
print("Who will snatch victory in this nerve-wracking game of luck and courage? 🤩\n")

# Input for number of players
while True:
    players = input("👥 How many brave souls are playing today? (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print(f"🙌 Awesome! {players} players will battle for glory!\n")
            break
        else:
            print("❗ Please enter a number between 2 and 4 only.")
    else:
        print("❗ Please enter a valid number!")

# Input player names
player_names = []
for i in range(players):
    while True:
        name = input(f"Enter name for Player {i + 1}: ").strip()
        if name:
            player_names.append(name)
            break
        else:
            print("Name can't be empty. Please enter a valid name.")

max_score = 100  
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        if player_scores[player_idx] >= max_score:
            continue  
        print(f"\n🕑 {player_names[player_idx]}, it’s your moment to shine!")
        print(f"🏆 Your Total Score: {player_scores[player_idx]}\n")
        current_score = 0
        while True:
            ask_roll = input(f"🎲 {player_names[player_idx]}, do you dare to roll the dice? (y/n): ")
            if ask_roll.lower() != "y":
                print("🛑 You decided to bank your points and live to roll another day!\n")
                break

            value = roll()

            if value == 1:
                print("💥 Oh no! You rolled a 1! Catastrophe! All your points this turn are lost!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"👍 Awesome! You rolled a {value}!")
                print(f"💰 Points this turn: {current_score}")

        player_scores[player_idx] += current_score
        print(f"💼 {player_names[player_idx]}, your updated total score: {player_scores[player_idx]}\n")
        print("---------------------------------------------------------")



# Game Over – announce the champion!
max_score_final = max(player_scores)
winning_idx = player_scores.index(max_score_final)

print("\n🥁🥁🥁 The drums roll as we announce our champion! 🥁🥁🥁")
playsound('rolls.wav')

import pyttsx3

run = pyttsx3.init()
sound= engine.getProperty('voices')
run.setProperty('voice', voices[1].id)
run.setProperty('rate', 185)
run.setProperty('volume', 1.0)
win_message = (
    f"Congratulations, {player_names[winning_idx]}! "
    f"You have conquered the game with an epic score of {max_score_final}! "
    "Thanks for playing the Ultimate Pig Dice Challenge!"
)

# Announce the winner via voice
run.say(win_message)
run.runAndWait()

print(f"🏅 {win_message}")
print("🌟 Thanks for playing the Ultimate Pig Dice Challenge! 🌟\n")


