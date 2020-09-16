# Quickstart

## Installation

We are trying very hard to provide you with the most convinient ways for you to install the NiaPy. Currently you can install it using: **pip**, **conda**, **Arch AUR package**, **Fedora package** or **Install from source**.

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

=== "Arch AUR package"

    <div class="termy">
    ```console
    $ yay -Syu python-niapy

    ---> 100%
    ```
    </div>

=== "Fedora package"

    <div class="termy">
    ```console
    $ yum install python3-niapy

    ---> 100%
    ```
    </div>

=== "Install from source"

    <div class="termy">
    ```console
    $ git clone https://github.com/NiaOrg/NiaPy.git

    ---> 100%

    $ cd Niapy
    $ python setup.py install

    ---> 100%
    ```
    </div>

## Simple example

In this example, let’s say, we want to try out Gray Wolf Optimizer algorithm against Sphere benchmark function. Firstly, we have to create new file, with name, for example ```basic_example.py```. Then we have to import chosen algorithm from NiaPy, so we can use it. Afterwards we initialize GreyWolfOptimizer class instance and run the algorithm. Given bellow is complete source code of this simple example together with the output of the code.

{% include 'notebooks/quickstart.md.tmp' %}

For more tutorials using various NiaPy features please go through [user guide](/user_guide/introduction/).