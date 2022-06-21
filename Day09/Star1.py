# IMPORTS
import numpy as np

def checkIfMinimum(data : np.matrix, pos : tuple) -> bool:
    if (checkNord(data, pos) == False) : return False
    if (checkSouth(data, pos) == False) : return False
    if (checkEast(data, pos) == False) : return False
    if (checkWest(data, pos) == False) : return False
    return True
    
def checkNord(data : np.matrix, pos : tuple) -> bool:
    # There is no number above
    if pos[0] <= 0 : return True
    return data[pos[0], pos[1]] < data[pos[0]-1, pos[1]]

def checkSouth(data : np.matrix, pos : tuple) -> bool:
    # There is no number under
    if pos[0] >= data.shape[0]-1 : return True
    return data[pos[0], pos[1]] < data[pos[0]+1, pos[1]]

def checkEast(data : np.matrix, pos : tuple) -> bool:
    # There is no number to the East
    if pos[1] >= data.shape[1]-1 : return True
    return data[pos[0], pos[1]] < data[pos[0], pos[1]+1]

def checkWest(data : np.matrix, pos : tuple) -> bool:
    # Thre is no number to the West
    if pos[1] <= 0 : return True
    return data[pos[0], pos[1]] < data[pos[0], pos[1]-1]



if __name__ == '__main__':
    '''
    # TEST INPUT
    data = np.matrix([
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
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

    data = np.matrix(data)
    res = 0
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            if(checkIfMinimum(data, (row, col))):
                res += data[row, col] +1

    print("RESULTADO : " + str(res))