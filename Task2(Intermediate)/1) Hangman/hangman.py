from words import word_list
import random

def get_word():
    word = random.choice(word_list)
    return word.upper()


def game(word):
    letters_guessed = ''
    tries = 6

    print("the word you gotta guess is: ")
    print('_ ' * len(word))

    while tries > 0:
        guess = input("\ntry guessing a letter ").upper()
        
        if guess in letters_guessed:
            print("you have already guessed that letter! Try guessing another one")
            continue

        letters_guessed += guess

        if guess in word:
            print("WOAHHH you guessed a letter, try guessing more")
        else:
            tries -= 1
            print(f"you guessed a wrong letter, dont worry, you have {tries} tries left, try again, ")

        wrong_count = 0

        for i in word:
            if i in letters_guessed:
                print(i, end=' ')
            else:
                wrong_count += 1
                print('_ ', end=' ')
        
        if wrong_count == 0:
            print(f"\ncongratulationsssss!!!, you guessed the word: {word}")
            break
    else:
        print(f"\nsorry, you ran out of tries, the word was: {word}")


def main():
    word = get_word()
    game(word)


if __name__ == "__main__":
    main()