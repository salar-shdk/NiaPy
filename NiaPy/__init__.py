# encoding=utf8

"""Python micro framework for building nature-inspired algorithms."""

from __future__ import print_function


from NiaPy import util, algorithms, benchmarks, task
from NiaPy.runner import Runner

__all__ = ["algorithms", "benchmarks", "util", "task", "Runner"]
__project__ = "NiaPy"
"""str: Project name."""
__version__ = "2.0.0rc11"
"""str: Version."""

VERSION = "{0} v{1}".format(__project__, __version__)
"""str: Full project name and version."""
