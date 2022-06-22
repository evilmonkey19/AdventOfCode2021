from types import NoneType
import numpy as np

def getExplotedDumbos() -> int:
    rows, cols = np.nonzero(data >= 10)
    while len(rows)>0 and len(cols)>0:
        data[rows[0], cols[0]] = 0
        addOneToNeighbours(rows[0], cols[0])
        rows, cols = np.nonzero(data >=10)
    return len(data[data==0])

def addOneToNeighbours(row: int, col : int) -> None:
    addOneToCell(row, col-1) # north
    addOneToCell(row+1, col-1) # north-east
    addOneToCell(row+1, col) # east
    addOneToCell(row+1, col+1) # south-east
    addOneToCell(row, col+1) # south
    addOneToCell(row-1, col+1) # south-west
    addOneToCell(row-1, col) # west
    addOneToCell(row-1, col-1) # north-west

def addOneToCell(row: int, col: int) -> None:
    if row < 0 or row > data.shape[0]-1: return
    if col < 0 or col > data.shape[1]-1: return
    if data[row, col] == 0: return
    data[row, col] += 1

if __name__ == "__main__":
    global data
    '''
    data = np.array([
                    [5,4,8,3,1,4,3,2,2,3],
                    [2,7,4,5,8,5,4,7,1,1],
                    [5,2,6,4,5,5,6,1,7,3],
                    [6,1,4,1,3,3,6,1,4,6],
                    [6,3,5,7,3,8,5,4,7,8],
                    [4,1,6,7,5,2,4,6,4,5],
                    [2,1,7,6,8,4,1,7,2,1],
                    [6,8,8,2,8,8,1,1,3,4],
                    [4,8,4,6,8,4,8,5,5,4],
                    [5,2,8,3,7,5,1,5,2,6],
                    ])
    '''
    file = open('data.txt')
    file_data = file.readlines()
    file.close()
    data = []
    file_data = [line.split() for line in file_data]
    for line in file_data:
        for n in line:
            data.append([int(x) for x in n])
    data = np.array(data)
    res : int = 0
    for _ in range(0,100):
        data += 1
        res += getExplotedDumbos()
    print(f'RES: {res}')
