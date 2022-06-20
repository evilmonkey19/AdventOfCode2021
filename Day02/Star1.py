if __name__ == '__main__':
    file = open('data.txt')
    data = file.readlines()
    file.close()

    width = 0
    depth = 0

    for line in data:
        value = [int(s) for s in line.split() if s.isdigit()]
        if(line.startswith('forward')):
            width += value[0]
        elif(line.startswith('down')):
            depth += value[0]
        elif(line.startswith('up')):
            depth -= value[0]

    print(width)
    print(depth)
    print(width*depth)
