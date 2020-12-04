# encoding=utf8

"""Python micro framework for building nature-inspired algorithms."""

from __future__ import print_function


from NiaPy import util, algorithms, benchmarks, task
from NiaPy.runner import Runner

__all__ = ["algorithms", "benchmarks", "util", "task", "Runner"]
__project__ = "NiaPy"
<<<<<<< HEAD
__version__ = "2.0.0rc12"
=======
"""str: Project name."""
__version__ = "2.0.0rc11"
"""str: Version."""
>>>>>>> 362de3a83ddc3829b1945af882d7c3aa0f632cb7

VERSION = "{0} v{1}".format(__project__, __version__)
"""str: Full project name and version."""
