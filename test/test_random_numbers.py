import BoxMuller as bm

listA = []
listB = []
listC = []
listD = []


generatorA = bm.uniform_distribution(100.0, 104001.0, 714025.0)
generatorB = bm.uniform_distribution(1001.0, 100000.0, 714025.0)
generatorC = bm.uniform_distribution(137.0, 150887.0, 714025.0)
generatorD = bm.uniform_distribution(1103515245.0, 12345.0, 254635656.0)

#number of random numbers
N = 10000

#generate uniformly distributed random numbers
for i in range(0, N):
    listA.append(next(generatorA))
    listB.append(next(generatorB))
    listC.append(next(generatorC))
    listD.append(next(generatorD))

print(listA[1])

#generate random numbers from a normal distribution
listN = []
generatorN = bm.uniform_distribution(100.0, 104001.0, 714025.0)
generatorNpair = bm.normal_distribution(generatorN, 0.0, 1.0)
for i in range(0, N):
    listN.append(next(generatorNpair))

print(listN[1])