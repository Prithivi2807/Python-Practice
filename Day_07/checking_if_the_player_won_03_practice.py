#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += ["_"]
print(display)
#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all
#  the letters in the chosen_word and 'display' has no more 
# blanks ("_"). Then you can tell the user they've won.

# guess = input("Guess a letter: ").lower()
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            # print(guess)
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")


print()
print(display)