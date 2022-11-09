# from fucntions import Board, Check
# from turn import Turn 
# import os

# L_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # L_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# # D_board = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

# Board(L_board)

# playing = True
# Previous_turn = -1


# while (playing):
#     choice = input()
#     if (choice == "q"):
#         playing = False
#     else:
#        os.system('cls')
#        choice = int(choice)
#        choice -= 1
#        Turn += 1
#        if (Check(L_board)):
#             Turn -= 1
#             if(Turn % 2 == 0):
#                 print("Player O win the game!!!")
#             else:
#                 print("Player X win the game")
#        else: 
#             if (Turn % 2 == 0):
#                 if(L_board == "O"):
#                     print('bhara hua hai')
#                     L_board[choice] = "O"
#                     Board(L_board)
#                     print("Player X turn's:\n")
#                 else:
#                     L_board[choice] = "O"
#                     Board(L_board)
#                     print("Player X turn's:\n")
#             elif (Turn == 9):
#                 Board(L_board)
#                 print("Draw")
#                 playing = False
#             else:
#                 L_board[choice] = "X"
#                 Board(L_board)
#                 print("Player O turn's:\n")

import os

# spot = { 1:'1',2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
spot = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def draw(spot):
    game= (f"|{spot[0]}|{spot[1]}|{spot[2]}|\n"
           f"|{spot[3]}|{spot[4]}|{spot[5]}|\n"
           f"|{spot[6]}|{spot[7]}|{spot[8]}|\n")
    print(game)

playing = True
turn = 0



    



while playing:
    turn += 1
    draw(spot)
    
    if turn % 2 == 0:
        print("Player 2 turn's:")
    else:
        print("Player 1 turn's:")
        
    choice = input()
    
    
    if choice == "q": 
         print("Game Ended")
         playing = False
        
    elif str.isdigit(choice):
        if not spot[int(choice)] in {"X", "O"}:
            
            if turn % 2 == 0:
                spot[int(choice)] = "X"
            else:
                spot[int(choice)] = "O"
                
            def check(spot):
                
                    if turn == 9:
                        draw(spot)
                        print("Draw")
                        exit()
                        
                    if (spot[0] and spot[1] and spot[2] == 'X' or 'O') or (spot[3] and spot[4] and spot[5] == 'X' or 'O') or (spot[6] and spot[7] and spot[8] == 'X' or 'O') or (spot[0] and spot[3] and spot[6] == 'X' or 'O') or (spot[1] and spot[4] and spot[7] == 'X' or 'O') or (spot[2] and spot[5] and spot[8] == 'X' or 'O') or (spot[1-1] and spot[5-1] and spot[9-1] == 'X' or 'O') or (spot[3-1] and spot[5-1] and spot[7-1] == 'X' or 'O'):
                         previous = turn - 1
                         if previous % 2 == 0:
                             draw(spot)
                             print("Player O Wins")
                             exit()
                         else:
                              draw(spot)
                              print("Player X Wins")
                              exit()
                
            check(spot)
            os.system('cls')
           
    else:
        print("enter a number between 1-9")
