class NQueen:
    def __init__(self,box):
        self.box = box
        self.queen = 'Queen'
        self.queenPos = [None,None,None,None]

    def placeQueen(self,i,j):
        if self.detectRowAttack(i) is False:
            self.box[i][j] = self.queen

    def detectRowAttack(self,i):
        count = 0
        for q in self.box[i]:
            if q is self.queen:
                count += 1
                if count > 0:
                    return True
        return False

    def detectColunmAttack(self,j):
        count = 0
        #for n in range():
        pass




box = [
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None]
]

nQueen = NQueen(box)
