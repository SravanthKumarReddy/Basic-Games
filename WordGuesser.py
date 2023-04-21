from english_words import get_english_words_set
import random
web2lowerset = get_english_words_set(['web2'], lower=True)
web2lowerset = list(web2lowerset)
word_to_guess=random.choice(web2lowerset)

player_guess = input("Guess The correct word: ")
if player_guess == word_to_guess:
    print('Congratulations you have guess the word!!')
elif player_guess!= word_to_guess:
    print('Incorrect Guess. Try again')
    print(f"The first clue is that the word has {len(word_to_guess)} alphabtes")
    if input("Guess The correct word: ") == word_to_guess:
        print("Yes this is the correct Guess")
    else:
        print("Incorrect Guess")
        temp=''
        for i in word_to_guess[::2]:
            temp+=i+ '_'
        print(f"second clue is {temp}")
        if input("Guess The correct word: ") == word_to_guess:
            print("YOu have won")
        else:
            print("you lost and are out of attempts")
            print(f'The correct word is {word_to_guess}')
            

