
from typing import List
from letter_State import letterState
from wordle import Wordle
from colorama import Fore
import random


def main():
    print("Hello wordle")
    word_set = load_word_set("play_wordle.txt")
    secret = random.choice(list(word_set))

    wordle = Wordle(secret)

    while wordle.can_attempt:

        x = input("\nType ur guess: ")

        if (len(x)) != wordle.WORD_LENGTH:
            print(
                Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!! " + Fore.RESET)
            continue

        # if not x in word_set:
        #     print(
        #         Fore.RED + f"{x} is not a valid word, try again!! " + Fore.RESET)
        #     continue
        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:

        print(
            f"You have solved this puzzle in {6-wordle.remaining_attempts}  tries !!!")
    else:
        print("You failed to solve the puzzle.")
        print(f"The random word was {secret}")


def display_results(wordle: Wordle):
    print("\nYour results so far...\n")
    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        # print(f"{colored_result_str}")
        lines.append(colored_result_str)
    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join("_"*wordle.WORD_LENGTH))
    draw_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[letterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad*2
    top_border = "┌" + "─"*content_length + "┐"
    bottom_border = "└" + "─"*content_length + "┘"
    space = " "*pad
    print(top_border)
    for line in lines:
        print("│" + space+line+space+"│")
    print(bottom_border)


if __name__ == "__main__":
    main()
