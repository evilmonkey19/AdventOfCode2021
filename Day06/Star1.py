# IMPORTS
import numpy as np

global poblation

def updatePoblation() -> None:
    for i in range(len(poblation)):
        if poblation[i] == 0:
            giveBirth(i)
        else:
            poblation[i] -= 1

def giveBirth(index : int) -> None:
    global poblation
    poblation[index] = 6
    poblation = np.append(poblation, 8)


if __name__ == '__main__':
    
    # TEST INPUT
    data = '3,4,3,1,2'
    '''

    file = open('data.txt')
    data = file.readlines()
    file.close()
    data = data[0]
    '''
    poblation = np.array(data.split(','), dtype=np.int8)
    nDays = 80

    for i in range(nDays):
        updatePoblation()

    print(len(poblation))
