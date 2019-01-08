# -*- coding:utf-8 -*-

#import pexpect
import re
import telnetlib
import time
import traceback

import paramiko


class MIT(object):
    ''''''

    def __init__(self):
        pass


class TConnection(MIT):
    ''''''

    def __init__(self, host, username, password, enable_password):
        # super().__init__()
        self.host = host
        self.username = username
        self.password = password
        self.enable_password = enable_password

        self._connected = False
        self._connection = None

        self.hostname = self._get_hostname()

        if self.username == '':
            self.username = None
        if self.password == '':
            self.password = None

    def connect(self):
        '''connect to device,telnet and telnetlib'''
        self._connection = telnetlib.Telnet(self.host)

        prompt = ['ogin:', 'assword:', '>']
        idx, match, btext = self.expect(prompt)

        if match.group().decode('ascii') == 'ogin:':
            self.write(self.username)
            self.write(self.password)
            idx, match, btext = self.expect(['invalid', '>'])
            if match.group().decode('ascii') == 'invalid':
                print('invalid username or password')
        elif match.group().decode('ascii') == 'assword:':
            self.write(self.password)
        elif match.group().decode('ascii') == '>':
            pass
        else:
            print('invild prompt:' + btext.decode('ascii'))

        self._connected = True

    def disconnect(self):
        self._connection = None
        self._connected = False

    def enable(self):
        if self._connected:
            self.write('enable')
            self.write(self.enable_password)
            idx, match, btext = self.expect(['#', 'assword:'])
            if match.group().decode('ascii') == 'assword:':
                print('invalid enable password')
                # raise
            else:
                pass

    def write(self, command, timeout=0.1):
        '''通过telnet方式向device发送数据，不返回结果'''
        if self._connection is None:
            self.connect()
            #
        self._connection.write(command.encode('ascii') + b'\n')
        time.sleep(timeout)

    def read_until(self, command):
        expect_re = [command + '.*' + self.hostname +
                     '#$', command + '.*' + self.hostname + '>$']

        idx, match, ret_text = self.expect(expect_re, 2)
        return ret_text

    def _get_hostname(self):
        self.write('\r')
        idx, match, text = self.expect(['#$', '>$'])

        if match is not None:
            self.hostname = text.replace('>', '').replace('#', '').strip()
            return self.hostname
        else:
            # raise
            print('unable to get device hostname')

    def get_version(self):
        pass

    def expect(self, search_list, timeout=2):
        idx, match, btext = self._connection.expect(
            [pattern.encode('ascii') for pattern in search_list], timeout)
        return idx, match, btext.decode('ascii', 'ignore')

    def exec(self, command):
        '''执行命令，返回结果，telnet'''
        self.write(command)
        text = self.read_until(command)
        return text


class SConnection(MIT):
    ''''''

    def __init__(self, host, username, password, enable_password):
        self.host = host
        self.username = username
        self.password = password
        self.enable_password = enable_password
        self.port = 22

        self._connected = False
        self._connection = None

        self.hostname = None

    def _connect(self,port=22):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)

        self._connection = transport.open_session()
        self._connection.get_pty()   #打开远程terminal
        self._connection.invoke_shell()   #。。。。
        self.hostname = self._get_hostname()

        self._connected = True

    def disconnect(self):
        self._connection = None
        self._connected = False

    def _get_hostname(self):
        result = self.exec('')
        return result.replace('>', '').replace('#', '').strip()

    def enable(self, level=-1):
        if level <= 0:
            self.write('enable')
            self.write(self.enable_password)
        else:
            self.write('enable ' + str(level))
            self.write(self.enable_password)

    def write(self, command):
        self._connection.sendall(command + '\n')
        time.sleep(0.1)

    def exec(self, *commands):
        for command in commands:
            self._connection.sendall(command + '\n')
            time.sleep(1)
        ret = self._connection.recv(1024).decode('utf-8')
        return ret

    def read_until(self, prompt):
        pass


class Inspection(MIT):
    ''''''

    def __init__(self):
        pass

    def readstring(self, string):
        pass

    def waitstring(self, string):
        pass
