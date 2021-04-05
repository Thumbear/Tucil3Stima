dict = {} 
adjmatrix = {} ; 
def Bacafile() :
    f = open("PetaITB.txt", "r")
    i = 0 
    j = 0 
    for line in f :
        line = line.replace("\n", "").split(" ")
        if isNotMatrix(line) : 
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

main()
