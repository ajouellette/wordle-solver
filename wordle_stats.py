import random
import numpy as np
from wordle import find_all, is_valid, filter_word_list


def score_word(target, guess):
    score = ""
    for i in range(5):
        if target[i] == guess[i]:
            score += 'g'
        elif guess[i] in target:
            score += 'y'
        else:
            score += 'b'
    return score


def auto_play(words, target, start_guess, N=200):
    """Play wordle N times starting from given guess."""
    n_guesses = []
    for i in range(N):
        guess = start_guess
        word_list = words.copy()
        n = 0
        while True:
            score = score_word(target, guess)
            word_list = filter_word_list(word_list, guess, score)
            if len(words) == 0:
                n = -1
                break
            guess = random.choice(word_list)
            n += 1
            if target == guess:
                break
        n_guesses.append(n)
    return n_guesses


def main():
    with open("five_letter_words", 'r') as file:
        words = file.read().splitlines()

    target = "prick"
    guess = "irate"
    n_guesses = np.array(auto_play(words, target, guess))
    successes = n_guesses != -1
    print("200 games starting from guess", guess)
    print(np.sum(np.logical_not(successes)), "failures")
    print(np.mean(n_guesses[successes]), np.std(n_guesses[successes]))


if __name__ == "__main__":
    main()
