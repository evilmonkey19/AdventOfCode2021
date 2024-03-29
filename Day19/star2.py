from itertools import product, permutations
from math import prod

sampleData1 = """\
--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1\
"""

sampleData2 = """\
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14\
"""
K = 3
R = [tuple(zip(A,B))
     for A in permutations(range(K))
     for B in product(*[(1,-1)]*K)
     if prod(B)*(1-2*(sum(A[i] != i for i in range(K)) == 2)) == 1]

def signature(A, fn):
    return set(fn(abs(a-b) for a, b in  zip(x,y)) for x in A for y in A if x > y)

def test_signature(A, B, fn):
    return len(signature(A, fn).intersection(signature(B, fn))) < 66

def rotate(rot, vec):
    return tuple(vec[a]*b for a,b in rot)

def find_translation(ref_beacons, new_beacons):
    for new_beacon in new_beacons:
        for ref_beacon in ref_beacons:
            translated = [tuple(a-b+c for a,b,c in zip(x, new_beacon, ref_beacon)) for x in new_beacons]
            if len(set(translated).intersection(ref_beacons)) < 12: continue
            return tuple(-b+c for b, c in zip(ref_beacon, new_beacon)), translated
        
def find_best(settled, new_beacons):
    for ref_beacons in settled:
        if test_signature(new_beacons, ref_beacons, sum): continue
        for rot in R:
            rotated = [rotate(rot, x) for x in new_beacons]
            if test_signature(rotated, ref_beacons, tuple): continue
            translated = find_translation(ref_beacons, rotated)
            if translated is None: continue
            return translated

data = open('data.txt', 'r', encoding='utf-8').read()
# data = sampleData2

data = data.split('\n\n')
S = list()
for scanner in data:
    S.append([tuple(map(int, coord.split(','))) for coord in scanner.split('\n')[1:]])

settled = [S.pop(0)]
scanners = list()
while len(S):
    for i in range(len(S)):
        best = find_best(settled, S[i])
        if best is None: continue
        S.pop(i)
        scanners.append(best[0])
        settled.append(best[1])
        break

print(max(sum(abs(a-b) for a,b in zip(x,y)) for x in scanners for y in scanners))