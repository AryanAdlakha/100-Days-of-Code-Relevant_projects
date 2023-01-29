import random
import hangman_art
import word_list

print(hangman_art.logo)
chosen_word = random.choice(word_list.word_list)
#print(chosen_word)

display = []

for letter in chosen_word:
    display += "_"

lives = 6
end_of_game = False
while not end_of_game and lives != 0:
    guess = input("Enter a letter ").lower()
    if guess in display:
        print(f"You've already guessed letter {guess}")
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        lives = lives - 1
        print(f"The letter {guess} is not present in the word")
        print(hangman_art.stages[lives])

        if lives == 0:
            end_of_game = True
            print("You Lose")
    print(display)
    if '_' not in display:
        end_of_game = True
        print("Won")
