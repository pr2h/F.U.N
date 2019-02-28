def hujambo():
    print('''
##################################################
# Tool    : hangman                              #
# Version : 1.0                                  #
# Runs on : Windows/ Linux                       #
# Source  : https://github.com/pr2h/             #
# Coded with Python 3                            #
##################################################
    ''')

import random
import sys
    
def filereader():
    try:
        filename = "game_list.txt"
        f = open(filename,'r')
        content = f.readlines()
        f.close()
    except:
        print('[!] ERROR: File "game_list.txt" not found\n[!] Create this file with the words you want to guess in this same folder\n[!] Enter each choice in each line in the file\n[*] Example (game_list.txt):\nchoice1\nchoice2\nchoice3\nand so on..')
        sys.exit()

    list_of_items = []
    # List of alphabets with space character
    alphabets = list("abcdefghijklmnopqrstuvwxyz ")
    
    for line in content:
        line = line.lstrip().rstrip().lower()
        
        if line.startswith('#'):
            continue
        elif line == "" or line == " ":
            continue

        flag = 0
        for character in line:
            if character not in alphabets:
                flag = 10
                break
            
        if flag == 0:
            list_of_items.append(line)

    if (list_of_items) == 0:
        print('[!] ERROR: File "game_list.txt" not in proper format\n[!] List is empty\n[!] Modify this file with the words you want to guess in this same folder\n[!] Enter each choice in each line in the file\n[*] Example (game_list.txt):\nchoice1\nchoice2\nchoice3\nand so on..')
        sys.exit()

    return list_of_items

def guess_game_main(word):
    word = word.lower()
    
    found_letter = []
    tried_letter = []
    count = 10
    wrong_answer = 0
    number_of_allowed_wrong_guesses = 7
    hangman_diagram = ["|---","|  |","|  O","| /|\\","|  |","|  /\\"]

    while count != 0 and wrong_answer < number_of_allowed_wrong_guesses:
        guess = "start"
        count = 0
        for letter in word:
            if letter == ' ':
                print(' ', end = "  ")
            elif letter in found_letter:
                print(letter, end = " ")
            else:
                print('_', end = " ")
                count+=1
        print('\n')
        
        while len(guess) != 1:
            guess = input('[*] Enter letter : ')
            guess = guess.lower()

        if guess in word:
            if guess in found_letter:
                print('[-] You already found this!\n')
            else:
                found_letter.append(guess)
                print('[+] Correct guess!\n')
        else:
            if guess in tried_letter:
                print('[-] You already tried this!')
            else:
                tried_letter.append(guess)
                
            wrong_answer+=1
            print('[-] Penalty number '+str(wrong_answer)+' / ' + str(number_of_allowed_wrong_guesses) + '\n')

            for i in range(1,wrong_answer):
                try:
                    print(hangman_diagram[i-1])
                except:
                    # In case number_of_allowed_wrong_guesses is set more than 7
                    pass
            print('\n')

    if wrong_answer != number_of_allowed_wrong_guesses:
        print('[+] Congrats! You beat the game!')

    else:
        print('[*] The correct answer was ' + word)
        print('[*] Better luck next time')

if __name__ == '__main__':
    hujambo()
    while True:
        words = filereader()
        word = random.choice(words)
        guess_game_main(word)
        print('\n\n[*] I had fun! Let\'s play again!')
