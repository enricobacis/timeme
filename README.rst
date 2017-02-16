timeme
======

*python decorator that prints the running time of a function*

Description
-----------

This decorator prints the running time that a function needed to complete.

.. code:: python

    from timeme import timeme
    from time import sleep

    @timeme
    def function(a, b):
        sleep(2)

    function(1, 2)
    # 'function' ((1, 2), {}) 2.00 sec


Installation
------------

The package has been uploaded to `PyPI`_, so you can install it with pip:

    pip install timeme


.. _PyPI: https://pypi.python.org/pypi/timeme
