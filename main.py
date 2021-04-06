import Euclidean as E
import ReadFile as RF
import networkx as nx
import matplotlib.pyplot as plt

listofcost = [] # { 0 : ["ITB" , fn] }
lintasan = [] # { 0 : { "ITB", level}}
matriksberbobot = [[0 for i in range(RF.jumlah)] for j in range(RF.jumlah)]
listofnode = []
G = nx.Graph()
# pos = None


def showGraph():
    # bikin list of endge dari RF.dict dan 

    for i in range (len(RF.adjmatrix)):
        for j in range (len(RF.adjmatrix)):
            if (RF.adjmatriks[i][j]==1):
                G.add_edge(RF.dict[i][0], RF.dict[j][0], weight=matriksberbobot[i][j])

    # G.add_edges_from(listofedge)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    # nx.draw_networkx_edges(G,pos,width=1.0, alpha=0.5, edge_color='r')
    plt.show()
    print("Simpul Simpul yang Tersedia :")
    for i in range(RF.jumlah):
        print(RF.dict[i][0])
    print("masukan nama simpul dengan benar (case sensitive)")
    start = str(input("Masukan simpul asal : "))
    end = str(input("Masukan simpul tujuan: "))
    AstarSearch(start,end)
    showGraphLintasan(pos)
    

def showGraphLintasan(pos):
    daftarsisi = []
    daftarnode = []
    #  Mencari daftar node lintasan
    daftarnode.append(lintasan[0][0])
    daftarnode.append(lintasan[len(lintasan) - 1][0])
    # Mencari daftar sisi
    for i in range(len(lintasan) - 1):
        daftarsisi.append((lintasan[i][0], lintasan[i+1][0]))

    nx.draw_networkx(G,pos)
    nx.draw_networkx_nodes(G,pos, nodelist = [daftarnode[0]] ,node_size = 1000, alpha=0.5, node_color='y')
    nx.draw_networkx_nodes(G,pos, nodelist = [daftarnode[1]] ,node_size = 1000, alpha=0.5, node_color='g')
    nx.draw_networkx_edges(G,pos, edgelist = daftarsisi ,width=8, alpha=0.5, edge_color='r')
    plt.show()





    
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
            if RF.adjmatriks[indekscurrNode][i] == 1 and (RF.dict[i][0] not in lintasan):
               # RF.dict[i][0] merupakan tetangga 
                nodetetangga = RF.dict[i][0]
                gn += matriksberbobot[indekscurrNode][i]
                hn += E.getDistanceEarth(float(RF.dict[indeksgoal][1]),float(RF.dict[indeksgoal][2]),float(RF.dict[i][1]),float(RF.dict[i][2]))
                fn = gn + hn 
                listofcost.append([ nodetetangga, fn, level])
                listVisited.append(nodetetangga)
        level += 1
        if isNotEmptyQ(listofcost):
            ismallest = minimum(listofcost)
            if listofcost[ismallest][2] == lintasan[len(lintasan)-1][1] :
                lintasan.pop()
                level -= 1 
            if listofcost[ismallest][0] == goal : 
                lintasan.append([ listofcost[ismallest][0], listofcost[ismallest][2]])
                break # memberhentikan while
            lintasan.append([ listofcost[ismallest][0], listofcost[ismallest][2]])
            queue.append(listofcost[ismallest][0])
            listofcost.pop(ismallest)
    # if nodegoal != "" :
    #     lintasan.append([ nodegoal, 99])

    print("Hasil Lintasan Terpendek Adalah ")
    for i in range(len(lintasan)) :
        if (i != len(lintasan)-1) :
            print(lintasan[i][0] + "-> ", end = "" )
        else :
            print(lintasan[i][0])
      
def hitungjarak(path) :

    jarak = 0 
    for i in range (1,len(path)) :
        node = lintasan[i-1][0] 
        # mencari indeks node sekarang 
        for j in range(RF.jumlah) :
            if node == RF.dict[j][0] :
                idxnode = j
                break
        nextnode = lintasan[i][0]
        # mencari indeks next node
        for j in range(RF.jumlah) :
            if nextnode == RF.dict[j][0] :
                idxpath = i
                break
        for j in range(len(matriksberbobot[idxpath])) :
            if j == idxnode :
                jarak += matriksberbobot[idxpath][j]
    return jarak





def main() :

    toberbobot()
    # print(hitungjarak(lintasan))
    showGraph() 
    # showGraphLintasan()
    print("Jarak Terpendek adalah : ")
    print(hitungjarak(lintasan))
    
    



main()
