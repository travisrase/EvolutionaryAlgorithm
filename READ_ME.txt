READ ME

TITLE: EvolutionaryAlgorithm
AUTHORS: twrase, cjfitzge
LANGUAGE: Python3
PURPOSE: The object-oriented program, EvolutionaryAlgorithm, that we have
implemented uses two different types of nature-inspired algorithms in an attempt to satisfy different MAXSAT tests. The first of these algorithms
is called Genetic Algorithms, which seeks to rank and breed individuals 
and then have them reproduce, eventually converging on a maximum 
satisfiability. The other optimization algorithm, Population-based 
Incremental Learning (or PBIL), uses competitive supervised learning 
as its main evolution metric by ways of the generation and manipulation 
of a population and probability vector. The main purpose of this project 
is to determine which of the two algorithms is more efficient for various
test metrics. 

INSTRUCTIONS:
From the command line, our program can be run by typing 
"Python3 EvolvAlg.py [test_name.cnf] [numBits] [selMethod/learn_rate] 
[crossMethod/negLearn] [crossProb/mutProb] [mutProb/mutShift] [g/p]"
The elements within brackets within quotes are different parameters by
which the person running the program can manipulate the algorithm. The
first element in each of the brackets with a "/" in them indicates that
it is used for the first algorithm, GA, and vice versa for PBIL.

Our program will output the following:
	1. The name of the MAXSAT problem.
	2. The number of variables and clauses in the problem.
	3. The number and percentage of clauses that the best assignment
	   found by our algorithm satisfies.
	4. The assignment that achieves those results.
	5. The iteration during which the best assignment was found. 