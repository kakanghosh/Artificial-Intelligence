class NPuzzle:
    def __init__(self,matrix):
        self.matrix = matrix

    def getInversion(self):
        inversionList = []
        for n in range(len(self.matrix)):
            for m in range(len(self.matrix[n])):
                #print(n,', ',m,' = ',self.matrix[n][m],' ',end='')
                 if self.matrix[n][m] is not None:
                     inversionList.append(self.calculateInv(n, m, self.matrix[n][m]))
            #print()
        print(inversionList)
        #print('Inversiom: ',sum(inversionList))
        return sum(inversionList)

    def calculateInv(self,i,j,value):
        count = 0
        #print(i,',',j,' = ',value,end='')
        for n in range(len(self.matrix)):
            for m in range(len(self.matrix[n])):
                if self.matrix[n][m] is not None:
                    if  self.matrix[n][m] < value:
                        if n == i and m > j:
                            count += 1
                        elif n > i:
                            count += 1
        #print()
        return count

    def getBlankPosition(self):
        index = 0
        for n in range(len(self.matrix)-1,0,-1):
            index += 1
            for m in range(len(self.matrix[n])):
                if self.matrix[n][m] is None:
                    return  index

def isEven(number):
    if number % 2 is 0:
        return True
    else:
        return False

puzzle = [
    [6,1,10,2],
    [7,11,4,14],
    [5,None,9,15],
    [8,12,13,3]
]
solvable = False
nPuzzle = NPuzzle(puzzle)
dimen = 16
inv = nPuzzle.getInversion()
blank = nPuzzle.getBlankPosition()

if isEven(dimen) is  False:
    if isEven(inv) is True:
        solvable = True
else:
    if isEven(blank) is False:
        if isEven(inv):
            solvable = True
    else:
        if isEven(inv) is False:
            solvable = True


if solvable:
    print("Yes Puzzle is Solvable")
else:
    print("No!! Puzzle is not Solvable")