def pathFinder(matrix,fr,fd,visited,r=0,d=0,path=""):
    if r==len(matrix[0]) or d ==len(matrix) or r<0 or d<0 or visited[r][d]==1:
        return
    if r==fr and d ==fd:
        print(path)
        return
    visited[r][d]=1
    
    move(matrix,fr,fd,visited,r+1,d,path," R ")
    move(matrix,fr,fd,visited,r+1,d+1,path," Drd ")
    move(matrix,fr,fd,visited,r,d+1,path," D ")
    move(matrix,fr,fd,visited,r-1,d+1,path," Dld ")
    move(matrix,fr,fd,visited,r-1,d,path," L ")
    move(matrix,fr,fd,visited,r-1,d-1,path," Uld ")
    move(matrix,fr,fd,visited,r,d-1,path," U ")
    move(matrix,fr,fd,visited,r+1,d-1,path," Urd ")

    visited[r][d]=0

def move(matrix,fr,fd,visited,r,d,path,dir):
    path+=dir
    pathFinder(matrix,fr,fd,visited,r,d,path)
    path = path[:-1]

matrix = [  ["start",2,  3],
            [   4  ,   5 ,"find"],
            [7,8,9]]
visited = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

pathFinder(matrix,2,1,visited)