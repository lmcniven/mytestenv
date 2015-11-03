import json

my_list = range (8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]
{}
my_list[-1] ['ip_addr'] = '10.10.10.239'
my_list[-1] ['attribs'] = range(5)


print json.dumps(my_list)


