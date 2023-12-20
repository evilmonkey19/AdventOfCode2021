import re

sampleData = \
"""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

# sampleData = "[[[[[9,8],1],2],3],4]"

def parse_snailfish(n):
    v = re.split(r"(\[|\]|,)", n)
    v = [x for x in v if x not in ("", ",")]
    v = [int(x) if x.isdigit() else x for x in v]
    return v

def add(a, b):
    return ['['] + a + b + [']']


def explode(n):
    depth = 0
    for i, s in enumerate(n):
        if s == '[':
            depth += 1
        elif s == ']':
            depth -= 1
        if (
            depth > 4 \
            and s == '[' \
            and isinstance(n[i+1], int) \
            and isinstance(n[i+2], int) \
            and n[i+3] == ']'
        ):
            for j in range(i, 0, -1):
                if isinstance(n[j], int):
                    n[j] += n[i+1]
                    break
            for j in range(i+4, len(n)):
                if isinstance(n[j], int):
                    n[j] += n[i+2]
                    break
            n = n[:i] + [0] + n[i + 4 :]
            return n, True
    return n, False

def split(n):
    for i,s in enumerate(n):
        if isinstance(s, int) and s >= 10:
            n = n[:i] + ['[', s//2, s-s//2,']'] + n[i + 1:]
            return n, True
    return n, False

def reduce(n):
    to_reduce = True
    while to_reduce:
        n, to_reduce = explode(n)
        if not to_reduce:
            n, to_reduce = split(n)
    return n

def magnitude(n):
    while len(n) > 1:
        for i, s in enumerate(n):
            if (
                s == '[' \
                and isinstance(n[i+1], int) \
                and isinstance(n[i+2], int) \
                and n[i+3] == ']'
            ):
                n = n[:i] + [3*n[i+1] + 2*n[i+2]] + n[i + 4:]
                break
    return n[0]


# data = sampleData
data = open('data.txt', 'r', encoding='utf-8').read()
data = data.splitlines()

m = parse_snailfish(data[0])
for d in data[1:]:
    n = parse_snailfish(d)
    m = add(m,n)
    m = reduce(m)
print(magnitude(m))