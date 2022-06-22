openingChars : list = ['(', '[', '{', '<']
closingChars : list = [')', ']', '}', '>']
pointsChars : list  = [ 1,   2,   3,   4 ]

def getScoreUncompletedLines(uncompletedLines : list) -> int:
    scores : list = []
    for line in uncompletedLines:
        scores.append(getScoreUncompletedLine(line))
    scores.sort()
    return scores[int((len(scores)-1)/2)]

def getScoreUncompletedLine(line : str) -> int:
    uncompletedClosings : list = getUncompletedClosingsOnStr(line)
    return countPointsUncompletedClosing(uncompletedClosings)

def countPointsUncompletedClosing(illegalClosingList : list) -> int:
    res : int = 0
    index : int = 0
    for char in illegalClosingList :
        index = openingChars.index(char)
        res = (res*5) + pointsChars[index]
    return res

def getUncompletedClosingsOnStr(line : str) -> list:
    opening_pool : list = []
    for char in line:
        if char in openingChars:
            opening_pool.append(char)
        else:
            opening_pool.pop(-1)
    return opening_pool[::-1]

def getUncorruptedLines() -> list:
    uncorruptedLines : list = []
    for line in data:
        if getIllegalClosingsOnStr(line) == []:
            uncorruptedLines.append(line)
    return uncorruptedLines

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
    data = []
    with open('data.txt', 'r') as f:
        for line in f:
            data.append(line.strip())

    uncompletedLines : list = getUncorruptedLines()
    res : int = getScoreUncompletedLines(uncompletedLines)
    print(f'RES: {res}')
