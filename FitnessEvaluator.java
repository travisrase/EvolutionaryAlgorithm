import java.util.Arrays;

public class FitnessEvaluator{
  int numClauses = 0;
  int[][] clauses;

  public FitnessEvaluator(numClauses, clauses){
    this.numClauses = numClauses;
    this.clauses = clauses;
  }

  public double EvaluateSolution(int[] solution){
    int numTrueClauses = 0;
    //evaluate each clause in clauses
    for (int[] clause: clauses){
      //evaluate each varible in the clause
      boolean evaluation = false;
      for (int varIndex: clause){
        //check for negative
        if (varIndex < 0){
          evaluation = !solution[(varIndex*-1)] || evaluation;
        }
        else{
          evaluation = solution[(varIndex)] || evaluation;
        }
      }
      // check to see if clause evaluated to true
      if(evaluation == true){
        // if clause is true increment number of true clauses found
        numTrueClauses++;
      }
    }
    //return percentage of correct clauses
    return (double)numTrueClauses/(double)numClauses
  }
}
