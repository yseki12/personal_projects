from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('      ' + '|' + '       ' + '|' + '          ')
    print('  ' + board[7]+ '   |   ' + board[8] + '   |   ' + board[9])
    print('      ' + '|' + '       ' + '|' + '          ')
    print('------------------------')
    print('      ' + '|' + '       ' + '|' + '          ')
    print('  ' + board[4]+ '   |   ' + board[5] + '   |   ' + board[6])
    print('      ' + '|' + '       ' + '|' + '          ')
    print('------------------------')
    print('      ' + '|' + '       ' + '|' + '          ')
    print('  ' + board[1]+ '   |   ' + board[2] + '   |   ' + board[3])
    print('      ' + '|' + '       ' + '|' + '          ')

def player_input():
    
    clear_output()
    marker = ' '
     
    while marker != "X" and marker != "O":
        marker = input("Player 1: Please Choose X or O: ")
        
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
        
    print(f"Player 1 is {player1}")
    print(f"Player 2 is {player2}")
        
    return (player1, player2)

def place_marker(board, marker, position):
    
    board[position] = marker


def win_check(board, mark):
    
    if (mark == board[1] == board[5] == board[9] or 
    mark == board[1] == board[2] == board[3]or 
    mark == board[4] == board[5] == board[6]or
    mark == board[7] == board[8] == board[9]or
    mark == board[1] == board[4] == board[7]or 
    mark == board[2] == board[5] == board[8]or
    mark == board[3] == board[6] == board[9]or
    mark == board[3] == board[5] == board[7]):
        return True


def choose_first():
    first = random.randint(1,2)
    
    if first == 1:
        return "Player1"
    else:
        return "Player2"

def space_check(board, position):
    
    if board[position] == ' ':
        return True


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True


def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Enter next position (1-9): "))
    
    return position

def replay():
    
    replay = ''
    
    while replay != 'yes' and replay != 'no' and replay != 'y' and replay != 'n':
        replay = input("Play Again? (y/n)").lower()
    
    if replay == "y" or replay == "yes":
        return True
    else:
        print("Thanks for Playing")
        return False


print('Welcome to Tic Tac Toe!')

###SETUP###
while True:
    
    board = [' '] * 10

    player1_marker, player2_marker = player_input()

    choose_first()

    turn = choose_first()

    print(turn + " will go first")

    play_game = input("Ready? (y/n)").lower()

    if play_game == "y" or play_game == 'yes':
        game_on = True
    else:
        game_on = False
    
    while game_on == True:
    
        if turn == "Player1":
            
            display_board(board)

            position = player_choice(board)

            place_marker(board,player1_marker,position)
        
            if win_check(board, player1_marker) == True:
                display_board(board)
                print("Player 1 has WON")
                game_on = False
        
            else:
                if full_board_check(board) == True:
                    display_board(board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player2"
        
        else:

            display_board(board)

            position = player_choice(board)

            place_marker(board,player2_marker,position)
        
            if win_check(board, player2_marker) == True:
                display_board(board)
                print("Player 2 has WON")
                game_on = False
        
            else:
                if full_board_check(board) == True:  
                    display_board(board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player1"

    if not replay():
        break
