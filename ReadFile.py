dict = {} 
adjmatrix = {} 
arrSumNode = []
def Bacafile() :
    f = open("PetaITB.txt", "r")
    i = 0 
    j = 0 
    pertama = True
    for line in f :
        line = line.replace("\n", "").split(" ")
        if (pertama) :
            arrSumNode.append(int(line[0]))
            pertama = False 
        elif isNotMatrix(line) : 
            dict[i] = line
            i += 1 
        else :
            for k in range(len(line)):
                line[k] = int(line[k])
            adjmatrix[j] = line
            j += 1 

    f.close

def isNotMatrix(arr) :
    if arr[0] != '1' and arr[0] != '0' :
        return True
    return False 

def main() :
    Bacafile()
    print("=======Bagian node=======")
    print()
    for z in range(len(dict)) :
        print(dict[z])
    print()
    print("=======bagian matriks=======")
    print()
    for p in range(len(adjmatrix)) : 
        print(adjmatrix[p])


Bacafile()
jumlah = arrSumNode[0]
adjmatriks = [ 0 for i in range(jumlah) ]
for g in range(jumlah):
    # for h in range(jumlah) :
    adjmatriks[g] = adjmatrix[g]

