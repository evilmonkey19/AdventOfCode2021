def getFourDigitOutputStripped(data : str) -> list:
    digits = data.partition('|')[0].strip().split(' ')
    numbers = getEasyNumbers(digits)
    print(numbers)
    input()
    return getCompostNumbers(digits, data)

# Get 1 -> len 2, 4 -> len 4, 7 -> len 3 , 8 -> len 7
def getEasyNumbers(digits : list) -> list:
    for digit in enumerate(digits):
        if (len(digit[1]) == 2) : digits[digit[0]], digits[1] = digits[1], digits[digit[0]]
        elif(len(digit[1]) == 3) : digits[digit[0]], digits[7] = digits[7], digits[digit[0]]
        elif(len(digit[1]) == 4) : digits[digit[0]], digits[4] = digits[4], digits[digit[0]]
        elif(len(digit[1]) == 7) : digits[digit[0]], digits [8] = digits[8], digits[digit[0]]
    return digits

def getCompostNumbers(numbers : list, data : str) -> list:
    return []

    
'''
def countEasyDigits() -> int:
    res = 0
    lenEasyDigits = getLengthEasyDigits()
    for fourDigits in data :
        res += len([d for d in sorted([len(digit) for digit in fourDigits]) if d in lenEasyDigits])
    return res

def getLengthEasyDigits() -> list:
    lenDigits = [len(digit) for digit in digits]
    return sorted([digit for digit in lenDigits if lenDigits.count(digit)==1])

def getFourDigitOutput(line : list) -> int:
    res = 0
    for digit in enumerate(reversed(line)):
        print(''.join(sorted(digit[1])))
        print([x for x in range(len(digits)) if digits[x] == ''.join(sorted(digit[1]))])
        res += 10**digit[0]
    print(res)
    return 0
'''

if __name__ == '__main__':

    # TEST INPUT
    data = [
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
    '''
    
    res = 0
    for line in data :
        numbers = getFourDigitOutputStripped(line)
        #res += getFourDigitOutput(line)
    
    #print("RESULTADO : " + str(countEasyDigits()))