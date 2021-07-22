#finding place where to n queens and conditions is
#1. no one attack each other
#2. only one in row
#3. only one in col
def nQueen(matrix,c,hashrow,hashdiag,hashdiagU):
    #terminate condition 
    if c==len(matrix[0]):
        print(matrix)
        return

    for i in range(len(matrix[0])):
        if issafe(i,c,matrix,hashrow,hashdiag,hashdiagU):
            matrix[i][c]=1
            hashrow[i]=1
            hashdiag[i+c]=1
            hashdiagU[len(matrix)-1+c-i]==1
            nQueen(matrix,c+1,hashrow,hashdiag,hashdiagU)
            matrix[i][c]=0
            hashdiagU[len(matrix)-1+c-i]==0
            hashdiag[i+c]=0
            hashrow[i]=0
    return


#we need to check only three diagonal becuause we start filling queen left to right
def issafe(row,col,matrix,hashrow,hashdiag,hashdiagU):
    if hashdiag[row+col]==1 or hashrow[row]==1 or hashdiagU[len(matrix)-1 + col -row]==1: return False
    return True

n=4
matrix= [[0 for j in range(n)] for i in range(n)]
hashrow = [0 for i in range(n)]
hashdiag = [0 for i in range(2*n-1)]
hashdiagU = [0 for i in range(2*n-1)]
nQueen(matrix,0,hashrow,hashdiag,hashdiagU)
