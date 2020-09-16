# encoding=utf8

"""Benchmarks Utility module."""

from NiaPy import benchmarks

class BenchmarkUtility:
    r"""Base class with string mappings to benchmarks.

    !!! example

        ```python
            from NiaPy.benchmarks import BenchmarkUtility

            benchmark = BenchmarkUtility().get_benchmark("rastrigin")
        ```
    """

    def __init__(self):
        r"""Initialize the benchmark utility."""

        self.benchmark_classes = {
            "ackley": benchmarks.Ackley,
            "alpine1": benchmarks.Alpine1,
            "alpine2": benchmarks.Alpine2,
            "bentcigar": benchmarks.BentCigar,
            "chungReynolds": benchmarks.ChungReynolds,
            "cosinemixture": benchmarks.CosineMixture,
            "csendes": benchmarks.Csendes,
            "discus": benchmarks.Discus,
            "dixonprice": benchmarks.DixonPrice,
            "conditionedellptic": benchmarks.Elliptic,
            "elliptic": benchmarks.Elliptic,
            "expandedgriewankplusrosenbrock": benchmarks.ExpandedGriewankPlusRosenbrock,
            "expandedschaffer": benchmarks.ExpandedSchaffer,
            "griewank": benchmarks.Griewank,
            "happyCat": benchmarks.HappyCat,
            "hgbat": benchmarks.HGBat,
            "infinity": benchmarks.Infinity,
            "katsuura": benchmarks.Katsuura,
            "levy": benchmarks.Levy,
            "michalewicz": benchmarks.Michalewichz,
            "modifiedscwefel": benchmarks.ModifiedSchwefel,
            "perm": benchmarks.Perm,
            "pinter": benchmarks.Pinter,
            "powell": benchmarks.Powell,
            "qing": benchmarks.Qing,
            "quintic": benchmarks.Quintic,
            "rastrigin": benchmarks.Rastrigin,
            "ridge": benchmarks.Ridge,
            "rosenbrock": benchmarks.Rosenbrock,
            "salomon": benchmarks.Salomon,
            "schaffer2": benchmarks.SchafferN2,
            "schaffer4": benchmarks.SchafferN4,
            "schumerSteiglitz": benchmarks.SchumerSteiglitz,
            "schwefel": benchmarks.Schwefel,
            "schwefel221": benchmarks.Schwefel221,
            "schwefel222": benchmarks.Schwefel222,
            "sphere": benchmarks.Sphere,
            "sphere2": benchmarks.Sphere2,
            "sphere3": benchmarks.Sphere3,
            "step": benchmarks.Step,
            "step2": benchmarks.Step2,
            "step3": benchmarks.Step3,
            "stepint": benchmarks.Stepint,
            "styblinskiTang": benchmarks.StyblinskiTang,
            "sumSquares": benchmarks.SumSquares,
            "trid": benchmarks.Trid,
            "weierstrass": benchmarks.Weierstrass,
            "whitley": benchmarks.Whitley,
            "zakharov": benchmarks.Zakharov
        }

    def get_benchmark(self, benchmark):
        r"""Get the optimization problem.

        Arguments:
            benchmark (Union[str, Benchmark]): String or class that represents the optimization problem.

        Returns:
            Benchmark: Optimization function with limits.

        """

        if issubclass(type(benchmark), benchmarks.Benchmark) or isinstance(benchmark, benchmarks.Benchmark):
            return benchmark
        elif benchmark in self.benchmark_classes.keys():
            return self.benchmark_classes[benchmark]()
        else:
            raise TypeError("Passed benchmark is not defined!")
