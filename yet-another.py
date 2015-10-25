#!/usr/bin/python2.7

a=10

def test ():
    global a
    print a


test()

a=20

print a

