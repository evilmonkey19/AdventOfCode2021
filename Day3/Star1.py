if __name__ == '__main__':
    '''
    data = ['00100', '11110', '10110', '10111', '10101',
            '01111', '00111', '11100', '10000', '11001',
            '00010', '01010'];
    '''
    file = open('data.txt')
    data = file.readlines()
    file.close()


    gamma = [0] * (len(data[0])-1)
    epsilon = [0] * (len(data[0])-1)
    for line in data:
        line = line.strip()
        for i in range(0,len(line)-1):
            gamma[i] += int(line[i])
    gamma = [1 if i>(len(data)/2) else 0 for i in gamma]
    epsilon = [0 if i else 1 for i in gamma]
    gamma_res = 0
    epsilon_res = 0
    for i in range(0, len(data[0])-1):
        gamma_res += gamma[-i-1]*2**i;
        epsilon_res += epsilon[-i-1]*2**i;

    print(gamma_res)
    print(epsilon_res)
    print(gamma_res*epsilon_res)
