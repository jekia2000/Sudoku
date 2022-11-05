class Board:
    def __init__(self):
        self.list=[0]*9
        self.row=[0]*9
        self.column=[0]*9
        self.square=[0]*9
        for i in range (9):
            self.list[i]=[0]*9
            self.row[i]= range(1,10)
            self.column[i]=[]
            self.square[i]=[]

    def fill(self,i,j,value):
        self.list[i][j]=value
        self.row[i].append(value)
        self.column[j].append(value)
        self.square[i//3 * 3 + j // 3].append(value)

    def unfill(self,i,j):
        del self.row[i][len(self.row[i])-1]
        del self.column[j][len(self.column[j])-1]
        del self.square[i //3 *3+j // 3][len(self.square[i//3*3+j//3])-1]


    def backtrack(self):
        positions=[]
        for row in range (9):
            for column in range (9):
                if self.list[row][column]==0:
                    positions.append(9*row+column)
        k=0
        value=1

        while k < len(positions):

            lastPosition=positions[k]
            i=lastPosition // 9
            j=lastPosition % 9
            isWritten=False
            for m in range(value, 10):
                if not(m in self.row[i]) and not(m in self.column[j]) and not(m in self.square[i//3*3+j//3]):
                    self.fill(i,j,m)
                    isWritten=True
                    break

            if not isWritten:
                if k==0:
                    return -1

                lastPosition=positions[k-1]
                i=lastPosition // 9
                j=lastPosition % 9
                self.unfill(i,j)
                value=self.list[i][j]+1
                k=k-1

            else:
                k=k+1
                value=1
        return 0
        

    def write(self):
        for i in range (9):
            row=""
            for j in range (9):
                row+="{:4d}".format(self.list[i][j])
            print(row)


def main():
    b1=Board()
    b1.backtrack()
    b1.write()

if __name__=="__main__":
    main()
    
