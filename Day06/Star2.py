# IMPORTS
import numpy as np

global poblation

def updatePoblation() -> None:
    toGiveBirth = poblation[0]
    poblation[0:8] = poblation[1:9]
    poblation[6] += toGiveBirth
    poblation[8] = toGiveBirth


if __name__ == '__main__':
    '''
    # TEST INPUT
    data = '3,4,3,1,2'
    '''

    file = open('data.txt')
    data = file.readlines()
    file.close()
    data = data[0]

    poblation = np.zeros(9, dtype = np.int64)
    for number in data.split(','):
        poblation[int(number,10)+1] += 1
    nDays = 256
    for i in range(nDays+1):
        updatePoblation()

    print(sum(poblation))
