
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


if __name__ == "__main__":
    hash = Hash()

    filenameA = "a.txt"
    # filenameB = "b.txt"
    # filenameC = "c.txt"
    # filenameD = "d.txt"
    # filenameE = "e.txt"

    # filenames = [filenameA, filenameB, filenameC, filenameD, filenameE]
    filenames = [filenameA]

    for filename in filenames:
        print(filename)
        file, S, TI, NS, NC, BP, SI, CT = hash.DataIn(filename)
        # menuSorted, menuScoreSorted, argSort = hash.Sort(menu)
        # ress = hash.Crude(M, T2, T3, T4, menu)
        # ressToFile = hash.ResToFile(ress, filename + ".out")
        # print(ressToFile[0])
