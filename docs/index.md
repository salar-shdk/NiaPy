# Welcome to NiaPy documentation

<p align="center"><img src="../images/NiaPyLogo.png" alt="NiaPy" title="NiaPy"/></p>

---

[![DOI](http://joss.theoj.org/papers/10.21105/joss.00613/status.svg)](https://doi.org/10.21105/joss.00613)

Python micro framework for building nature-inspired algorithms.

Nature-inspired algorithms are a very popular tool for solving optimization problems. Numerous variants of nature-inspired algorithms have been developed ([paper 1](https://arxiv.org/abs/1307.4186), [paper 2](https://www.mdpi.com/2076-3417/8/9/1521)) since the beginning of their era. To prove their versatility, those were tested in various domains on various applications, especially when they are hybridized, modified or adapted. However, implementation of nature-inspired algorithms is sometimes a difficult, complex and tedious task. In order to break this wall, NiaPy is intended for simple and quick use, without spending time for implementing algorithms from scratch.

* **Free software:** MIT license
* **Documentation:** https://niapy.readthedocs.io/en/stable/
* **Python versions:** 3.6.x, 3.7.x or 3.8.x (backward compatibility with 2.7.x)
* **Dependencies:** [click](developer_guide/contributing.md#development-dependencies)


## Installation

=== "pip"

    <div class="termy">
    ```console
    $ pip install NiaPy

    ---> 100%
    ```
    </div>

=== "conda"

    <div class="termy">
    ```console
    $ conda install -c niaorg niapy

    ---> 100%
    ```
    </div>

=== "Arch Linux"

    <div class="termy">
    ```console
    $ yay -Syu python-niapy

    ---> 100%
    ```
    </div>

=== "Fedora Linux"

    <div class="termy">
    ```console
    $ yum install python3-niapy

    ---> 100%
    ```
    </div>

=== "From Source"

    <div class="termy">
    ```console
    $ git clone https://github.com/NiaOrg/NiaPy.git

    ---> 100%

    $ cd Niapy
    $ python setup.py install

    ---> 100%
    ```
    </div>


## Mission

Our mission is to build a collection of nature-inspired algorithms and
create a simple interface for managing the optimization process along
with statistical evaluation. NiaPy offers:

-   numerous benchmark functions implementations,
-   use of various nature-inspired algorithms without struggle and
    effort with a simple interface, and
-   easy comparison between nature-inspired algorithms.

## Licence

This package is distributed under the [MIT License].

## Disclaimer

This framework is provided as-is, and there are no guarantees that it
fits your purposes or that it is bug-free. Use it at your own risk!

[nature-inspired algorithms were developed]: https://arxiv.org/abs/1307.4186
[MIT License]: http://www.opensource.org/licenses/MIT