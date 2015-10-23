#/usr/bin/python2.7

a=10

def test ():
    global a
    a=a+10
    print a

test()

print a
