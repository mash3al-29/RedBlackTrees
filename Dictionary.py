from RedBlackTree import RedBlackTree, RedBlackTreeNode


def load_dictionary():
    # file = open('Dictionary.txt', 'r')
    file = open('dictionary_small.txt', 'r')

    words = file.readlines()
    dictionary = RedBlackTree()

    for line in words:
        dictionary.insert(line.strip())

    return dictionary


def write_dictionary(dictionary: RedBlackTree):
    with open('dictionary_small.txt', 'w') as file:
        words = dictionary.get_all_elements()
        for i, word in enumerate(words):
            if i == len(words) - 1:
                file.write(word)
            else:
                file.write(word + '\n')


def insert_word(dictionary: RedBlackTree):
    word = input('Enter word:')
    if word.isalpha():
        node = dictionary.search_tree(word)
        if node is None:
            dictionary.insert(word)
            dictionary.print_tree_size()
            dictionary.print_black_height()
            dictionary.print_tree_height()
            write_dictionary(dictionary)
        else:
            print('ERROR: Word already in the dictionary')
            dictionary.print_tree_size()
            dictionary.print_black_height()
            dictionary.print_tree_height()
    else:
        print('word is not letters!')


def search_word(dictionary):
    word = input('Enter word:')
    node = dictionary.search_tree(word)
    if node is None:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    dictionary_ = load_dictionary()
    insert_word(dictionary_)
    search_word(dictionary_)
    # dictionary_.print_black_height()
