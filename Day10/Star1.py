openingChars : list = ['(', '[', '{', '<']
closingChars : list = [')', ']', '}', '>']
pointsChars : list  = [3, 57, 1197, 25137]

def countIllegalChars() -> int:
    illegalClosingList : list = []
    for line in data:
        illegalClosingList.extend(getIllegalClosingsOnStr(line))
    return countPointsIllegalClosing(illegalClosingList)

def countPointsIllegalClosing(illegalClosingList : list) -> int:
    res : int = 0
    index : int = 0
    for char in illegalClosingList :
        index = closingChars.index(char)
        res = res + pointsChars[index]
    return res

def getIllegalClosingsOnStr(line : str) -> list:
    illegalClosings : list = []
    opening_pool = []
    for char in line:
        if char in openingChars:
            opening_pool.append(char)
        else:
            if not isRightClosing(opening_pool[-1], char):
                illegalClosings.append(char)
            opening_pool.pop(-1)
    return illegalClosings

def isRightClosing(openingChar : str, closingChar : str) -> bool:
    openingIndex : int = openingChars.index(openingChar)
    closingIndex : int = closingChars.index(closingChar)
    return openingIndex == closingIndex



if __name__ == "__main__":
    global data
    '''
    data = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]
    '''
    #read data from data.txt and put in data
    data = []
    with open('data.txt', 'r') as f:
        for line in f:
            data.append(line.strip())

    res : int = countIllegalChars()
    print(f'RES: {res}')
