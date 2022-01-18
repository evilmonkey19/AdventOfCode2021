def findOxigenGeneratorRating(data) -> int:
    for i in range (0, len(data[0])):
        data = findDataWithMostCommonBitBasedOnIndex(data, i)
        if len(data) == 1:
            break
    return int(data[0],2)

def findDataWithMostCommonBitBasedOnIndex(data, index) -> list[str]:
    mostCommonBit = findMostCommonBitBasedOnIndex(data, index)
    return [line for line in data if line[index] == mostCommonBit]

def findMostCommonBitBasedOnIndex(data, index) -> str:
    zeros = 0
    # Find out how many 0s there is in the index
    for line in data:
        zeros += 1 if line[index] == '0' else 0
    return '0' if zeros > len(data) - zeros  else '1'

def findCO2ScruberRating(data) -> int:
    for i in range(0, len(data[0])-1):
        data = findDataWithLessCommonBitBasedOnIndex(data,i)
        if len(data) == 1:
            break
    return int(data[0], 2)

def findDataWithLessCommonBitBasedOnIndex(data, index) -> list[str]:
    lessCommonBit = findLessCommonBitBasedOnIndex(data, index)
    return [line for line in data if line[index] == lessCommonBit]

def findLessCommonBitBasedOnIndex(data, index) -> str:
    zeros = 0
    for line in data:
        zeros += 1 if line[index] == '0' else 0
    return '1' if zeros > len(data)-zeros else '0'


if __name__ == '__main__':
    '''
    data = ['00100', '11110', '10110', '10111', '10101',
            '01111', '00111', '11100', '10000', '11001',
            '00010', '01010'];
    '''
    file = open('data.txt')
    data = file.readlines()
    file.close()
    
    data = [line.strip() for line in data]

    
    ## Find Oxigen generator rate
    oxigen_generator_rate = findOxigenGeneratorRating(data)
    print(oxigen_generator_rate)
    print("==========================")
    CO2_scrubber_rating = findCO2ScruberRating(data)
    print(CO2_scrubber_rating)
    print(oxigen_generator_rate*CO2_scrubber_rating)
    