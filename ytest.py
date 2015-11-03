#!/usr/bin/python2.7


import yaml

my_list = range (8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]
{}
my_list[-1] ['ip_addr'] = '10.10.10.239'
my_list[-1] ['attribs'] = range(7)


print yaml.dump(my_list)
