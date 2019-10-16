from FitnessEvaluator import FitnessEvaluator as FA
import random

class PBIL:
    def __init__(self, problem, popSize, learn, negLearn, mutProb, mutShift, numIterations):
        self.fitnessEvaluator = FA(problem)
        self.samples = int(numIterations)
        self.learn = float(learn)
        self.negLearn = float(negLearn)
        self.numBits = int(popSize)
        self.mutProb = float(mutProb)
        self.mutShift = float(mutShift)

    def genSampleVector(self, probabilities):
        sample = []
        for i in range(self.numBits):
            val = random.random()
            if(val > probabilities[i]):
                sample += [1]
            else:
                sample += [0]
        return sample

    def evaluateSolutions(self, sample):
        return self.fitnessEvaluator.evaluateSolution(sample)


    def getBestVector(self, sampleVectors, evaluations):
        maxIndex = 0
        max = 0.0
        for i in range(len(evaluations)):
            if evaluations[i] > max:
                max = evaluations[i]
                maxIndex = i
        return sampleVectors[maxIndex]

    def getWorstVector(self, sampleVectors, evaluations):
        lowIndex = 0
        low = 0.0
        for i in range(len(evaluations)):
            if evaluations[i] < low:
                low = evaluations[i]
                lowIndex = i
        return sampleVectors[lowIndex]

    def solve(self):
        probability = []
        for i in range(self.numBits):
            probability += [0.5]

        for i in range(self.numBits):
            sampleVectors = []
            evaluations = []
            #Generate sample vectors
            for v in range(self.samples):
                val = self.genSampleVector(probability)
                sampleVectors += [val]
                eval = self.evaluateSolutions(val)
                evaluations += [eval]

            bestVector = self.getBestVector(sampleVectors, evaluations)
            print("---------")
            print("i good: ", self.evaluateSolutions(bestVector))
            worstVector = self.getWorstVector(sampleVectors, evaluations)
            print("i bad: ", self.evaluateSolutions(worstVector))
            print()

            #Update the probability vector towards the best solution
            for v in range(self.numBits):
                probability[v] = probability[v] * (1.0 - self.learn) + bestVector[v] * (self.learn)

            """Update the probability vector away from the worst solution"""
            for v in range(self.numBits):
                probability[v] = probability[v] * (1.0 - self.negLearn)
                + bestVector[v] * (self.negLearn)

            """Mutate probability vector"""
            for v in range(self.numBits):
                if random.random() < self.mutProb:
                    mutateDirection = 0
                    if random.random() > 0.5:
                        mutateDirection = 1
                        probability[v] = probability[v] * (1.0 - self.mutShift)
                        + mutateDirection * (self.mutShift)
