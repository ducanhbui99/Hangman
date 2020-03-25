# Tyler Bui
import random

file = open("word_box.txt", "r")  # open the text file with each line contains each word
lst1 = file.readlines()  # create lst1 containing every words
file_len = len(lst1)  # length of lst1


def restart():  # restart?
    say = input('New game? (y or n) ')
    if say == 'y':
        answer = False
        run()
    else:
        answer = True
    return answer


def run():  # run function
    over = False  # set point over = false
    random_no = random.randint(0, file_len - 1)  # random number from 0 to file's length
    random_word = lst1[random_no]
    random_word= random_word.replace(' ', '')
    print(random_word)
    hidden_word = ''
    for i in range(len(lst1[random_no]) - 1):
        hidden_word += '_ '  # create a string which is a representation of the word
    a = hidden_word.split(' ')  # split the string into smaller bits and put them into a list
    lst2 = []  # create lst2 which contains all the guessed letters
    strike = 0  # how many times have the player guessed wrongly
    print('Welcome to HangMan. You will have the guess the hidden word, but you only have 5 chances to guess incorrectly, so guess wisely.')
    print(hidden_word)
    while not over:  # a loop
        check = False  # break point = false
        letter = input('Choose a letter: ')
        while len(letter) > 1:  # if the input letter has a length of bigger than 1 (not a letter)
            letter = input('Choose a letter dumbass ')
        while letter in lst2:  # if the input char is in lst2, player has to choose another letter
            letter = input('Choose another letter dumbass: ')
        lst2.append(letter)  # if the input char is not in lst2, add the char to lst2
        for i in range(len(a)):  # loop over a list to see if the guessed input is correct
            if lst1[random_no][i] == letter:
                check = True
                a[i] = letter
        sep = ' '
        hidden_word = sep.join(a)
        print(hidden_word)

        if '_' not in hidden_word:  # if all the characters are guessed, you win, ask to restart
            print('Congratulation! You Win!')
            over = restart()

        if check == False:  # if the input char is incorrect, strike increased by 1
            strike += 1
            print('Strike ' + str(strike))
            if strike == 5:  # if it is the 5th strike, game over, ask to restart
                print('BOOOO! Game Over!')
                over = restart()


run()
