""" This class takes one parameter in its constructor and that is
an array of int clauses. Given this input, it can evaluate variable
assignment solutions to the given set of clauses. It returns the percentage
of clauses correctly assiged. """

class FitnessEvaluator:
    def __init__(self, clauses):
        self.clauses = clauses
        self.numClauses = len(clauses)

    #getter method for number of clauses.
    def getNumClauses(self):
        return self.numClauses

    #given a solution as an array of 0's and 1's corresponding to true and false
    #variables assignments respectively, it will evaluate the initialized MAX-SAT
    #problem with the given solution and return the percentage of true clauses. 
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
        return (numTrueClauses)/(self.numClauses)
