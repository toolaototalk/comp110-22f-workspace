"""Constructed Wordle ex."""
__author__ = "730521912"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(target: str, single_char: str) -> bool:
    """Return bool value whether the first str parameter contains the second single character."""
    assert len(single_char) == 1
    if single_char in target:
        return True
    else:
        return False
      
 
def emojified(guess: str, secret_word: str) -> str:
    """Emojify the result of the guess based on correctness."""
    assert len(guess) == len(secret_word)
    guessIndex = 0
    result = ""
    while guessIndex < len(secret_word):
        if guess[guessIndex] == secret_word[guessIndex]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret_word, guess[guessIndex]):
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        guessIndex = guessIndex + 1 
    return result


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess and continue prompting them until they provide a guess of the expected length."""
    word_input = input(f"Enter a {expected_length}character word: ")
    while len(word_input) != int(expected_length):
        word_input = input(f"That wasn't {expected_length} chars! Try again: ")
    return (word_input)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    turn: int = 1
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(5)
        result = emojified(guess, secret)
        print(result)
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()
