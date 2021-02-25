import collections
import numpy as np
# import matplotlib.pyplot as plt
# plt.ion()


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
        MT = file.pop(0)
        # print(MT)
        MT = MT.split(" ")
        if len(MT) > 4:
            MT.pop(-1)
        MT = np.int0(MT)
        M = MT[0]
        T2 = MT[1]
        T3 = MT[2]
        T4 = MT[3]
        menu = []
        for item in file:
            item = item.split(" ")
            menu.append(item[1:])
        return file, MT, M, T2, T3, T4, menu

    def DataIn(self, filename):
        fileRaw = self._ReadIp(filename)
        file, MT, M, T2, T3, T4, menu = self._ToVars(fileRaw)
        # return file, MT, M, T2, T3, T4
        return M, T2, T3, T4, menu

    def _MenuFlat(self, menu):
        menuFlat = []
        for men in menu:
            for me in men:
                menuFlat.append(me)
        return menuFlat

    def _MenScore(self, men, ingredientsCounted):
        score = 0
        for me in men:
            score = score + (1 / ingredientsCounted[me])
        return score

    # def _ingredientsCounted(self, menuFlat):
    def MenuScore(self, menu):
        menuFlat = self._MenuFlat(menu)
        ingredientsCounted = collections.Counter(menuFlat)
        menuScore = []
        for men in menu:
            menuScore.append(self._MenScore(men, ingredientsCounted))
        return menuScore

    def Sort(self, menu):
        menuScore = self.MenuScore(menu)
        # argSort = np.argsort(menuScore)
        argSort = range(len(menuScore))
        menuSorted = []
        menuScoreSorted = []
        for i in argSort:
            menuSorted.append(menu[i])
            menuScoreSorted.append(menuScore[i])
        return menuSorted, menuScoreSorted, argSort

    def ResToFile(self, ress, filename="trash"):
        resToFile = []
        resToFile.append(str(len(ress)) + "\n")
        for line in ress:
            resToFile.append(" ".join(str(item) for item in line) + "\n")
        with open(filename, "w") as f:
            f.writelines(resToFile)
        return resToFile

    def ScoreOfResFile(self, filename="trash"):
        with open(filename, "r") as f:
            file = f.readlines()
        fileList = []
        for fil in file:
            fileList.append(fil[:-1])
        if len(fileList) != int(fileList[0]):
            print("Wrong number of lines on first line")
            return 0

    def Crude(self, M, T2, T3, T4, menu):
        menuSorted, menuScoreSorted, argSort = self.Sort(menu)
        argSort = list(argSort)
        ress = []

        for t in range(T4):
            res = [4]
            for k in range(4):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 5:
                ress.append(res)

        for t in range(T3):
            res = [3]
            for k in range(3):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 4:
                ress.append(res)

        for t in range(T2):
            res = [2]
            for k in range(2):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 3:
                ress.append(res)
        return ress

    def Dumb(self, M, T2, T3, T4, menu):
        menuSorted, menuScoreSorted, argSort = self.Sort(menu)
        argSort = list(argSort)
        ress = []

        for t in range(T4):
            res = [4]
            for k in range(4):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 5:
                ress.append(res)

        for t in range(T3):
            res = [3]
            for k in range(3):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 4:
                ress.append(res)

        for t in range(T2):
            res = [2]
            for k in range(2):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 3:
                ress.append(res)
        return ress

    def Vector(self, menu):
        menuFlat = self._MenuFlat(menu)
        menuBasis = list(set(menuFlat))
        menuVector = np.zeros((len(menu), len(menuBasis)))
        for r in range(len(menu)):
            men = menu[r]
            for c in range(len(menuBasis)):
                basi = menuBasis[c]
                if basi in men:
                    menuVector[r, c] = 1
        return menuVector, menuBasis

    def Cor2(self, M, T2, T3, T4, menu):
        menuVector, menuBasis = self.Vector(menu)
        cor = np.matmul(menuVector, menuVector.transpose())
        # corBackup = cor.copy()
        corMax = len(menuVector) + 1
        # corMax = cor.max() + 1
        # zerosIndex = np.where(menu)
        emptied = []
        menuIndex = list(np.arange(len(menu)))
        ress = []

        for t in range(T4):
            row = cor[menuIndex[0], :].copy()
            row[menuIndex[0]] = corMax
            lowToHigh = np.argsort(row)
            lowToHigh = list(lowToHigh)
            lowToHig = lowToHigh[0:3]
            # print(lowToHig)
            # print(row)
            if row[lowToHig[-1]] < corMax:
                res = lowToHig
                res.append(menuIndex[0])
                resWithT = [4]
                for re in res:
                    cor[re, :] = corMax
                    cor[:, re] = corMax
                    rePos = np.where(np.array(menuIndex) == re)[0][0]
                    emptied.append(menuIndex.pop(rePos))
                    resWithT.append(re)
                ress.append(resWithT)
            else:
                print("T4 over, t = ", t)
                break
        return ress

    def Trash(self, filename):
        inputRaw = self._ReadIp(filename)
        tSim = inputRaw[0].split(" ")[0]
        tSim = int0(tSim)
        kStreets = inputRaw[0].split(" ")[2]
        kStreets = int0(kStreets)
        kInterSections = inputRaw[0].split(" ")[1]
        kInterSections = int0(kInterSections)
        kCars = inputRaw[0].split(" ")[3]
        kCars = int0(kCars)
        carsRaw = inputRaw[-kCars:]
        cars = []
        for carRaw in carsRaw:
            car = carRaw.split(" ")[1:]
            cars.append(car)
        streets = []
        streetsRaw = inputRaw[1:kStreets+1]
        for streetRaw in streetsRaw:
            street = streetRaw.split(" ")
            street[0] = int0(street[0])
            street[1] = int0(street[1])
            street[3] = int0(street[3])
            
            streets.append(street)

        interSections = []
        for k in range(kInterSections):
            interSections.append([])
        
        for street in streets:
            interSections[street[1]].append(street[2])
        return interSections, cars, tSim

    def Counts(self, cars, tSim):
        carsFlat = self._MenuFlat(cars)
        streetSet = list(set(carsFlat))
        counts = dict()
        for street in streetSet:
            counts[street] = 0 #change to 1 and see
        for car in cars:
            # weight = sqrt(len(car))
            weight = 1 / len(car)
            # weight = 1
            for street in car:
                counts[street] = counts[street] + weight
#                if counts[street] > tSim:
#                    counts[street] = tSim
#                    print("Exceeded tSim")
        keys = counts.keys()
        for key in keys:
            # counts[key] = sqrt(counts[key])
            # counts[key] = counts[key] ** 2
            if counts[key] > tSim:
                counts[key] = tSim
                print("Exceeded tSim at Square")
        # counts = collections.Counter(carsFlat)
        # counts = dict(counts)
        return counts

    def Ress(self, interSections, counts, tSim):
        ress = []
        for interSection in interSections:
            res = []
            for street in interSection:
                if street in counts.keys():
                    seconds = counts[street] / len(interSection)
                    # seconds = counts[street]
                    seconds = seconds / 100
                    seconds = ceil(seconds)
                    seconds = int0(seconds)
                else:
                    seconds = 1
                # res.append([street, seconds])
                seconds = np.random.randint(10)
                if seconds > tSim:
                    seconds = tSim
                res.append([street, seconds])
            ress.append(res)
        return ress

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
    hash = Hash()
    self = hash

    filenameA = "a.txt"
    filenameB = "b.txt"
    filenameC = "c.txt"
    filenameD = "d.txt"
    filenameE = "e.txt"
    filenameF = "f.txt"

    filenames = [filenameA, filenameB, filenameC, filenameD, filenameE, filenameF]
    # filenames = [filenameA]

    # filename = filenames[0]
    for filename in filenames:
        interSections, cars, tSim = hash.Trash(filename)
        counts = hash.Counts(cars, tSim)
        ress = hash.Ress(interSections, counts, tSim)
        hash.RessToFile(ress, filename + ".out")
        print(filename)

#    for filename in filenames:
#        print(filename)
#        M, T2, T3, T4, menu = hash.DataIn(filename)
#        menuSorted, menuScoreSorted, argSort = hash.Sort(menu)
#        # ress = hash.Dumb(M, T2, T3, T4, menu)
#        ress = hash.Cor2(M, T2, T3, T4, menu)
#        filenameBase = filename.split(".")[0]
#        ressToFile = hash.ResToFile(ress, filenameBase + ".out")
#        print(ressToFile[0])
