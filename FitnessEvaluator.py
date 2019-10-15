class FitnessEvaluator:
    def __init__(self, clauses):
        self.clauses = clauses
        self.numCluases = len(clauses)

    def evaluateSolution(solution):
        numTrueClauses = 0;
        for clause in clauses:
            #evaluate each varible in the clause
            evaluation = false
            for varIndex in clause:
                #check for negative
                if varIndex < 0 :
                    evaluation = !solution[(varIndex*-1)] || evaluation
                else:
                    evaluation = solution[(varIndex)] || evaluation
            #check to see if clause evaluated to true
            if(evaluation):
            # if clause is true increment number of true clauses found
            numTrueClauses += 1;
        #return percentage of correct clauses
        return double(numTrueClauses)/double(numClauses)
