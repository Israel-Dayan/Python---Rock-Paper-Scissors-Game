from random import shuffle
# player1 picks rock or paper or scissors
def player1_choice():
    choice = input('player1 pick: rock \ paper \ scissors: \n')
    choice = choice.lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print('invalid input place your choice again')
        choice = input('player1 pick: rock \ paper \ scissors: \n')
    return choice
# player2 picks rock or paper or scissors
def player2_choice():
    choice = input('player2 pick: rock \ paper \ scissors: \n')
    choice = choice.lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print('invalid input place your choice again')
        choice = input('player2 pick: rock \ paper \ scissors: \n')
    return choice
# pc picks randomly rock paper or scissors
def pc_choice():
    list1 = ['rock', 'paper', 'scissors']
    shuffle(list1)
    print(f'pc choice: {list1[0]}')
    return list1[0]
# check wining player
def win_check(player, pc):
    if player == pc:
        return('tie')
    elif player == 'rock' and pc == 'scissors' or player == 'paper' and pc == 'rock' or player == 'scissors' and pc == 'paper':
        return('you won')
    elif player == 'rock' and pc == 'paper' or player == 'paper' and pc == 'scissors' or player == 'scissors' and pc == 'rock':
        return('you lost')


#this is the game running
#asking the player which mode he wants to play single or multi
play_the_game = input("what mode do you want to play: single player / multiplayer [1/2] ? \n")
while play_the_game not in ['1', '2']:
    print('invalid input place your choice again')
    play_the_game = input("what mode do you want to play: single player / multiplayer [1/2] ? \n")
if play_the_game == "1":
    #asking the player how many roundes he wants to play
    start_the_game = input("what mode do you want to play one round or three rounds [1/3] ? \n")
    while start_the_game not in ["1", "3"]:
        print('invalid input place your choice again')
        start_the_game = input("what mode do you want to play one round or three rounds [1/3] ? \n")
    if start_the_game == "1":
# this is the game running in single mode for one round
        game = 'y'
        while game == 'y' or game == 'Y':
            print(win_check(player1_choice(), pc_choice()))
            game = input('do you want to continue y \ n ? : \n')
            while game not in ['y', 'n', 'Y', 'N']:
                print('invalid input place your choice again')
                game = input('do you want to continue y \ n ? \n')
            while game == 'n' or game == 'N':
                print('thank you and good bye!!!')
                break
    elif start_the_game == "3":
    # this is the game running single mode for three rounds
        game = 'y'
        while game == 'y' or game == 'Y':
            win_count = 0
            lose_count = 0
            tie_count = 0
            for game in [1, 2, 3]:
                play = win_check(player1_choice(), pc_choice())
                if play == "you won":
                    win_count += 1
                elif play == "you lost":
                    lose_count += 1
                elif play == "tie":
                    tie_count += 1
            if win_count > lose_count:
                print('you won the game!!!')
            elif lose_count > win_count:
                print('you lost the game!!!')
            else:
                print('you tied')
            game = input('do you want to continue y \ n ? \n')
            while game not in ['y', 'n', 'Y', 'N']:
                print('invalid input place your choice again')
                game = input('do you want to continue y \ n ? \n ')
            while game == 'n' or game == 'N':
                print('thank you and good bye!!!')
                break
#this is the game in multiplayer mode
elif play_the_game == "2":
    start_the_game = input("what mode do you want to play one round or three rounds [1/3] ? \n")
    while start_the_game not in ["1", "3"]:
        print('invalid input place your choice again')
        start_the_game = input("what mode do you want to play one round or three rounds [1/3] ? \n")
    if start_the_game == "1":
        #this is multiplayer mode with one round
        game = 'y'
        while game == 'y' or game == 'Y':
            player1 = win_check(player1_choice(), player2_choice())
            if player1 == "you won":
                print("player1 won")
            elif player1 == "you lost":
                print("player2 won")
            else:
                print("you tied")
            game = input('do you want to continue y \ n ? \n')
            while game not in ['y', 'n', 'Y', 'N']:
                print('invalid input place your choice again')
                game = input('do you want to continue y \ n ? \n')
            while game == 'n' or game == 'N':
                print('thank you and good bye!!!')
                break
    elif start_the_game == "3":
        # this is multiplayer mode with three rounds
        game = 'y'
        while game == 'y' or game == 'Y':
            win_count = 0
            lose_count = 0
            tie_count = 0
            for game in [1, 2, 3]:
                play = win_check(player1_choice(), player2_choice())
                if play == "you won":
                    win_count += 1
                elif play == "you lost":
                    lose_count += 1
                elif play == "tie":
                    tie_count += 1
            if win_count > lose_count:
                print('player1 won the game!!!')
            elif lose_count > win_count:
                print('player2 won the game!!!')
            else:
                print('you tied')
            game = input('do you want to continue y \ n ? \n')
            while game not in ['y', 'n', 'Y', 'N']:
                print('invalid input place your choice again')
                game = input('do you want to continue y \ n ? \n')
            while game == 'n' or game == 'N':
                print('thank you and good bye!!!')
                break



