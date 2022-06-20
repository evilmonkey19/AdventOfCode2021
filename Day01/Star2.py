import csv

if __name__ == '__main__':
    data = []
    with open('data.csv', 'r') as csvfile:
        for row in csv.reader(csvfile, delimiter=';'):
            data.append(row[0])
    data = [int(num,10) for num in data]
    counter = 0
    for i in range(3,len(data)):
        if (data[i-2]+data[i-1]+data[i]) > (data[i-3]+data[i-2]+data[i-1]):
            counter += 1
    print(counter)
