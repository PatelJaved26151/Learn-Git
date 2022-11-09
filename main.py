from fucntions import Board, Check
from turn import Turn 
import os

L_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# L_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# D_board = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

Board(L_board)

playing = True
Previous_turn = -1


while (playing):
    choice = input()
    if (choice == "q"):
        playing = False
    else:
       os.system('cls')
       choice = int(choice)
       choice -= 1
       Turn += 1
       if (Check(L_board)):
            Turn -= 1
            if(Turn % 2 == 0):
                print("Player O win the game!!!")
            else:
                print("Player X win the game")
       else: 
            if (Turn % 2 == 0):
                if(L_board == "O"):
                    print('bhara hua hai')
                    L_board[choice] = "O"
                    Board(L_board)
                    print("Player X turn's:\n")
                else:
                    L_board[choice] = "O"
                    Board(L_board)
                    print("Player X turn's:\n")
            elif (Turn == 9):
                Board(L_board)
                print("Draw")
                playing = False
            else:
                L_board[choice] = "X"
                Board(L_board)
                print("Player O turn's:\n")
