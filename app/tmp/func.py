import telnetlib
import os
import time
from app.models import Command


def telnet(ipaddress,device_type,enable_password,*args):
    """Telnet main program"""
    
    def do_telnet():
        '''telnet'''
        with telnetlib.Telnet(ipaddress,timeout=100) as tn:
            if tn.read_until(b'>'):
                tn.write(b'enable\r\n')
                tn.read_until(b'password:')
                tn.write(enable_password.encode('utf-8') + b'\r\n')
            elif tn.read_until(b'login:'):
                tn.write(args[0].encode('utf-8') + b'\r\n')
                tn.write(args[1].encode('utf-8') + b'\r\n')
                if tn.read_until(b'>'):
                    tn.write(b'enable\r\n')
                    tn.read_until(b'password:')
                    tn.write(enable_password.encode('utf-8') + b'\r\n')
                else :
                    raise ValueError 
            else :
                tn.write(args[1].encode('utf-8') + b'\r\n')
                tn.write(b'enable\r\n')
                tn.read_until(b'password:')
                tn.write(enable_password.encode('utf-8') + b'\r\n')
                if tn.read_until(b'password:'):
                    raise ValueError
            
            general_commands = Command.query.filter_by(apply_to_device='general',exec_mode='priv')
            for command in general_commands:
                tn.write(command.command.encode('utf-8') + b'\r\n')
                time.sleep(1)

            fsconfig_commands = Command.query.filter_by(apply_to_device='general',exec_mode='fsconfig')
            tn.write(b'filesystem\r\n')
            for command in fsconfig_commands:
                tn.write(command.command.encode('utf-8') + b'\r\n')
                time.sleep(0.1)
            tn.write(b'exit\r\n')

            time.sleep(1)
            result = tn.read_very_eager().decode('gb2312','ignore')
        return result

    #如果没有文件夹就创建文件夹
    if os.path.exists('Logs'):
        pass
    else:
        os.mkdir('Logs')

    #定义日志路径及日志文件名
    log_path=os.path.join(os.getcwd(),'Logs')
    log_file = '【巡检日志】' + device_type + '_' + time.strftime(r'%Y%m%d_%H%M%S') + '.log'
    logfile = os.path.join(log_path,log_file)

    with open(logfile,'w',encoding='utf-8') as save_file:
        result = do_telnet()
        save_file.write(result)


def ssh(ipaddress,device_type,username,password,enable_password,*args):
    if os.path.exists('Logs'):
        pass
    else :
        os.mkdir('Logs')

    