import sys
from GeneticAlgorithm import GeneticAlgorithm  as GA
from PBIL_python import PBIL as PB
import FitnessEvaluator as FE

class EvolvAlg:
    def __init__(self, fileName, popSize, selMethod, crossMethod, crossProb, mutProb, numGen,alg):
        self.fileName = fileName
        self.popSize = popSize
        self.selMethod = selMethod
        self.crossMethod = crossMethod
        self.crossProb = crossProb
        self.mutProb = mutProb
        self.numGen = numGen
        self.alg = alg
        self.problem = []

    def readFile(self, fileName):
        file = open(fileName, "r+")
        inp = file.readlines()
        inp = [line.strip("\n") for line in inp]
        for r in inp:
            cleanRow = []
            row = r.split(" ")
            try:
                for var in row:
                    var = int(var)
                    if var != 0:
                        cleanRow += [var]
                self.problem += [cleanRow]
            except:
                continue

    def run(self):
        self.readFile(self.fileName)
        print("self.alg: ", self.alg)
        if(self.alg == "g"):
            ga = GA(self.problem, self.popSize, self.selMethod, self.crossMethod, self.crossProb, self.mutProb, self.numGen)
            ga.solve()
        else:
            pb = PB(self.problem, self.popSize, self.selMethod, self.crossMethod, self.crossProb ,self.mutProb, self.numGen)
            pb.solve()

#Run Program
fileName = sys.argv[1]
popSize = sys.argv[2]
selMethod = sys.argv[3]
crossMethod = sys.argv[4]
crossProb = sys.argv[5]
mutProb = sys.argv[6]
numGen = sys.argv[7]
alg = sys.argv[8]
print("fileName: ", fileName)
print("popSize: ", popSize)
print("selMethod: ", selMethod)
print("crossMethod: ", crossMethod)
print("crossProb: ", crossProb)
print("mutProb: ", mutProb)
print("numGen: ", numGen)
print("alg: ", alg)

eA = EvolvAlg(fileName,popSize,selMethod,crossMethod, crossProb,mutProb,numGen,alg)
eA.run()
