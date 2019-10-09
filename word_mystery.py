import random

# def handle_guess(word, board, guess):
#     while word.index(guess):
#         index = word.index(guess)
#         board[index] = guess
#         return board
        
def check_correct_guesses(correct_guesses, incorrect_guesses):
    letter = input('guess a letter ')
    if letter in word:
        correct_guesses.append(letter)
        print(correct_guesses)
    

  

def get_word(word_list):
    random_word = random.choice(word_list)
    word_length = (len(random_word) * ("_ "))
    print(word_length)
    #print(random_word)
    return random_word
     
def make_list_from_text(words):
    list_of_words = words.split()
    return list_of_words

def read_file(filename):
    with open(filename) as words:
        text = words.read()
        return make_list_from_text(text)

def playing_game(word):
    gameon = True
    correct_guesses = []
    incorrect_guesses = []
    while gameon and len(incorrect_guesses)<8:
        check_correct_guesses(word, correct_guesses, incorrect_guesses)

     
    
word = get_word(read_file("words.txt")) 
check_correct_guesses(word)


















