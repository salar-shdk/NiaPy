Getting Started
===============

It's time to write your first NiaPy example. Firstly, if you haven't already, install NiaPy package on your system
using following command:

.. code:: bash

    pip install NiaPy

or:

.. code:: bash

    conda install -c niaorg niapy

When package is successfully installed you are ready to write you first example.

Basic optimization example
--------------------------
In this example, let's say, we want to try out Gray Wolf Optimizer algorithm against Pintér benchmark function.
Firstly, we have to create new file, with name, for example *basic_example.py*. Then we have to import chosen
algorithm from NiaPy, so we can use it. Afterwards we initialize GreyWolfOptimizer class instance and run the algorithm.
Given bellow is complete source code of basic example.

.. code:: python

    from NiaPy.algorithms.basic import GreyWolfOptimizer
    from NiaPy.task import StoppingTask

    # we will run 10 repetitions of Grey Wolf Optimizer against Pinter benchmark function
    for i in range(10):
        task = StoppingTask(D=10, nFES=1000, benchmark='pinter')
        algorithm = GreyWolfOptimizer(NP=20)
        best = algorithm.run(task)
        print(best[-1])


Given example can be run with ``python basic_example.py`` command and should give you similar output as
following:

.. code:: bash

    0.27046073106003377
    50.89301186976975
    1.089147452727528
    1.18418058254198
    102.46876441081712
    0.11237241605812048
    1.8869331711450696
    0.04861881403346098
    2.5748611081742325
    135.6754069530421



