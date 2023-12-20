import numpy as np
from scipy.signal import convolve2d

def enhance(data, n_times):
    algorithm = [int(x == '#') for x in data[0]]
    img = np.array([[int(x == '#') for x in y] for y in data[2:]])

    matrix = np.array([[2**0,2**1,2**2], [2**3,2**4,2**5], [2**6,2**7,2**8]])
    fillvalue = 0

    for _ in range(n_times):
        idx = convolve2d(img, matrix, fillvalue=fillvalue)
        img = np.vectorize(lambda x: algorithm[x])(idx)
        fillvalue = algorithm[0] if fillvalue == 0 else algorithm[2**9-1]
    return img

dataSample = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###\
"""

# data = dataSample

data = open('data.txt', 'r', encoding='utf-8').read()
data = data.splitlines()

img = enhance(data, 2)

print(sum([sum(x) for x in img]))

