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

for step in range(10):
    chain_pairs = [chain[i:i+2] for i in range(0, len(chain)-1)]
    res_chain = f"{chain[0]}"
    for chain_pair in chain_pairs:
        if chain_pair in rules:
            middle_index = len(chain_pair) // 2
            res_chain += rules[chain_pair] + chain_pair[middle_index:]
    chain = res_chain

counter = Counter(chain)
counters = counter.most_common()
num_ocurrences_most_common_letter = counters[0][1]
num_ocurrences_least_common_letter = counters[-1][1]
print(num_ocurrences_most_common_letter - num_ocurrences_least_common_letter)

