
class Hash:

    def __init__(self):
        pass

    def _ReadIp(self, filename):
        with open(filename, "r") as f:
            file = f.read()
        file = file.split("\n")
        if len(file[-1]) == 0:
            file.pop(-1)
        return file    


    def _ToVars(self, file):
        """
        S: Simulation time in seconds
        TI: Total number of intersections
        NS: No of Streets
        NC: No of Cars
        BP: Bonus Points
        SI : list of Street information {intersection1, intersection2, streetname, duration in street}
        CT:  list of Car Travel {no: of streets, street1, street2, street3...}
        """
        FL = file.pop(0)
        # print(MT)
        FL = FL.split(" ")
        if len(FL) > 5:
            FL.pop(-1)

        S = FL[0]
        TI = FL[1]
        NS = int(FL[2])
        NC = int(FL[3])
        BP = FL[4]
        SI =[]
        CT = []
        for i in range(NS):
            item = file[i].split(" ")
            SI.append(item[:])
        print(SI)

        for i in range(NS, NS + NC):
            item = file[i].split(" ")
            CT.append(item[:])
        print(CT)
        return file, S, TI, NS, NC, BP, SI, CT          

    def DataIn(self, filename):
        fileRaw = self._ReadIp(filename)
        file, S, TI, NS, NC, BP, SI, CT   = self._ToVars(fileRaw)
        return file, S, TI, NS, NC, BP, SI, CT 


    # Function to convert adjacency
    # list to adjacency matrix  
    def convert(self, adj, V):

        # Initialize a matrix
        matrix = [[0 for j in range(V)] 
                    for i in range(V)]   
        for i in range(V):
            for j in adj[i]:
                matrix[i][j] = 1
        return matrix

    # Function to insert vertices 
    # to adjacency list
    def insert(self, adj, u, v):

        # Insert a vertex v to vertex u
        adj[u].append(v)
        return

    # Function to display adjacency list
    def printList(self,adj, V):
        
        for i in range(V):
            print(i, end = '')
            
            for j in adj[i]:
                print(' --> ' + str(j), end = '')
            print()
        print()

    # Function to display adjacency matrix
    def printMatrix(self, adj, V):
        
        for i in range(V):
            for j in range(V):
                print(adj[i][j], end = ' ')
                
            print()

    
    def RessToFile(self, ress, filename="trash"):
        ressToFile = []
        ressToFile.append(str(len(ress)) + "\n")
        for k in range(len(ress)):
            ressToFile.append(str(k) + "\n")
            res = ress[k]
            ressToFile.append(str(len(res)) + "\n")
            for re in res:
                ressToFile.append(" ".join(str(item) for item in re) + "\n")
        with open(filename, "w") as f:
            f.writelines(ressToFile)
        return ressToFile
        

if __name__ == "__main__":

    filenameA = "a.txt"
    # filenameB = "b.txt"
    # filenameC = "c.txt"
    # filenameD = "d.txt"
    # filenameE = "e.txt"

    # filenames = [filenameA, filenameB, filenameC, filenameD, filenameE]
    filenames = [filenameA]

    for filename in filenames:
        hash = Hash()
        print(filename)
        file, S, TI, NS, NC, BP, SI, CT = hash.DataIn(filename)




        # adjacency matrix code
        V = int(TI)
        adjList = [[] for i in range(V)]

        # Inserting edges
        for i in range(NS):
            hash.insert(adjList, int(SI[i][0]), int(SI[i][1]))
            i+=1
        # Display adjacency list
        print("Adjacency List: ")
        hash.printList(adjList, V)

        # Function call which returns
        # adjacency matrix after conversion
        adjMatrix = hash.convert(adjList, V)

        # Display adjacency matrix
        print("Adjacency Matrix: ")
        hash.printMatrix(adjMatrix, V)




