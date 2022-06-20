def getFourDigitOutputString(data : str) -> list:
    return data.partition('|')[-1].strip().split(' ')

# Approach : compare the length because it is unique
def countEasyDigits(data : list) -> int:
    res = 0
    for n in data:
        if(isItEasyDigit(n)):
            res += 1
    return res


def isItEasyDigit(number : str) -> bool:
    easyDigitsLength = {2, 3, 4, 7}
    return len(number) in easyDigitsLength

if __name__ == '__main__':
    '''
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
    
    res = 0
    for line in data :
        numbers = getFourDigitOutputString(line)
        res += countEasyDigits(numbers)
    
    print("RESULTADO : " + str(res))