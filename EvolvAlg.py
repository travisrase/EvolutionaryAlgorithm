import sys
import GeneticAlgorithm.GeneticAlgorithm as GA
import PBIL.PBIL as PB
import FitnessEvaluator.FitnessEvaluator as FE

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

    def run():
        readFile(self.fileName)
        if(alg == "g"):
            ga = GA()
            ga.solve()
        else:
            pb = PB()
            pb.solve()



#Run Program
fileName = sys.argv[0]
popSize = sys.argv[1]
selMethod = sys.argv[2]
crossMethod = sys.argv[3]
crossProb = sys.argv[4]
mutProb = sys.argv[5]
numGen = sys.argv[6]
alg = sys.argv[7]

eA = EvolvAlg(fileName,popSize,selMethod,crossMethod, crossProb,mutProb,numGen,alg)
eA.run()
