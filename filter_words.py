# generates a list of 5 letter words from /usr/share/dict/words

def main():
    filtered = set()
    with open("/usr/share/dict/words", 'r') as file:
        for line in file:
            word = line.strip().replace("'", '').lower()
            if len(word) == 5:
                filtered.add(word)

    print(f"{len(filtered)} 5 letter words found")
    filtered = list(filtered)
    filtered.sort()

    with open("./five_letter_words", 'w') as file:
        file.write('\n'.join(filtered))


if __name__ == "__main__":
    main()
