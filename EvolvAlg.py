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
        self.numVariables = 0

    def readFile(self, fileName):
        file = open(fileName, "r+")
        inp = file.readlines()
        inp = [line.strip("\n") for line in inp]
        for r in inp:
            cleanRow = []
            row = r.split(" ")
            if row[0] == "c":
                continue
            elif row[0] == "p":
                try:
                    self.numVariables = int(row[2])
                except:
                    continue
            else:
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
        if(self.alg == "g"):
            ga = GA(self.problem, self.numVariables, self.popSize, self.selMethod, self.crossMethod, self.crossProb, self.mutProb, self.numGen)
            solution = ga.solve()
            #print(solution)
        else:
            pb = PB(self.problem, self.numVariables, self.popSize, self.selMethod, self.crossMethod, self.crossProb ,self.mutProb, self.numGen)
            solution = pb.solve()
        print("Filename: " + self.fileName)
        print("Number of Variables: " + str(self.numVariables) + ", Number of clauses: " + str(solution["numClauses"]))
        print("Number of true clauses: " + str(solution["trueClauses"]) + ", Percent true clauses: " + str(solution["percentage"]))
        print("Variable assignment: " + str(solution["solution"]))
        print("Number of iterations needed: " + str(solution["iteration"]))

#Run Program
fileName = sys.argv[1]
popSize = sys.argv[2]
selMethod = sys.argv[3]
crossMethod = sys.argv[4]
crossProb = sys.argv[5]
mutProb = sys.argv[6]
numGen = sys.argv[7]
alg = sys.argv[8]

eA = EvolvAlg(fileName,popSize,selMethod,crossMethod, crossProb,mutProb,numGen,alg)
eA.run()
