# Laboratory_10- Evolutionary Algorithms

## Evolutionary Computation
- Evolutionary computation is a subfield of artificial intelligence (AI) that involves combinatorial optimization problems.
- Nature inspired algorithms that are based on the principles of natural selection and genetics.
- Inspired of survival of the fittest
- Flow: 
- Initialize population ( parameters -> chromosomes -> population)
- Evaluate population (fitness function, a single number who gages the quality of the solution, the bigger the better)
- Terminate population (criteria -> goal achieved, number of generations reached max,performance reached)
- Selection (survival of the fittest, we choose tipically the ones with the best fitness)
- Variation (crossover, mutation) -> new population (crossover). And then we use mutation. We select a random gene and we change it.

##What it is need to be done:
- 20 points/network while using predefined functions
- 50 points/network while using the genetic algorithm developed by the student
- there are 4 given networks
- there are 6 I can get
- so 20*4+ 20*6= 200 points
- 50*4+50*6= 500 points
- 2 fitness functions = 100 points
- total 800 points


Order of solving:
- get the data
- choosing and parameterizing the method of solving the problem
- displaying the identified solution
- specifying the performance of the chosen solving method


## Given data:
- the network's graph
- the algorithm's parameters

## Output data:
- the number of identified communities in the graph
- the membership to a certain community for each node of the graph/network


## Optimization problems if D is continous:
- Sphere function (unimodal): f(x)=x1^2+x2^2+...+xn^2 = sum(x^2)
- Griewank function( uni-modal,non-convez function): f(x)=1+1/4000*sum(x^2)-prod(cos(x/sqrt(i)))
- Rastrigin function (multi-modal): f(x)=10n+sum(x^2-10cos(2*pi*x))

## Optimization problems if D is discrete:
- traveling salesman problem (TSP)
- knapsack problem

## Solving the problem:
- analize the problem and the data given then choose the method of solving
- define the fitness function
- define the genetic operators :
  - selection
  - crossover
  - mutation
- define the evolutionary scheme
  - generational algorithm
  - steady-state algorithm
- choose the optimal solution