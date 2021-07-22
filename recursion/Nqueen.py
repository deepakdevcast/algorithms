#finding place where to n queens and conditions is
#1. no one attack each other
#2. only one in row
#3. only one in col
def nQueen(matrix,c):
    #terminate condition 
    if c==len(matrix[0]):
        print(matrix)
        return

    for i in range(len(matrix[0])):
        if issafe(i,c,matrix):
            matrix[i][c]=1
            nQueen(matrix,c+1)
            matrix[i][c]=0
    return


#we need to check only three becuause we start filling queen left to right
def issafe(row,col,matrix):
    #first direction: upper-left diagonal
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if matrix[i][j]==1: return False

    #second direction: column or left
    for i in range(col,-1,-1):
        if matrix[row][i]==1: return False

    #third direction: lower-left diagonal
    for i,j in zip(range(row,len(matrix)),range(col,-1,-1)):
        if matrix[row][i]==1: return False
    return True


matrix= [[0 for j in range(4)] for i in range(4)]
nQueen(matrix,0)