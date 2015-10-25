#!/usr/bin/python2.7

import yaml


a=10


def test (num):

    global a
    a=a+num
    print a

test(10)
test(5)
print a + 10



