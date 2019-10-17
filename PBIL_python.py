from FitnessEvaluator import FitnessEvaluator as FA
import random

class PBIL:
    def __init__(self, problem, numVariables, popSize, learn, negLearn, mutProb, mutShift, numIterations,):
        self.fitnessEvaluator = FA(problem)
        self.numVariables = int(numVariables)
        self.numIterations = int(numIterations)
        self.learn = float(learn)
        self.negLearn = float(negLearn)
        self.popSize = int(popSize)
        self.mutProb = float(mutProb)
        self.mutShift = float(mutShift)

    def genSampleVector(self, probabilities):
        sample = []
        for i in range(self.numVariables + 1):
            val = random.random()
            if i == 0:
                sample += [0]
            elif(val > probabilities[i]):
                sample += [1]
            else:
                sample += [0]
        return sample

    def evaluateSolutions(self, sample):
        return self.fitnessEvaluator.evaluateSolution(sample)

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

    # def getBestVector(self, sampleVectors, evaluations):
    #     maxIndex = 0
    #     max = 0.0
    #     for i in range(len(evaluations)):
    #         if evaluations[i] > max:
    #             max = evaluations[i]
    #             maxIndex = i
    #     return sampleVectors[maxIndex]
    #
    # def getWorstVector(self, sampleVectors, evaluations):
    #     lowIndex = 0
    #     low = 0.0
    #     for i in range(len(evaluations)):
    #         if evaluations[i] < low:
    #             low = evaluations[i]
    #             lowIndex = i
    #     return sampleVectors[lowIndex]

    def solve(self):
        probability = []
        for i in range(self.numVariables + 1):
            probability += [0.5]

        for i in range(self.popSize):
            sampleVectors = []
            evaluations = []
            #Generate sample vectors
            for v in range(self.numIterations):
                val = self.genSampleVector(probability)
                sampleVectors += [val]
                eval = self.evaluateSolutions(val)
                if eval == 1.0:
                    return val
                evaluations += [eval]

            bestWorstVectors = self.getBestWorstVectors(sampleVectors, evaluations)
            bestVector = bestWorstVectors[0]
            worstVector = bestWorstVectors[1]

            if self.evaluateSolutions(bestVector) == 1.0:
                print("yahtzee", bestVector)
                return bestVector
            #bestVector = self.getBestVector(sampleVectors, evaluations)[0]
            # print("---------")
            # print("i good: ", self.evaluateSolutions(bestVector))
            # #worstVector = self.getWorstVector(sampleVectors, evaluations)
            # print("i bad: ", self.evaluateSolutions(worstVector))
            # print()

            #Update the probability vector towards the best solution
            for v in range(self.numVariables + 1):
                probability[v] = probability[v] * (1.0 - self.learn) + bestVector[v] * (self.learn)

            """Update the probability vector away from the worst solution"""
            for v in range(self.numVariables + 1):
                probability[v] = probability[v] * (1.0 - self.negLearn)
                + bestVector[v] * (self.negLearn)

            """Mutate probability vector"""
            for v in range(self.numVariables + 1):
                if random.random() < self.mutProb:
                    mutateDirection = 0
                    if random.random() > 0.5:
                        mutateDirection = 1
                        probability[v] = probability[v] * (1.0 - self.mutShift)
                        + mutateDirection * (self.mutShift)
        print(":(", bestVector, self.evaluateSolutions(bestVector))
        return bestVector
