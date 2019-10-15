class PBIL:
    def __init__(self, fitnessEvaluator, samples, learn, negLearn, numBits, MutProbability, mutShift):
        self.fitnessEvaluator = fitnessEvaluator
        self.samples = samples
        self.learn = learn
        self.negLearn = negLearn
        self.numBits = numBits
        self.mutProbability = mutProbability
        self.mutShift = mutShift

    def genSampleVector(probabilities):
        Random rand = new Random()
        sample = []
        for i in numBits:
            sample[i] = rand.nextInt(2);
        return sample

    def evaluateSolutions(sample):
        // call the fitness function on the sample vector @ that index
        return fitness.EvaluateSolution(sample)


    def getBestVector(sampleVectors, evaluations):
        maxIndex = 0
        max = 0.0
        for i in range(len(evaluations)):
            if evaluations[i] > max:
                max = evaluations[i]
                maxIndex = i
        return sampleVectors[maxIndex]

    def getWorstVector(sampleVectors, evaluations):
        lowIndex = 0
        low = 0.0
        for i in range(len(evaluations)):
            if evaluations[i] < low:
                low = evaluations[i]
                lowIndex = i
        return sampleVectors[lowIndex]

    def solve():
        probability = []
        for i in range(self.numBits):
            probability[i] = 0.5
        while ...
            sampleVectors = []
            evaluations = []
            """Generate sample vectors"""
            for i in range(self.samples):
                sampleVectors[i] = genSampleVector(probability)
                evaluations[i] = evaluateSolutions(sampleVectors[i])

            bestVector = getBestVector(sampleVectors, evaluations)
            worstVector = getWorstVector(sampleVectors, evaluations)

            """Update the probability vector towards the best solution"""
            for i in range(self.numBits):
                probability[i] = probability[i] * (1.0 - self.learn)
                                    + bestVector[i] * (self.learn)

            """Update the probability vector away from the worst solution"""
            for i in range(self.numBits):
                probability[i] = probability[i] * (1.0 - self.negLearn)
                                    + bestVector[i] * (self.negLearn)

            """Mutate probability vector"""
            for i in range(self.numBits)
                if random.random() < self.mutProbability:
                    mutateDirection = 0
                    if random.random() > 0.5:
                        mutateDirection = 1
                    probability[i] = probability[i] * (1.0 - self.mutShift)
                                        + mutateDirection * (self.mutShift)
