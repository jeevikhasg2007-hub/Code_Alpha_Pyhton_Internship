import random

words = ["python", "apple", "school", "intern", "coding"]
word = random.choice(words)

guessed = []
attempts = 6
print("=== HANGMAN GAME ===")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")

    elif guess in word:
        guessed.append(guess)
        print("Correct!")

    else:
        guessed.append(guess)
        attempts -= 1
        print("Wrong! Remaining guesses:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("Correct word was:", word)
