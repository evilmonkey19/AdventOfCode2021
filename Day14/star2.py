from collections import Counter
sampleData = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

data = open('data.txt', 'r', encoding="utf-8").read()
# data = sampleData

chain, rules = data.split("\n\n")
rules = {rule.split(' -> ')[0]:rule.split(' -> ')[1] for rule in rules.split("\n")}

pairs = Counter([chain[i:i+2] for i in range(len(chain) -1 )])

for _ in range(40):
    new_pairs = Counter()
    for p, v in pairs.items():
        if p in rules:
            c = rules[p]
            new_pairs[p[0] + c] += v
            new_pairs[c + p[1]] += v
        else:
            new_pairs[p] += pairs[p]
    pairs = new_pairs

count = Counter()
for p, v in pairs.items():
    count[p[0]] += v
count[chain[-1]] += 1

print(count.most_common()[0][1] - count.most_common()[-1][1])