import random
from FitnessEvaluator import FitnessEvaluator  as FA

class GeneticAlgorithm:
    def __init__(self, problem, numVars, numIndividuals, selMethod, crossMethod, crossProb, mutProb, numGens):
        self.numVars = numVars
        self.lenProblem = len(problem)
        self.numIndividuals = int(numIndividuals)
        self.selMethod = selMethod
        self.crossMethod = crossMethod
        self.crossProb = float(crossProb)
        self.mutProb = float(mutProb)
        self.numGens = int(numGens)
        self.FA = FA(problem)
        self.rsProbabilityTable = self.buildProbabilityTable()
        self.solutionFound = False

    def solve(self):
        #build initial population randomly
        population = self.buildRandomPop()
        currentIteration = 1
        #run a selection, breeding and mutation algorithm for numGens iterations
        for i in range(self.numGens):
            #first select breeding pool from population
            breedingPool = self.selectBreedingPool(population)
            #check to see if solution has been found
            if breedingPool[0] == -1:
                break
            #breed new population from breedingPool
            newPopulation = self.breedNewPop(breedingPool)
            #mutate new population
            population = self.mutatePop(newPopulation)
            if (self.solutionFound):
                break
            elif(i < self.numGens-1):
                currentIteration += 1

        profileTuples = self.buildProfileTuples(population)
        sortedProfileTuples = sorted(profileTuples, key=lambda tup: tup[1], reverse=True)
        indexBestSolution = sortedProfileTuples[0][0]
        bestSolution = population[indexBestSolution]
        fitnessRating = sortedProfileTuples[0][1]
        return self.formatSolution(bestSolution, fitnessRating, currentIteration)

    #function that will randomly create a population of self.numIndividiuals
    def buildRandomPop(self):
        pop = []
        for i in range(self.numIndividuals):
            sol = self.buildRandomSolution()
            pop += [sol]
        return pop

    #this method will return a breeding pool based on one of three algorithms
    #for selection: rank sort, tournmanet selection, selection by groups
    def selectBreedingPool(self,pop):
        profileTuples = self.buildProfileTuples(pop)
        sortedProfileTuples = sorted(profileTuples, key=lambda tup: tup[1], reverse=True)
        if (sortedProfileTuples[0][1] == 1.0):
            self.solutionFound = True
            return [-1]
        #use rank sort seclection method
        if(self.selMethod == "rs"):
            breedingPoolIndicies = self.rs(sortedProfileTuples)
            breedingPool = [pop[i] for i in breedingPoolIndicies]
            return breedingPool
        elif(self.selMethod == "ts"):
            breedingPoolIndicies = self.ts(profileTuples,5,20)
        else:
            breedingPoolIndicies = self.gr(profileTuples)
        breedingPool = [pop[i] for i in breedingPoolIndicies]
        return breedingPool

    #this method given an input of sorted profile tuples will return an array
    #of length popSize of integer indicis of solutions. This method chooses a solution
    # of rank i with probability 1/(sum(k) k: 0->i)
    def rs(self, sortedProfileTuples):
        rankedIndicies = [index[0] for index in sortedProfileTuples]
        selectedIndicies = []
        for i in range(self.numIndividuals):
            rank = self.generateRSIndex()
            selectedIndicies += [rankedIndicies[rank]]
        return selectedIndicies

    #this method uses a proabability table to generate i with probability 1/(sum(k) k: 0->i)
    def generateRSIndex(self):
        r = random.randrange(0,len(self.rsProbabilityTable))
        return self.rsProbabilityTable[r]

    #this method builds a probability table used to geenrate rs indicis.
    #the table has more indicies assigned to numbers of higher rank. More specfically
    #for each index i there are numIndividuals - i indicies in the array assigned to
    #i
    def buildProbabilityTable(self):
        table = []
        for i in range (1,self.numIndividuals+1):
            table += [i]*(self.numIndividuals - i)
        return table

    #this method implements tournament selection in which m random solutions are chosen
    #and the best n are added to the breeding pool. This process is repeated until
    #popSize solutions have been chosen.
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

    #In group selection the population is split into two random groups and the aggregate
    #fitness of each group is computed. The group with the highest fitness is doubles and returned
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

    #for a given breeding pool, solutions are recombined with neighboring solutions,
    #to generate a new population of the same size.
    def breedNewPop(self,breedingPool):
        newPop = []
        for i in range(0,len(breedingPool)-1,2):
            newSols = self.combine(breedingPool[i], breedingPool[i+1])
            newPop += [newSols[0], newSols[1]]
        return newPop

    #this method combines a solution A and B from the breeding pool using
    #either 1 point cross or uniform cross based on terminal input paramters.
    #If 1 point cross is selected then the 1c method is called with probability
    #cross prob, otherwise the origonal solutions are returned
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

    #this method, given two solutions will switch the values that come after
    #and before a random index i in solution A and B.
    def onePointCross(self, solA, solB):
        crossOverPoint = random.randrange(len(solA))
        newA = solA[0:crossOverPoint] + solB[crossOverPoint:len(solB)]
        newB = solB[0:crossOverPoint] + solA[crossOverPoint:len(solA)]
        return (newA, newB)

    #this method implements a uniform cross scheme in which for a given index i of
    #solution A and B it will switch the value of solA and solB with probability crossProb
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

    #this method iterates through all solutions in the population and runs a mutation
    #algorithm on each solution.
    def mutatePop(self, pop):
        newPop = []
        for sol in pop:
            newPop += [self.mutateSolution(sol)]
        return newPop

    #this method, given a solution, will iterate through all indicies and flip
    #a 0 or 1 with probability mutProb.
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

    #This method will build a ranodm solution of 0's and 1's of length numVars
    def buildRandomSolution(self):
        sol = []
        for i in range(self.numVars+1):
            sol += [self.getIndexValue(.5)]
        return sol

    #Given a percetnatge of a random value being true. This method will return
    # a 1 with probability probTrue and a 0 with probability 1-probTrue
    def getIndexValue(self,probTrue):
        r = random.random()
        if r < probTrue:
            return 1
        else:
            return 0

    #This method, given a populatino of solutions, will generate a tuple containing
    #the index of the solution in the given population list, and then a fitness ranking.
    def buildProfileTuples(self, pop):
        fitnessRatings = [self.FA.evaluateSolution(i) for i in pop]
        profileTuples = []
        breedingPoolIndicies = []
        for i in range(len(fitnessRatings)):
            profileTuples += [(i,fitnessRatings[i])]
        return profileTuples

    #formats and returns a dictionary to be sent to EvolvAlg for final output
    def formatSolution(self, solution, evaluation, iteration):
        solutionDict = {}
        numClauses = self.FA.getNumClauses()
        solutionDict["numClauses"] = numClauses
        solutionDict["percentage"] = evaluation
        solutionDict["trueClauses"] = int(numClauses * evaluation)
        solutionDict["solution"] = solution
        solutionDict["iteration"] = iteration
        return solutionDict
