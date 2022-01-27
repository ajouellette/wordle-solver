import random
import string


def find_all(string, char):
    """Find all indicies of char in string."""
    return [i for i, letter in enumerate(string) if letter == char]


def get_intial_guess(words):
    """Generate a reasonable first guess from a list of words.

    Word must have all unique letters, 3 most common vowels, and most common
    consonant.
    """
    while True:
        i = random.randrange(len(words))
        if len(words[i]) != len(set(words[i])):
            continue
        if 'e' not in words[i]:
            continue
        if 'i' not in words[i]:
            continue
        if 'a' not in words[i]:
            continue
        if 'r' not in words[i]:
            continue
        return words[i]


def score_guess(guess):
    """Score guess to sort list of potential guesses."""
    score = 0
    # 10 points for all unique letters
    if len(set(guess)) == len(guess):
        score += 10
    # score based on presence of frequent letters
    letters = "eariotnslcudpmhgbfywkvxzjq"
    for letter in guess:
        score += (26 - letters.index(letter)) / 10
    return score


def is_valid(word, guess, grade):
    """Check if a word is a valid next guess based on previous guess."""
    for i, letter in enumerate(guess):
        if grade[i] == 'g' and word[i] != letter:
            return False
        if grade[i] == 'b':
            g_inds = find_all(grade, 'g')
            g_lettrs = [guess[i] for i in g_inds]
            if letter in word and letter not in g_lettrs:
                return False
        if grade[i] == 'y':
            if letter not in word:
                return False
            elif word[i] == letter:
                return False
    return True


def filter_word_list(words, guess, grade):
    valid_words = []
    for word in words:
        if is_valid(word, guess, grade):
            valid_words.append(word)
    return valid_words


def main():
    #word_file = "5-letter-words.txt"
    word_file = "five_letter_words"
    with open(word_file, 'r') as file:
        word_list = file.read().splitlines()

    #guess = get_intial_guess(word_list)
    # probably better just to use "irate" as initial guess
    guess = "irate"
    print("Initial guess suggestion:", guess)
    print(len(word_list), "possible options")

    for i in range(6):
        while True:
            guess = input("Tried guess: ")
            grade = input("Grade for guess: ")
            if len(guess) != 5 or len(grade) != 5:
                print("The guess and it's score must be 5 letters long.")
                continue
            if not set(grade).issubset(set("gyb")):
                print("The score can only contain the letters g, y, or b.")
                continue
            break

        word_list = filter_word_list(word_list, guess, grade)

        if len(word_list) == 1:
            print("Found solution:", word_list[0])
            break
        elif len(word_list) == 0:
            print("Could not find a solution. Possibly missing word in input list.")
            break

        word_list.sort(key=score_guess, reverse=True)
        print(len(word_list), "possible next guesses")
        print(word_list[:12])


if __name__ == "__main__":
    main()
