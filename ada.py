# Python3 program to implement
# the above approach

# Function to insert vertices 
# to adjacency list
def insert(adj, u, v):

    # Insert a vertex v to vertex u
    adj[u].append(v)
    return

# Function to display adjacency list
def printList(adj, V):
    
    for i in range(V):
        print(i, end = '')
        
        for j in adj[i]:
            print(' --> ' + str(j), end = '')
            
        print()
        
    print()
        
# Function to convert adjacency
# list to adjacency matrix
def convert(adj, V):

    # Initialize a matrix
    matrix = [[0 for j in range(V)] 
                for i in range(V)]
    
    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1
    
    return matrix

# Function to display adjacency matrix
def printMatrix(adj, V):
    
    for i in range(V):
        for j in range(V):
            print(adj[i][j], end = ' ')
            
        print()
        
    print()
        
# Driver code
if __name__=='__main__':
    TI =5
    NS = 5
    V = TI
    SI = [['2', '0', 'rue-de-londres', '1'], ['0', '1', 'rue-d-amsterdam', '1'], ['3', '1', 'rue-d-athenes', '1'], ['2', '3', 'rue-de-rome', '2'], ['1', '2', 'rue-de-moscou', '3']]
    adjList = [[] for i in range(V)]

    # Inserting edges
    for i in range(NS):
        insert(adjList, int(SI[i][0]), int(SI[i][1]))
        i+=1
    # Display adjacency list
    print("Adjacency List: ")
    printList(adjList, V)

    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(adjList, V)

    # Display adjacency matrix
    print("Adjacency Matrix: ")
    printMatrix(adjMatrix, V)

# This code is contributed by rutvik_56
