''' Helper class for importing the words from words_alpha.txt into a list data structure to be manipulated by hangman.py'''

def main():
    WORD_FILE = 'words_alpha.txt'

    f = open(WORD_FILE, "r")

    list_of_words = f.read().splitlines()
    return list_of_words
    # list_of_words = list(f)
    # list_of_words.rstrip('\n')
    # print(list_of_words[0])
    # print(len(list_of_words))



if __name__ == '__main__':
    main()