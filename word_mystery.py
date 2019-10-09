import random


def get_word(word_list):
    random_word = random.choice(word_list)
    word_length = len(random_word)
    print(word_length)
    print(random_word)
    return random_word
 
    
def make_list_from_text(words):
    list_of_words = words.split()
    return list_of_words


def read_file(filename):
    with open(filename) as words:
        text = words.read()
        return make_list_from_text(text)


    
get_word(read_file("words.txt"))

















