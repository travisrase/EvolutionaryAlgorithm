public class EvolvAlg{
  String fileName = "no file";
  int populationSize = 0;
  String selectionMethod = "na";
  String crossOverMethod = "na";
  double crossOverProbability = 0.0;
  double mutationProbability = 0.0;
  int numGenerations = 0;
  char algorithm = '';

  public EvolvAlg(fileName, populationSize, selectionMethod, crossOverMethod, crossOverProbability, mutationProbability, numGenerations, algorithm){
    this.fileName = fileName;
    this.selectionMethod = selectionMethod;
    this.crossOverMethod = crossOverMethod;
    this.crossOverProbability = crossOverProbability;
    this.mutationProbability = mutationProbability;
    this.numGenerations = numGenerations;
    this.algorithm = algorithm;
  }
}
