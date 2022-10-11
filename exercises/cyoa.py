"""EX6 Create your own advanture."""
__author__ = "730521912"


from random import randint


points: int = 0
player: str
CORRECT: str = "\U0001F7E9"
WRONG: str = "\U0001F7E8"
hero = ""
hint_index = 1
guess_count = 1
correct = 0


def greet() -> None:
    """Greeting the player."""
    global player 
    print("Welcome to the advanture to guess a superhero.")
    player = input("What is your name?")


def main() -> None:
    """The main function."""
    global points
    global player
    greet()
    option: str
    hero_list = ["Spiderman", "Ironman", "Batman", "Superman", "Captain America"]

    def guess():
        global guess_count
        global points
        global correct
        global hero
        if hero == "":
            print("You have to get a hint before you take a guess! You are directed to a hint.")
            hint(points)
        print(f"This is your guess {guess_count}/4")
        guess_count += 1
        if input("What is your guess?") == hero:
            correct += 1
            points += 10
            hero_list.remove(hero)
            if len(hero_list) > 1:
                print(f"{CORRECT} Good job {player}! You got {hero}! Now you can move on to guess another hero.")
                hero = ""
            else:
                print("Now you have guessed 4/5 heroes and now only {hero_list[0]} is left!")
        else:
            points += 3
            print(f"{WRONG}. Sorry {player}!Try again")
        return

    def hint(score: int) -> int:
        """Give hints of the character, up to three hints."""
        global hero
        global hint_index
        i: int = 1
        hero = hero_list[randint(0, len(hero_list) - 1)]
        finish: bool = False
        print(f"This is your hint {hint_index}/4.")
        hint_index += 1
        if hero == "Spiderman":
            while i < 4:
                if finish is not True:
                    if i == 1:
                        finish = input("The hero has different genes from normal human-beings. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 2:
                        finish = input("The hero accidentally gained his superpowers. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 3:
                        print("Last hint: The hero can cling to the wall with bare hands. The hero accidentally gained his superpowers. Go take a guess!")
                else:
                    return score + 8 - 2 * i
                i += 1
        if hero == "Ironman":
            while i < 4:
                if finish is not True:
                    if i == 1:
                        finish = input("The hero was not born with different genes from normal human-beings. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 2:
                        finish = input("The hero is very rich. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 3:
                        print("Last hint: The hero is a friend of Spiderman. Go take a guess!")
                else:
                    return score + 8 - 2 * i
                i += 1
        if hero == "Batman":
            while i < 4:
                if finish is not True:
                    if i == 1:
                        finish = input("The hero enhances his abilities through armor. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 2:
                        finish = input("The hero has advanced combat skills. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 3:
                        print("Last hint: The hero lost his parents when he was a child. Go take a guess!")
                else:
                    return score + 8 - 2 * i
        if hero == "Superman":
            while i < 4:
                if finish is not True:
                    if i == 1:
                        finish = input("The hero is extremly overpowered. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 2:
                        finish = input("The hero has one deadly weak point. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 3:
                        print("Last hint: The hero is not native to the earth. Go take a guess!")
                else:
                    return score + 8 - 2 * i
                i += 1
        if hero == "Captain America":
            while i < 4:
                if finish is not True:
                    if i == 1:
                        finish = input("The hero used to be very weak. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 2:
                        finish = input("The hero has great leadership skill. Do you what to take a guess now? Yes/No:") == "Yes"
                    elif i == 3:
                        print("Last hint: The hero's weapon is a shield. Go take a guess!")
                else:
                    return score + 8 - 2 * i
                i += 1
        return score + 8 - 2 * i
    
    while correct < 4 and hint_index <= 4 and guess_count <= 4:
        print(f"Hi {player}. Your job is to guess heroes from: {hero_list}.")
        option = input("Choose your option by inputing  a, b, or c. Where a -> hint, b -> guessing, c -> leaving:")
        if option == "a":
            points = hint(points)
        elif option == "b":
            guess()
        elif option == "c":
            print(f"Nice try! You got {correct} heroes right!")
            print(f"Game over! You scored {points}!")
            return
        else:
            print("Your input must be one of the character a, b, or c! Try again.")
    if correct == 4:
        print(f"Congratulations! {player}. You got all the heroes!")
    elif correct < 4:
        print(f"Nice try! You got {correct} heroes right!")
    print(f"Game over! You scored {points}!")
    

if __name__ == "__main__":
    main()