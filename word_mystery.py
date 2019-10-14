import random
import string



def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)

def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

# def display_letters(word, correct_guesses):
#     display_word = ""
#     for letter in word:
#         if letter in correct_guesses:
#             display_word += letter + " "
#         else:
#             display_word += " _ "
#     print(display_word) 

def entering_game():       
    permission = input("\n MYSTERY WORD  If you want to play, press 's', if not, press command + d: \n").lower()
    if permission == "s": 
        difficulty_level = input("\nPlease Select Level (e = easy, m = moderate, h = hard):\n").lower()
        if difficulty_level == "e":
            print("\nWelcome to the Easy Level\n")
        if difficulty_level == "m":
            print("\nWelcome to the Moderate Level\n")
        if difficulty_level == "h":
            print("\nWelcome to the Hard Level\n")
    else: 
        print(" Valid response required.")
    return difficulty_level  

def level_word(words, difficulty): 
    easy_mode = []
    moderate_mode = []
    hard_mode = []

    for word in words: 
        if len(word) >= 4 and len(word) <=6:
            easy_mode.append(word)
        elif len(word) > 6 and len(word) <=8:
            moderate_mode.append(word)
        elif len(word) > 8: 
            hard_mode.append(word)
    if difficulty == "e":
        index = random.randrange(len(easy_mode) + 1)
        return easy_mode        
    elif difficulty == "m":
        index = random.randrange(len(easy_mode) + 1)
        return moderate_mode  
    elif difficulty == "h":
        index = random.randrange(len(easy_mode) + 1)
        return hard_mode     
              
        
# def check_correct_guesses(word,correct_guesses, incorrect_guesses):
#     letter = input('guess a letter ')
#     if letter in word:
#         correct_guesses.append(letter)
#         print("You got it right")
            
#     else:
#         incorrect_guesses.append(letter)
#         print("That's a wrong answer")
#     display_letters(word, correct_guesses)    
#     return correct_guesses, incorrect_guesses
       
def get_words(word_list):
    random_word = random.choice(word_list).lower()
    word_length = ([" _ " * len(random_word)])
    print(word_length)
    print(random_word)
    return random_word
     
# def my_word_list(words):
#     list_of_words = words.split()
#     return list_of_words

# def read_file(filename):
#     with open(filename) as words:
#         text = words.read()
#         return my_word_list(text)

# def get_words(word_list):
#     random_word = random.choice(word_list).lower()
#     word_length = ([" _ " * len(random_word) ])
#     print(word_length)
#     print(random_word)
#     return random_word

def display_letters(word, correct_guesses):
    display_word = ""

    for letter in word:
        if letter in correct_guesses:
            display_word += letter + " " + " "
        else:
            display_word += " _ "
    print(display_word)         


def guess_letter(word, incorrect_guesses, correct_guesses, lives): 
    guessed_letter = input("Guess a letter:")
 
    if guessed_letter in string.punctuation:
        print("Needs to be a letter")
    elif guessed_letter in " ": 
        print("Needs to be a letter")    
    elif len(guessed_letter) >= 2: 
        print("Needs to be one letter")   
    elif guessed_letter in word: 
        correct_guesses.append(guessed_letter)
        print(f"Correct! {correct_guesses}")
    elif guessed_letter in incorrect_guesses: 
        print("You already guessed that letter. Try again.")
    else:
        incorrect_guesses.append(guessed_letter)
        lives -= 1
        print(f"Wrong answer! Try again!{incorrect_guesses}")
        print(f"You now have {lives} lives left.")
    display_letters(word, correct_guesses)   
    return correct_guesses, incorrect_guesses

def check_for_win(word, correct_guesses):
    for letter in word:
       if letter not in correct_guesses:
         return False        
    return True

def playing_game():
    gameon= True
    correct_guesses = []
    incorrect_guesses = []
    difficulty = entering_game()
    word = get_words(level_word(print_my_game("words.txt"), difficulty))
    lives = 8 
    
    while gameon and len(incorrect_guesses) < 8:
       guess_letter(word, correct_guesses, incorrect_guesses, lives)
       if check_for_win(word, correct_guesses):
               gameon = False
               print("You Won")
    print("Game Over")

   
    




playing_game()



















