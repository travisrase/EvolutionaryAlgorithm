import random
from FitnessEvaluator import FitnessEvaluator  as FA

class GeneticAlgorithm:
    def __init__(self, problem, numIndividuals, selMethod, crossMethod, crossProb, mutProb, numGens):
        self.problem = problem
        self.lenProblem = len(problem)
        self.numIndividuals = int(numIndividuals)
        self.selMethod = selMethod
        self.crossMethod = crossMethod
        self.crossProb = crossProb
        self.mutProb = mutProb
        self.numGens = int(numGens)
        self.FA = FA(problem)

    def solve(self):
        #build initial population randomly
        population = self.buildRandomPop()
        for i in range(self.numGens):
            breedingPool = self.selectBreedingPool(population)

    def buildRandomPop(self):
        pop = []
        for i in range(self.numIndividuals):
            sol = self.buildRandomSolution(self.lenProblem)
            pop += [sol]
        return pop

    def selectBreedingPool(self,pop):
        fitnessRatings = [self.FA.evaluateSolution(i) for i in pop]
        if(self.selMethod == "rs"):
            breedingPool = self.rs(fitnessRatings)
            print(breedingPool)
            return breedingPool
        else:
            print()

    def rs(self, fitnessRatings):
        profileTuples = []
        for i in range(len(fitnessRatings)):
            profileTuples += [(i,fitnessRatings[i])]
        sorted_by_second = sorted(profileTuples, key=lambda tup: tup[1])
        res = [index[0] for index in sorted_by_second]
        return res

    def buildRandomSolution(self,numVars):
        sol = []
        for i in range(numVars):
            sol += [self.getIndexValue(.5)]
        return sol

    def getIndexValue(self,probTrue):
        r = random.random()
        if r < probTrue:
            return 1
        else:
            return 0
