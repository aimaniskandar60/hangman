from words import words
import random
import string

def select_word():
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = select_word()
    used_letters = set()
    word_letters = set(word)
    letters = set(string.ascii_uppercase)
    lives = int(input("How many lives would you like: "))

    while lives <= 0:
        lives = int(input("How many lives would you like: "))

    print("Welcome to hangman!")

    # The game goes on as long as the user still hasn't gotten the word
    # and if they still have lives.
    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print(f"Lives left: {lives}")
        user_input = str(input("Guess a letter: ")).upper()
        if user_input in letters - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print("Incorrect guess! You lost a live.")
        elif user_input in used_letters:
            print("You've already used this letter. Try again.")
        else:
            print("Invalid character.")

    if lives > 0:
        print(f"You've successfully guessed the word: {word}")
    else:
        print(f"You ran out of lives. The word was: {word}")

if __name__ == '__main__':
    hangman()