from FitnessEvaluator import FitnessEvaluator as FA
import random

class PBIL:
    def __init__(self, problem, numVariables, popSize, learn, negLearn, mutProb, mutShift, numGenerations):
        self.fitnessEvaluator = FA(problem)
        self.numVariables = int(numVariables)
        self.numGens = int(numGenerations)
        self.learn = float(learn)
        self.negLearn = float(negLearn)
        self.popSize = int(popSize)
        self.mutProb = float(mutProb)
        self.mutShift = float(mutShift)

    #This method is used to solve the given MAXSAT problem calling on various
    #helper methods to get that task done. Returns a dictionary used for final
    #output in EvolvAlg.
    def solve(self):
        probability = []
        #start population vector with all .5
        for i in range(self.numVariables + 1):
            probability += [0.5]

        #run numIterations iterations of the algorithm
        for i in range(self.numGens):
            sampleVectors = []
            evaluations = []
            #Generate sample vectors
            for v in range(self.popSize):
                sVector = self.genSampleVector(probability)
                sampleVectors += [sVector]
                eval = self.evaluateSolutions(sVector)
                if eval == 1.0:
                    return self.formatSolution(sVector, eval, (v + 1))
                evaluations += [eval]

            bestWorstVectors = self.getBestWorstVectors(sampleVectors, evaluations)
            bestVector = bestWorstVectors[0]
            worstVector = bestWorstVectors[1]

            #Update the probability vector towards the best solution
            for v in range(self.numVariables + 1):
                probability[v] = probability[v] * (1.0 - self.learn) + bestVector[v] * (self.learn)

            #Update the probability vector away from the worst solution
            for v in range(self.numVariables + 1):
                if (bestVector[v] != worstVector[v]):
                    probability[v] = probability[v] * (1.0 - self.negLearn)
                    + bestVector[v] * (self.negLearn)

            #Mutate probability vector
            for v in range(self.numVariables + 1):
                if random.random() < self.mutProb:
                    mutateDirection = 0
                    if random.random() > 0.5:
                        mutateDirection = 1
                        probability[v] = probability[v] * (1.0 - self.mutShift)
                        + mutateDirection * (self.mutShift)
        return self.formatSolution(bestVector, self.evaluateSolutions(bestVector),
                                    self.numGens)

    #This method generates a sample vector based on the various elements of the
    #probability vector parameter.
    def genSampleVector(self, probabilities):
        sample = []
        for i in range(self.numVariables + 1):
            val = random.random()
            if i == 0:
                sample += [0]
            elif(val  > probabilities[i]):
                sample += [1]
            else:
                sample += [0]
        return sample

    def evaluateSolutions(self, sample):
        return self.fitnessEvaluator.evaluateSolution(sample)

    #Given a list of sample vectors and a list of evaluations, this method
    #returns a tuple of the index of the best and worst vectors.
    def getBestWorstVectors (self, sampleVectors, evaluations):
        maxIndex = 0
        max = 0.0
        low = 0.0
        lowIndex = 0
        for i in range(len(evaluations)):
            if evaluations[i] > max:
                max = evaluations[i]
                maxIndex = i
            if evaluations[i] < low:
                low = evaluations[i]
                lowIndex = i
        return (sampleVectors[maxIndex], sampleVectors[lowIndex])

    #formats and returns a dictionary to be sent to EvolvAlg for final output
    def formatSolution(self, solution, evaluation, iteration):
        solutionDict = {}
        #solutionDict["file"] = self.problem
        #solutionDict["numVariables"] = self.numVariables
        numClauses = self.fitnessEvaluator.getNumClauses()
        solutionDict["numClauses"] = numClauses
        solutionDict["percentage"] = evaluation
        solutionDict["trueClauses"] = int(numClauses * evaluation)
        solutionDict["solution"] = solution
        solutionDict["iteration"] = iteration
        return solutionDict
