#############################
##                         ##
##          a a a a        ##
##         b       c       ##
##         b       c       ##
##          d d d d        ##
##         e       f       ##
##         e       f       ##
##          g g g g        ##
##                         ##
#############################

def getStringNumbers(line : str) -> list:
    data = line.partition('|')[0].strip().split(' ')
    numbers_dict = findNumberDict(data)
    numbers_dict = reverseKeysAndValuesOnDict(numbers_dict)
    return numbers_dict

def reverseKeysAndValuesOnDict(originalDict : dict) -> dict:
    new_dict = {}
    for k, v in originalDict.items():
        new_dict[v] = k
    return new_dict

def findNumberDict(data : str) -> dict:
    numbers_dict = {new_list: '' for new_list in range(10)}
    numbers_dict = get0to3(numbers_dict, data)
    numbers_dict = get4to6(numbers_dict, data)
    numbers_dict = get7to9(numbers_dict, data)
    return numbers_dict

def get0to3(originalNumbers_dict : dict, data : str) -> dict:
    numbers_dict = dict(originalNumbers_dict)
    numbers_dict[0] = ''.join(sorted(get0Str(data)))
    numbers_dict[1] = ''.join(sorted(get1Str(data)))
    numbers_dict[2] = ''.join(sorted(get2Str(data)))
    numbers_dict[3] = ''.join(sorted(get3Str(data)))
    return numbers_dict

def get4to6(originalNumbers_dict : dict, data : str) -> dict:
    numbers_dict = dict(originalNumbers_dict)
    numbers_dict[4] = ''.join(sorted(get4Str(data)))
    numbers_dict[5] = ''.join(sorted(get5Str(data)))
    numbers_dict[6] = ''.join(sorted(get6Str(data)))
    return numbers_dict

def get7to9(originalNumbers_dict : dict, data : str) -> dict:
    numbers_dict = dict(originalNumbers_dict)
    numbers_dict[7] = ''.join(sorted(get7Str(data)))
    numbers_dict[8] = ''.join(sorted(get8Str(data)))
    numbers_dict[9] = ''.join(sorted(get9Str(data)))
    return numbers_dict


# 0 is length 6  : "abcefg"
def get0Str(data : list) -> str:
    for n in data:
        if len(n) == 6:
            if not(all([digit in n for digit in get4Str(data)])) and all([digit in n for digit in get1Str(data)]):
                return n
            

# 1 is length 2 : "cf"      [UNIQUE in length]
def get1Str(data : list) -> str:
    for n in data:
        if len(n) == 2:
            return n

# 2 is length 5 : "acdeg"
def get2Str(data : list) -> str:
    for n in data:
        if len(n) == 5:
            if sum([digit in get4Str(data) for digit in n]) == 2:
                return n

# 3 is length 5 : "acdfg"
def get3Str(data : list) -> str:
    for n in data:
        if len(n) == 5:
            if all([digit in n for digit in get1Str(data)]):
                return n

# 4 is length 4 : "bcdf"    [UNIQUE in length]
def get4Str(data : list) -> str:
    for n in data:
        if len(n) == 4:
            return n

# 5 is length 5 : "abdfg"
def get5Str(data : list) -> str:
    for n in data:
        if len(n) == 5:
            if all([digit in get6Str(data) for digit in n]):
                return n

# 6 is length 6 : "abdefg"
def get6Str(data : list) -> str:
    for n in data:
        if len(n) == 6:
            if not(all([digit in n for digit in get1Str(data)])):
                return n

# 7 is length 3 : "acf"     [UNIQUE in length]
def get7Str(data : list) -> str:
    for n in data:
        if len(n) == 3:
            return n

# 8 is length 7 : "abcdefg"   [UNIQUE in length]
def get8Str(data : list) -> str:
    for n in data:
        if len(n) == 7:
            return n

# 9 is length 6 : "abcdfg"
def get9Str(data : list) -> str:
    for n in data:
        if len(n) == 6:
            if all([digit in n for digit in get4Str(data)]):
                return n

def getOutput(line : str, numbers_dict : dict) -> int:
    res = 0
    data = line.partition('|')[2].strip().split(' ')
    for n in enumerate(reversed(data)):
        res += numbers_dict[''.join(sorted(n[1]))] * 10**n[0]
    return res



if __name__ == '__main__':
    '''
    # TEST INPUT
    data = [
        #'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf',
        'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
        'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
        'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
        'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
        'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
        'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
        'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
        'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
        'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
        'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
    ]
    '''
    file = open('data.txt')
    data = file.readlines()
    file.close()
    data = [line.strip() for line in data]
    
    
    res = 0
    for line in data :
        numbers_dict = getStringNumbers(line)
        res += getOutput(line, numbers_dict)
    
    print("RESULTADO : " + str(res))