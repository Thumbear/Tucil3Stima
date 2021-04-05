import Euclidean as E
import ReadFile as RF

listofcost = {} # { 0 : ["ITB" , fn] }
matriksberbobot = [ [ 0 for i in range(RF.jumlah)] for j in range(RF.jumlah)]

def toberbobot() :
    for i in range(RF.jumlah):
        for j in range(RF.jumlah) :
            if RF.adjmatriks[i][j] == 1 :
                matriksberbobot[i][j] = E.getDistanceEarth(float(RF.dict[i][1]),float(RF.dict[i][2]),float(RF.dict[j][1]),float(RF.dict[i][2]))

def isAllvisited(arr) :
    if len(arr) == RF.jumlah :
        return True
    return False 

def getgn(start, n) :
    # cari indeks simpul start 
    for i in range(RF.jumlah):
        if start == RF.dict[i][0] :
            indeks = i 
    
    for j in range(RF.jumlah) :

    
    return 0 

def AstarSearch(start, goal):
    costTotal = 0
    listVisited = [] # Closed : List of Node yang sudah dievaluasi
    listNotVisited = [] # Open : List of node yang akan dievalusasi
    
    listNotVisited.append(start)
    listVisited.append(start)
    while (isAllvisited(listVisited) == False) and  : # tambah selama nodenya bukan node goal dan juga open masi ada 
        if goal in listNotVisited :
            print ('Goal merupakan Simpul Start')
        else :
            



def main() :
    print("=======Bagian node=======")
    print()
    for z in range(len(RF.dict)) :
        print(RF.dict[z])
    print()
    print("=======bagian matriks=======")
    print()

    for p in range(len(RF.adjmatrix)) : 
        print(RF.adjmatriks[p])

    print()
    print("=======Bagian Matriks Berbobot=======")
    print()
    toberbobot()
    for i in range(RF.jumlah) :
        print(matriksberbobot[i])


main()
