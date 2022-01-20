import random
import string


def find_all(string, char):
    """Find all indicies of char in string."""
    return [i for i, letter in enumerate(string) if letter == char]


def get_intial_guess(words):
    """Generate a reasonable first guess from a list of words."""
    while True:
        i = random.randrange(len(words))
        if len(words[i]) != len(set(words[i])):
            continue
        if 'e' not in words[i]:
            continue
        if 'o' not in words[i]:
            continue
        if 'r' not in words[i]:
            continue
        if 't' not in words[i]:
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

    guess = get_intial_guess(word_list)
    print("Initial guess:", guess)
    print(len(word_list), "possible options")

    for i in range(6):
        guess = input("Tried guess: ")
        grade = input("Grade for guess: ")

        assert len(guess) == 5 and len(grade) == 5

        word_list = filter_word_list(word_list, guess, grade)

        print(len(word_list))
        print(word_list[:10])


if __name__ == "__main__":
    main()
