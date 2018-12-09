import pexpect
from pexpect.popen_spawn import PopenSpawn


def telnet(host):
    tn = pexpect.popen_spawn.PopenSpawn('telnet %s' %host)
    tn.expect('>')
    tn.sendline('enable\r\n')
    tn.expect('password:')
    tn.sendline('a\r')
    tn.expect('#')
    tn.sendline('show version\r\n')

def ssh():
    pass

telnet('192.168.111.105')