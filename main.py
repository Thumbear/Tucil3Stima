import Euclidean as E
import ReadFile as RF

listofcost = [] # { 0 : ["ITB" , fn] }
lintasan = [] # { 0 : { "ITB", level}}
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

def isNotEmptyQ(arr) :
    return len(arr) > 0   

def minimum(arr) : 
    min = arr[0][1]
    imin = 0 
    for i in range(1,len(arr)):
        if arr[i][1] < min :
            min = arr[i][1]
            imin = i 
    return imin
    

def AstarSearch(start, goal):
 
    listVisited = [] 
    queue = [] 
    queue.append(start) 
    lintasan.append([ start, 0 ])
    indeksgoal = 0 
    listVisited.append(start)
    gn = 0 
    level = 1 
    nodegoal = "" 
    # mendapatkan indeks goal
    for i in range(RF.jumlah):
        if goal == RF.dict[i][0] :
            indeksgoal = i 
            break 
    while (isNotEmptyQ(queue)) :
        currNode = queue.pop() 
        indekscurrNode = 0 

        # mencari indeks di dict
        for i in range(RF.jumlah):
            if currNode == RF.dict[i][0] :
                indekscurrNode = i 
                break 
        # mentranversal kan semua tetangga currNode sekaligus menghitung gn dan hn
        for i in range(len(RF.adjmatriks[indekscurrNode])):
            hn = 0
            gn = 0 
            if RF.adjmatriks[indekscurrNode][i] == 1 and (RF.dict[i][0] not in listVisited) :
               # RF.dict[i][0] merupakan tetangga 
                nodetetangga = RF.dict[i][0]
                gn += matriksberbobot[indekscurrNode][i]
                hn += E.getDistanceEarth(float(RF.dict[indeksgoal][1]),float(RF.dict[indeksgoal][2]),float(RF.dict[i][1]),float(RF.dict[i][2]))
                fn = gn + hn 
                listofcost.append([ nodetetangga, fn, level])
                listVisited.append(nodetetangga)
        level += 1
        print(listofcost)
        print(listVisited)
        if isNotEmptyQ(listofcost):
            ismallest = minimum(listofcost)
            if listofcost[ismallest][2] == lintasan[len(lintasan)-1][1] :
                lintasan.pop()
            if listofcost[ismallest][0] == goal :
                lintasan.append([ listofcost[ismallest][0], listofcost[ismallest][2]])
                break
            lintasan.append([ listofcost[ismallest][0], listofcost[ismallest][2]])
            queue.append(listofcost[ismallest][0])
            listofcost.pop(ismallest)
    # if nodegoal != "" :
    #     lintasan.append([ nodegoal, 99])
    print(lintasan)
    print("Hasil Lintasan Terpendek Adalah ")
    for i in range(len(lintasan)) :
        if (i != len(lintasan)-1) :
            print(lintasan[i][0] + "-> ", end = "" )
        else :
            print(lintasan[i][0])
      



def main() :
    start = str(input("Masukan simpul asal : "))
    end = str(input("Masukan simpul tujuan: "))
    toberbobot()
    AstarSearch(start,end)


main()
