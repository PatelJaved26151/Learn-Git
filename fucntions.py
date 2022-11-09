# from main import L_board
from turn import Turn 


# L_board = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
def Board(L_board):
    # D_board = [1,2,3,4,5,6,7,8,9]

    draw_board = (f"| {L_board[0]} | {L_board[1]} | {L_board[2]} |\n"
                  f"| {L_board[3]} | {L_board[4]} | {L_board[5]} |\n"
                  f"| {L_board[6]} | {L_board[7]} | {L_board[8]} |\n")
    print(draw_board)


# def Check(L_board):
#     if(L_board[0] == L_board[1] == L_board[2] == "X" or
#        L_board[3] == L_board[4] == L_board[5] == "X" or 
#        L_board[6] == L_board[7] == L_board[8] == "X" or
#        L_board[0] == L_board[3] == L_board[6] == "X" or
#        L_board[1] == L_board[4] == L_board[7] == "X" or
#        L_board[2] == L_board[5] == L_board[8] == "X" or
#        L_board[6] == L_board[4] == L_board[2] == "X" or
#        L_board[0] == L_board[4] == L_board[8] == "X" ):
#         Turn -= 1
#         return True
#     elif(L_board[0] == L_board[1] == L_board[2] == "O" or
#          L_board[3] == L_board[4] == L_board[5] == "O" or 
#          L_board[6] == L_board[7] == L_board[8] == "O" or
#          L_board[0] == L_board[3] == L_board[6] == "O" or
#          L_board[1] == L_board[4] == L_board[7] == "O" or
#          L_board[2] == L_board[5] == L_board[8] == "O" or
#          L_board[6] == L_board[4] == L_board[2] == "O" or
#          L_board[0] == L_board[4] == L_board[8] == "O"):
#          Turn -= 1
#          return True
#     else:
#         print("kuch toh gadbad hai daya")
def Check(L_board):
    if(L_board[0] == L_board[1] == L_board[2] == "X" or
       L_board[3] == L_board[4] == L_board[5] == "X" or 
       L_board[6] == L_board[7] == L_board[8] == "X" or
       L_board[0] == L_board[3] == L_board[6] == "X" or
       L_board[1] == L_board[4] == L_board[7] == "X" or
       L_board[2] == L_board[5] == L_board[8] == "X" or
       L_board[6] == L_board[4] == L_board[2] == "X" or
       L_board[0] == L_board[4] == L_board[8] == "X" or
       L_board[0] == L_board[1] == L_board[2] == "O" or
         L_board[3] == L_board[4] == L_board[5] == "O" or 
         L_board[6] == L_board[7] == L_board[8] == "O" or
         L_board[0] == L_board[3] == L_board[6] == "O" or
         L_board[1] == L_board[4] == L_board[7] == "O" or
         L_board[2] == L_board[5] == L_board[8] == "O" or
         L_board[6] == L_board[4] == L_board[2] == "O" or
         L_board[0] == L_board[4] == L_board[8] == "O"):
         Turn -= 1
         return True
    else:
        print("kuch toh gadbad hai daya")

    

    