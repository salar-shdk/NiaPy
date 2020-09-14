# encoding=utf8

"""Algorithm Statistics module."""

import numpy as np

__all__ = ['BasicStatistics']


class BasicStatistics:
    r"""
    Class implementing the basic statistics.

    !!! example

        ```python
            import numpy as np
            from NiaPy.task import StoppingTask, OptimizationType
            from NiaPy.algorithms import BasicStatistics
            from NiaPy.algorithms.basic import DifferentialEvolution
            from NiaPy.benchmarks import Sphere

            NUM_RUNS = 10  # define number of runs
            stats = np.zeros(NUM_RUNS)

            for i in range(NUM_RUNS):
                task = StoppingTask(D=10, nFES=10000, optType=OptimizationType.MINIMIZATION, benchmark=Sphere())
                print ("Working on run: " + str(i+1))
                algo = DifferentialEvolution(NP=40, CR=0.9, F=0.5)
                best = algo.run(task)
                stats[i] = best[1]  # save best

            stat = BasicStatistics(stats)
            print(stat.generate_standard_report())  # generate report
        ```
    """
    Name = ['BasicStatistics']
    """List[str]: List of names for BasicStatistics class."""

    def __init__(self, array):
        r"""
        Initialize BasicStatistics.

        Args:
            array (Union[array, np.ndarray]): Array of results.
        """
        self.array = array if isinstance(array, np.ndarray) else np.asarray(array)

    def min_value(self):
        r"""
        Get minimum value from an array.

        Returns:
            float: Min value.
        """
        return self.array.min()

    def max_value(self):
        r"""
        Get maximum value from an array.

        Returns:
            float: Max value.
        """
        return self.array.max()

    def mean(self):
        r"""
        Get mean value from an array.

        Returns:
            float: Mean value.
        """
        return self.array.mean()

    def median(self):
        r"""
        Get median value from an array.

        Returns:
            float: Median value.
        """
        return np.median(self.array)

    def standard_deviation(self):
        r"""
        Get standard deviation from an array.

        Returns:
            float: Standard deviation value.
        """
        return self.array.std(ddof=1)

    def generate_standard_report(self):
        r"""
        Generate basic statistics report.

        Returns:
            str: Basic statistics report string.
        """
        return "Min: {0}, Max: {1}, Mean: {2}, Median: {3}, Std. {4}".format(
            self.min_value(),
            self.max_value(),
            self.mean(),
            self.median(),
            self.standard_deviation())
