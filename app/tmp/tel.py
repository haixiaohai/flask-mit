import telnetlib
import time


try:
    with telnetlib.Telnet(host='192.168.111.105',timeout=180) as tn:
        #print(tn.read_until(b'>').decode('utf-8'),end='')            
        tn.write(b'enable\r')
        time.sleep(0.1)
        tn.write(b'a\r')
        tn.write(b'\r')
        time.sleep(0.1)
        if tn.read_until(b'#'):
            tn.write(b'show version\r\n')
            time.sleep(0.5)
            version_info = tn.read_very_eager().decode('utf-8')
            #hostname = get_hostname(version_info)
            #version = get_version(version_info)
            commmands = ['more off','show version detail','show environment','show logging']
            for command in commmands:
                tn.write(b'\r\n')
                if tn.read_until(b'#'):
                    tn.write(command.encode('utf-8') + b'\r')
                time.sleep(1)
            time.sleep(2)
            print(tn.read_all().decode('gbk'))
            tn.close()
except ConnectionRefusedError:
    print('连接失败，请检测网络或者用户名密码是否正确！')


class Telnet():
    ''''''

def __init__(self,host,enbale_password,*args):
    self.host = host
    self.enbale_password = enbale_password
    self.port = 23


def get_hostname(self):
    pass

def get_version(self):
    pass