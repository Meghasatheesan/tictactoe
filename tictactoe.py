import numpy as np
print("this is a xo game between you and computer")
val=[]
for i in range(3):
    for j in range (3):
        val.append("_")
        print(end='')
    print("")
matrix=np.array(val).reshape(3,3)
def board():
    
    for row in matrix:
        print(" | ".join(row))
        print("-" * 6)

def game(player):
    while True:
        row= int(input("enter the row:"))
        col=int(input("enter the column: "))
        if row not in range(0,3) or col not in range (0,3):
            print('invalid input')
            continue
        elif matrix[row][col] !="_":
            print("occupied, try again")
            break
        else:
            matrix[row][col]= player
            break
def checkresult():
    for i in range(3):      
        if (matrix[i][0] == matrix[i][1] == matrix[i][2]) and matrix[i][1] in ['x','o']:
            print(f'{matrix[i][1]} wins')
            return True
    for j in range(3):
        if matrix[0][j] == matrix[1][j] == matrix[2][j] and matrix[0][j] in ['x','o']:
            print(f"{matrix[0][j]} wins")
            return True

  
    if matrix[1][1]==matrix[2][2]== matrix[0][0] and matrix[1][1] in ['x','o']:
        print(f"{matrix[1][1]} wins")
        return True
    

    if matrix[0][2]==matrix[1][1]==matrix[2][0] and matrix[1][1] in ['o','x']:
        print(f'{matrix[1][1]} win')
        return True
        
while True:
    for i in range(9):
        if i%2 ==0:
            game("x")           
        else:
            game("o")
        board()           
        if checkresult():
            print("thankyou for playing")
            break
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break

    



    
    
    
    




    
