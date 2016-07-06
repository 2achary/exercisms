#
# Skeleton file for the Python "Hello World" exercise.
#
from __future__ import unicode_literals


def hello(name=''):
    greeting = "Hello, {}!"
    if name:
        return greeting.format(name)
    return greeting.format('World')