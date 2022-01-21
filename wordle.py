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
    with open("five_letter_words", 'r') as file:
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

        print(len(word_list), "possible next guesses")
        print("random possible next guesses:")
        num = min(len(word_list), 10)
        print(random.sample(word_list, num))


if __name__ == "__main__":
    main()
