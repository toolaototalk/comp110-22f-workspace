"""One shot wordle exercise."""
__author__ = "730521912"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guessIndex = 0
secret_word = "python"
result = ""
guess = input(f"What is your {len(secret_word)}-letter guess?")
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again:")

while guessIndex < len(secret_word):
    if guess[guessIndex] == secret_word[guessIndex]:
        result = result + GREEN_BOX
    else:
        in_the_word = False
        index = 0
        while (not in_the_word) & (index < len(secret_word)):
            in_the_word = guess[guessIndex] == secret_word[index]
            index = index + 1
            if in_the_word:
                result = result + YELLOW_BOX
        if (not in_the_word):
            result = result + WHITE_BOX
    guessIndex = guessIndex + 1 

if guess == secret_word:
    print(result + "\n" + "Woo! You got it!")
else:
    print(result + "\n" + "Not quite. Play again soon!")