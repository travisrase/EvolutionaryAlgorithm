import random

class GeneticAlgorithm:
    def __init__(self, problem, numIndividuals, selMethod, crossMethod, crossProb, mutProb, numGens):
        self.problem = problem
        self.lenProblem = len(problem)
        self.numIndividuals = numIndividuals
        self.selMethod = selMethod
        self.crossMethod = crossMethod
        self.crossProb = crossProb
        self.mutProb = mutProb
        self.numGens = numGens


    def solve():
        population = buildPop()
        for 

    def buildPop():
        pop = []
        for i in range(self.numIndividuals):
            sol = self.buildRandomSolution(self.lenProblem)
            pop += [sol]
        return pop

    def buildRandomSolution(numVars):
        sol = []
        for i in range(numVars):
            sol += [getIndexValue(.5)]

    def getIndexValue(probTrue):
        r = random.random()
        if r < probTrue:
            return 1
        else:
            return 0
