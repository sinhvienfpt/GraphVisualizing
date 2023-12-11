

#Fucntion that make a adjacency list from a edgelist
def adjacencyMatrix_to_edgeList(path_adjacencyMatrix,path_output="./output.txt"):
    file_inp = open(path_adjacencyMatrix,'r')
    matrix = []
    for line in file_inp :
        matrix.append(line.split())
    
    file_out = open(path_output,"w")
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            #The condition i<j to make sure that we don't write the same
            #Edge ex 1 4 and 4 1 
            if matrix[i][j] == '1' and i < j :
                file_out.writelines(f"{i}  {j} \n")
       
                
#Function convert adjacency matrix to list
def adjacencyMatrix_to_adjacencyList(path_adjacencyMatrix,path_output="./output.txt"):
    file_inp = open(path_adjacencyMatrix,'r')
    matrix = []
    for line in file_inp :
        matrix.append(line.split())
    
    #Make a list to save all the adjacency
    list = [0,]
    size = len(matrix)
    for i in range(1,size):
        a = []
        for j in range(1,size):
            if matrix[i][j] == '1' :
                a.append(j)
        list.append(a)
    
    #Write the result in file output
    file_out = open(path_output,'w')
    for i in range(1,size):
        list[i] = map(str,list[i])
        res = str(i) + " : " + ",".join(list[i]) + "\n"
        file_out.write(res)


#Function convert edglist to matrix
def edgeList_to_adjacencyMatrix(path_edgeList,path_output="./output.txt"):
    file_inp = open(path_edgeList,'r')
    #Read file edge list and save it to matrix
    n,m = map(int,file_inp.readline().split())
    arr = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,file_inp.readline().split())
        arr[a][b] = 1
        arr[b][a] = 1
    #Write matrix in output
    file_out = open(path_output,'w')
    result = "\n".join((" ".join(map(str,row)) for row in arr))
    file_out.write(result)
   
    
#Function convert edge list to adjacency list
def edgeList_to_adjacencyList(path_edgeList,path_output="./output.txt"):
    file_inp = open(path_edgeList,'r')
    n,m = map(int,file_inp.readline().split())
    arr = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,file_inp.readline().split())
        arr[a].append(b)
        arr[b].append(a)
    
    
    file_out = open(path_output,'w')
    res = ""
    for i in range(1,n+1):
        res +=  str(i) + " : " + " ".join(map(str,arr[i])) + "\n" 
    file_out.write(res)       

               
#Fuction convert adjacency list to matrix
def adjacencyList_to_adjacencyMatrix(path_adjacencyList,path_output="./output.txt"):
    #Read file adjacency list at r-mode
    file_inp = open(path_adjacencyList,'r')
    points = []
    nears  = []
    for line in file_inp:
        a = line.strip()
        point,near = a.split(':')
        points.append(point.strip())
        nears.append(near.strip())
               
    for i in range(len(points)):
        points[i] = int(points[i])

    #Make a square matrix full 0's value size max(points)
    size = max(points)+1
    adjacencyMatrix =[[0 for _ in range(size)] for _ in range(size)]

    #Make arr[i][j] = 1 if there is a edge connect them 
    for i in range(len(points)) :
        nearby = list(map(int,nears[i].split(',')))
        for x in nearby:
            adjacencyMatrix[points[i]][x] = 1
            adjacencyMatrix[x][points[i]] = 1


    #Use file output at w-mode to write the result
    file_out = open(path_output,'w')
    result =  "\n".join((" ".join(map(str,row)) for row in adjacencyMatrix))            
    file_out.write(result)

#Function make a edge list from adjacency list
def adjcencyList_to_edgeList(path_adjacencyList,path_output="./output.txt"):
    #Read file adjacency list at r-mode
    file_inp = open(path_adjacencyList,'r')
    points = []     #Save the points
    nears  = []     #Save the adjacency points of the index points
    for line in file_inp:
        a = line.strip()
        point,near = a.split(':')
        points.append(point.strip())
        nears.append(near.strip().split(','))
    
    #Get the amount of points and edges
    n = len(points) 
    m = sum(len(near) for near in nears)//2
    
    #Write the result in output
    file_out = open(path_output,'w')
    file_out.write(f"{n} {m}\n")
    for i in range(len(points)):
        for j in range(len(nears[i])):
            #Points[i] < nears[i][j] to make sure we don' write the same points
            if points[i] < nears[i][j] :
                res = points[i]+" "+nears[i][j]+'\n'
                file_out.write(res)
    print(points,nears)
