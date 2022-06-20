# IMPORTS 
import numpy as np

# GLOBAL
global map

def createEmptyMap(nRows : int, nCols : int) -> None:
    global map
    map = np.zeros((nRows, nCols), dtype=np.int8)

def updateMap(line : str) -> None:
    splittedLine = splitLine(line)
    xRange = getXRange(splittedLine)
    yRange = getYRange(splittedLine)
    modifyMap(xRange, yRange)

def modifyMap(xRange : list, yRange : list) -> None:
    global map
    if len(yRange) == 1 : modifyMapHorizontal(xRange, yRange)
    elif len(xRange) == 1 : modifyMapVertical(xRange, yRange)
    elif len(xRange) == len(yRange) : 
        modifyMapDiagonal(xRange, yRange)

def modifyMapHorizontal(xRange : list, yRange : list) -> None:
    x = yRange[0]
    for y in xRange:
        map[x][y] += 1

def modifyMapVertical(xRange : list, yRange : list) -> None:
    y = xRange[0]
    for x in yRange:
        map[x][y] += 1

def modifyMapDiagonal(xRange : list, yRange : list) -> None:
    for x,y in zip(yRange, xRange):
        map[x][y] += 1

def splitLine(line : str) -> list:
    res = []
    for coordinates in line.split(' -> '):
        for n in coordinates.split(','):
            res.append(n)
    return res



def getXRange(coordinates : list) -> list:
    x1, x2 = int(coordinates[0], 10), int(coordinates[2],10)
    res = np.arange(np.minimum(x1,x2), np.maximum(x1,x2)+1)
    if len(res) == 0 : res = [x1]
    if x2 > x1 : res = res[::-1]
    return res

def getYRange(coordinates : list) -> list:
    y1, y2 = int(coordinates[1],10), int(coordinates[3],10)
    res = np.arange(np.minimum(y1,y2), np.maximum(y1,y2)+1)
    if len(res) == 0 : res = [y1]
    if y2 > y1 : res = res[::-1]
    return res


if __name__ == '__main__':
    '''
    # TEST INPUT
    data = [
            '0,9 -> 5,9',
            '8,0 -> 0,8',
            '9,4 -> 3,4',
            '2,2 -> 2,1',
            '7,0 -> 7,4',
            '6,4 -> 2,0',
            '0,9 -> 2,9',
            '3,4 -> 1,4',
            '0,0 -> 8,8',
            '5,5 -> 8,2'
            ]
    createEmptyMap(10,10)
    '''
    file = open('data.txt')
    data = file.readlines()
    file.close()
    createEmptyMap(1000,1000)

    for line in data :
        updateMap(line)

    print(map)
    print("RESULTADO : " + str(np.count_nonzero(map >= 2)))

