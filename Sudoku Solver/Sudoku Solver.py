# This method is used to read the text file containing the numbers separated by commas 
def loadboard():
    board = []
    fileHandle = open("Text.txt", "r")   
    tile = fileHandle.readlines()        #Reads the lines
    for line in range(len(tile)):        
        if line!= len(tile) - 1:
            tile[line]=tile[line][:-1]
            board.append(list(map(int,tile[line].split(","))))
        else:
            board.append(list(map(int,tile[line].split(","))))
    fileHandle.close()
    return board                      

#This method is used to find empty space and find possible solutions for it 
def findEmpty(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:    #If the row and col cell is empty return that cell
                return (i, j) #row, column
    return None               


#Method to check if a valid number can be entered in current cell
def valid(board, num, pos):
    
    row = pos[0]
    column = pos[1]
    


    #Checks through every col element except current cell, returns False if number is already present in column
    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False
    
    #Similarly for row
    for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False
    
    
    #9 blocks of 3x3 cells are divided, this checks whether a num is already present in the row or col
    startRowBox = row//3 
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False


    return True



#Function to print board whilst checking if Sudoku is completed or not 
def printBoard(board):
    
    if not findEmpty(board):
        print("Sudoku Complete")
    else:
        print("Not Completed")
    for i in range(len(board)):
        if i%3 == 0:
            print("-------------------")
            
        for j in range(len(board[0])):
            if j%3 == 0:
                print("\b|", end ="")
            
            print(str(board[i][j])+" ", end="")
        print("\b|")
    print("-------------------")


#Backtracking begins       
def solve(board):
    
    find = findEmpty(board)     #Finds an empty cell
    
    if not find:
        return True
    else:
        row, col = find
    

    #Recursive function 
    for i in range(1,10):
        if valid(board, i, find):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False
          
board = loadboard()         
solve(board)           
printBoard(board)      
    