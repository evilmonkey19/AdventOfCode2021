import re

sampleData = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
data = open('data.txt', 'r', encoding="utf-8").read()
# data = sampleData
coords_section, folds_section = data.split("\n\n")
coords = {tuple(map(int, c.split(','))) for c in coords_section.splitlines()}
folds = [re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines()]
folds = [(a, int(v)) for a, v in folds]

for axis, v in folds[0:1]:
    if axis == 'y':
        coords = {(x,y) for x,y in coords if y < v} | {(x, v - (y - v)) for x, y in coords if y >= v }
    elif axis == 'x':
        coords = {(x,y) for x,y in coords if x < v} | {(v - (x - v), y) for x,y in coords if x >= v}


print(len(coords))