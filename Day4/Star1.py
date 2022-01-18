from typing import Tuple
from numpy import array, sum, append

def playBingo(numbers : list, cardboards : list) -> Tuple: 
    for n in numbers:
        cardboards = markNumberOnCardboards(n, cardboards)
        if (winner:=isThereAWinner(cardboards)) >= 0:
            return (n, cardboards[winner])
    return (-1, -1)

def markNumberOnCardboards(number : str, carboards : list) -> None:
    for cardboard in carboards:
        if (indexs:=getIndexOfNumberInCardboard(number, cardboard)) != None :
            cardboard = markNumberOnCardboard(cardboard, indexs)
    return carboards

def markNumberOnCardboard(cardboard : array, indexs : list) -> array:
    for index in indexs:
        cardboard[index[0]][index[1]] = 'x'
    return cardboard


def isThereAWinner(cardboards : list) -> int:
    for cardboard in enumerate(cardboards):
        if (isAnyRowCompletedInCardboard(cardboard[1]) or
            isAnyColumnCompletedInCardboard(cardboard[1])):
            return cardboard[0]
    return -1

def isAnyRowCompletedInCardboard(cardboard : array) -> bool:
    for i in range(0, cardboard.shape[0]):
        if all(box == 'x' for box in cardboard[i,:]):
            return True
    return False

def getCompletedRowInCardboard(cardboard : array) -> int:
    for i in range(0, cardboard.shape[0]):
        if all(box == 'x' for box in cardboard[i,:]):
            return i
    return -1

def isAnyColumnCompletedInCardboard(cardboard : array) -> bool:
    for i in range(0, cardboard.shape[1]):
        if all(box == 'x' for box in cardboard[:,i]):
            return True
    return False

def getCompletedColumnInCardboard(cardboard : array) -> int:
    for i in range(0, cardboard.shape[1]):
        if all(box == 'x' for box in cardboard[i,:]):
            return i
    return -1

def getIndexOfNumberInCardboard(number : str, carboard : array) -> list:
    res = []
    for i in range(0, len(carboard)):
        for j in range(0, len(carboard[i])):
            if carboard[i][j] == number:
                res.append((i,j))
    return res

def reconvertCardboard(cardboard : array) -> array:
    cardboard = reconvertXto0(cardboard)
    cardboard = reconvertToInts(cardboard)
    return cardboard

def reconvertXto0(cardboard : array) -> array:
    for i in range(0, cardboard.shape[0]):
        cardboard[:, i] = list(map(lambda x: x.replace('x', '0'), cardboard[:,i])) 
    return cardboard

def reconvertToInts(cardboard : array) -> array:
    return [list(map(int, x)) for x in cardboard]

if __name__ == '__main__':
    '''
    # TEST INPUT
    numbers = ['7','4','9','5','11','17','23','2','0','14',
                '21','24','10','16','13','6','15','25','12',
                '22','18','20','8','19','3','26','1']

    cardboard1 = array([
                    ['22',  '13',   '17',   '11',   '0'],
                    ['8',   '2',    '23',   '4',    '24'],
                    ['21',  '9',    '14',   '16',   '7'],
                    ['6',   '10',   '3',    '18',   '5'],
                    ['1',   '12',   '20',   '15',   '19']
    ])
    
    cardboard2 = array([
                    ['3',   '15',   '0',    '2',    '22'],
                    ['9',   '18',   '13',   '17',   '5'],
                    ['19',  '8',    '7',    '25',   '23'],
                    ['20',  '11',   '10',   '24',   '4'],
                    ['14',  '21',   '16',   '12',   '6']
    ])

    cardboard3 = array([
                    ['14',  '21',   '17',   '24',   '4'],
                    ['10',  '16',   '15',   '9',    '19'],
                    ['18',  '8',    '23',   '26',   '20'],
                    ['22',  '11',   '13',   '6',    '5'],
                    ['2',   '0',    '12',   '3',    '7']
    ])
    cardboards = [cardboard1, cardboard2, cardboard3]
    '''
    file = open('data.txt')
    data = file.readlines()
    file.close()

    numbers = list(data[0].strip().split(','))
    
    cardboards = []
    cardboard = []
    for i in range(2,len(data)):
        if data[i] != '\n':
            cardboard.append(list(filter(None, data[i].strip().split(' '))))
        else:
            cardboard = array(cardboard)
            cardboards.append(cardboard)
            cardboard = []
            
    (winning_number, cardboard) = playBingo(numbers, cardboards)

    res = sum(reconvertCardboard(cardboard))
    res = res * int(winning_number)
    
    print("Resultado : " + str(res))
    