# Introduction

! TODO: write introduction !

## Features

Over the years, with the help of the community, we implemented more than 30 algorithms and also more than 30 benchmark functions.

### Algorithms

NiaPy features more than 30 algorithms. They are categorized as basic, modified, and others.

#### Basic algorithms

- Artificial bee colony algorithm
- Bat algorithm
- Camel algorithm
- Cuckoo search
- Differential evolution algorithm
- Evolution Strategy
- Firefly algorithm
- Fireworks algorithm
- Flower pollination algorithm
- Forest optimization algorithm
- Genetic algorithm
- Glowworm Swarm Optimization
- Grey wolf optimizer
- Harmony Search Algorithm
- Krill Herd Algorithm
- Monarch butterfly optimization
- Monkey King Evolution
- Moth flame optimizer
- Particle swarm optimization
- Sine Cosine Algorithm

Documentation for the basic algorithms can be found here: [NiaPy.algorithms.basic](reference/algorithms/basic/).


#### Modified algorithms

- Hybrid bat algorithm
- Self-adaptive differential evolution algorithm
- Dynamic population size self-adaptive differential evolution algorithm

Documentation for the modified algorithms can be found here: [NiaPy.algorithms.modified](reference/algorithms/modified/).


#### Other algorithms

- Anarchic society optimization
- Hill climb algorithm
- Multiple trajectory search
- Nelder mead method
- Simulated annealing algorithm

Documentation for the other algorithms can be found here: [NiaPy.algorithms.other](reference/algorithms/other/).


### Benchmark functions

NiaPy features more than 30 benchmark functions. Documentation for them can be found here: [NiaPy.benchmarks](reference/benchmarks).


### Other features:

- Using different termination conditions (nFES, nGEN, reference value)
- Basic statistics example (min, max, mean, median, std)
- Storing improvements during the evolutionary cycle
- Custom initialization of initial population

## Why use NiaPy?

NiaPy is micro-framework for using and building nature-inspired algorithms dedicated for researchers and practitioners. The major strenghtness of NiaPy is large collection of ready to use algorithms and benchmark functions, as well as the simplistic architecture design which allows users to add their own algorithms or extend the existing ones. The NiaPy micro-framework can also be easily used for solving real-world problems. The usabillity of NiaPy is shown in the numerous toolboxes build on top of it and large number of citations in many scientific papers. For the detailed list please look at the next section.

## Who uses NiaPy?

NiaPy is used in many research papers. The full list of papers using NiaPy is available [here](https://scholar.google.si/scholar?oi=bibs&hl=en&cites=15685269763828608718&as_sdt=5).

Additionally, here is the list of known projects which use NiaPy:

<div x-data="alpineInstance()"
     x-init="fetch('https://github-dependents.swarm.grega.xyz/NiaOrg/Niapy')
                      .then(response => response.json())
                      .then(data => dependents = data.entries)">
    <ul>
        <template x-for="dependent in dependents">
            <li>
                <a x-bind:href="'https://github.com/'+dependent.org+'/'+dependent.repo" x-text="dependent.repo"></a>
                <span x-text="'⭐ '+dependent.stars+'🍴'+dependent.forks"></span>
            </li>
        </template>
    </ul>
</div>

<script>
function alpineInstance() {
  return {
    dependents: [],
  }
}
</script>