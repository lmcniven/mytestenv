#!/usr/bin/python2.7

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def main():
    ip_addr = '10.0.45.210'
    username = 'mcnivl10'
    password = 't0psecret'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until('sername:', TELNET_TIMEOUT)
    output = remote_conn.write(username + '\n')
    output = remote_conn.read_until('ssword:', TELNET_TIMEOUT)
    output = remote_conn.write(password + '\n')
    output = remote_conn.write('\n')


    time.sleep(1)
    output = remote_conn.read_very_eager()


    output = remote_conn.write('show configuration' + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()    


if __name__== "__main__":
     main()

