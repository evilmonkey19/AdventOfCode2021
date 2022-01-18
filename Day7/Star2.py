# IMPORTS
import numpy as np
import math

def getMinimumFuelPosition(data : list) -> int:
    index, min = 0, math.inf 
    for n in range(max(data)):
        if min > (value:=calculateFuelUsed(data, n)) :
            index, min = n, value
    return index 
    

def calculateFuelUsed(data : list, index : int) -> int:
    res = 0
    for n in data:
        res += sum(np.arange(np.abs(n-index)+1))
    print(index)
    return res

if __name__ == '__main__':
    '''
    # TEST INPUT
    data = '16,1,2,0,4,2,7,1,2,14'
    '''

    file = open('data.txt')
    data = file.readlines()
    file.close()
    data = data[0]

    data = data.split(',')
    data = [int(n,10) for n in data]

    index = getMinimumFuelPosition(data)
    fuelUsed = calculateFuelUsed(data, index)

    print("Total fuel used: " + str(fuelUsed))
