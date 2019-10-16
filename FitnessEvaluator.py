class FitnessEvaluator:
    def __init__(self, clauses):
        self.clauses = clauses
        self.numCluases = len(clauses)

    def evaluateSolution(self,solution):
        numTrueClauses = 0;
        for clause in self.clauses:
            #evaluate each varible in the clause
            evaluation = 0
            for varIndex in clause:
                #check for negative
                if varIndex < 0 :
                    evaluation = solution[(varIndex*(-1))] + evaluation
                else:
                    evaluation = solution[(varIndex)] + evaluation
            #check to see if clause evaluated to true
            if(evaluation > 0):
                # if clause is true increment number of true clauses found
                numTrueClauses += 1
        #return percentage of correct clauses
        return (numTrueClauses)/(self.numCluases)
