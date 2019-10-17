import random
from FitnessEvaluator import FitnessEvaluator  as FA

class GeneticAlgorithm:
    def __init__(self, problem, numVars, numIndividuals, selMethod, crossMethod, crossProb, mutProb, numGens):
        self.problem = problem
        self.numVars = numVars
        self.lenProblem = len(problem)
        self.numIndividuals = int(numIndividuals)
        self.selMethod = selMethod
        self.crossMethod = crossMethod
        self.crossProb = float(crossProb)
        self.mutProb = float(mutProb)
        self.numGens = int(numGens)
        self.FA = FA(problem)

    def solve(self):
        #build initial population randomly
        population = self.buildRandomPop()
        #run a selection, breeding and mutation algorithm for numGens iterations
        for i in range(self.numGens):
            #first select breeding pool from population
            breedingPool = self.selectBreedingPool(population)
            #breed new population from breedingPool
            newPopulation = self.breedNewPop(breedingPool)
            #mutate new population
            population = self.mutatePop(newPopulation)
        profileTuples = self.buildProfileTuples(population)
        sortedProfileTuples = sorted(profileTuples, key=lambda tup: tup[1], reverse=True)
        indexBestSolution = sortedProfileTuples[0][0]
        bestSolution = population[indexBestSolution]
        fitnessRating = sortedProfileTuples[0][1]
        return (fitnessRating, bestSolution)

    #function that will randomly create a population of self.numIndividiuals
    def buildRandomPop(self):
        pop = []
        for i in range(self.numIndividuals):
            sol = self.buildRandomSolution(self.numVars + 1)
            pop += [sol]
        return pop

    #this method will return a breeding pool based on one of three algorithms
    #for selection: rank sort, tournmanet selection, selection by groups
    def selectBreedingPool(self,pop):
        profileTuples = self.buildProfileTuples(pop)
        #use rank sort seclection method
        if(self.selMethod == "rs"):
            breedingPoolIndicies = self.rs(profileTuples)
            breedingPool = [pop[i] for i in breedingPoolIndicies]
            return breedingPool
        elif(self.selMethod == "ts"):
            breedingPoolIndicies = self.ts(profileTuples,5,20)
        else:
            breedingPoolIndicies = self.gr(profileTuples)
        breedingPool = [pop[i] for i in breedingPoolIndicies]
        return breedingPool

    """ incomplete """
    def rs(self, profileTuples):
        sorted_by_second = sorted(profileTuples, key=lambda tup: tup[1], reverse=True)
        res = [index[0] for index in sorted_by_second]
        return res

    def ts(self, profileTuples, n, m):
        indicies = []
        while len(indicies) < len(profileTuples):
            mIndicies = []
            for i in range(m):
                index = random.randrange(len(profileTuples))
                mIndicies += [index]
            mProfileTuples = [profileTuples[i] for i in mIndicies]
            sortedProfileTuples = sorted(mProfileTuples, key=lambda tup: tup[1], reverse=True)
            topNTuples = sortedProfileTuples[0:n]
            topNIndicies = [i[0] for i in topNTuples]
            indicies += topNIndicies
        return indicies[0:len(profileTuples)]

    def gr(self,profileTuples):
        g1 = []
        g2 = []
        for i in range(0,len(profileTuples)-1,2):
            r = random.random()
            if r < 0.5:
                g1 += [profileTuples[i]]
                g2 += [profileTuples[i+1]]
            else:
                g1 += [profileTuples[i+1]]
                g2 += [profileTuples[i]]
        #Evaluate fitness of each group
        f1 = sum([i[1] for i in g1])
        f2 = sum([i[1] for i in g2])
        if (f1 > f2):
            g1 = [i[0] for i in g1]
            return g1 + g1
        else:
            g2 = [i[0] for i in g2]
            return g2 + g2


    def breedNewPop(self,breedingPool):
        newPop = []
        for i in range(0,len(breedingPool)-1,2):
            newSols = self.combine(breedingPool[i], breedingPool[i+1])
            newPop += [newSols[0], newSols[1]]
        return newPop

    def combine(self, solA, solB):
        if self.crossMethod == "1c":
            r = random.random()
            if r < self.crossProb:
                return self.onePointCross(solA,solB)
            else:
                return (solA,solB)
        #by default will use uniform cross
        else:
            return self.uniformCross(solA,solB)

    def onePointCross(self, solA, solB):
        crossOverPoint = random.randrange(len(solA))
        newA = solA[0:crossOverPoint] + solB[crossOverPoint:len(solB)]
        newB = solB[0:crossOverPoint] + solA[crossOverPoint:len(solA)]
        return (newA, newB)

    def uniformCross(self, solA, solB):
        newA = []
        newB = []
        for i in range(len(solA)):
            r = random.random()
            if r < self.crossProb:
                newA += [solB[i]]
                newB += [solA[i]]
            else:
                newA += [solA[i]]
                newB += [solB[i]]
        return(newA,newB)

    def mutatePop(self, pop):
        newPop = []
        for sol in pop:
            newPop += [self.mutateSolution(sol)]
        return newPop

    def mutateSolution(self,sol):
        newSol = []
        for i in sol:
            r = random.random()
            if (r < self.mutProb):
                if (i == 0):
                    newSol += [1]
                else:
                    newSol += [0]
            else:
                newSol += [i]
        return newSol

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
    def buildProfileTuples(self, pop):
        fitnessRatings = [self.FA.evaluateSolution(i) for i in pop]
        profileTuples = []
        breedingPoolIndicies = []
        for i in range(len(fitnessRatings)):
            profileTuples += [(i,fitnessRatings[i])]
        return profileTuples
