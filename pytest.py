#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TESTS
import os
import subprocess

class Device():
    def __init__(self, name='', stype=''):
        self.name = name
        self.stype = stype
    
    def __str__(self):
        print(f'{self.name}, {self.stype}')

class Commands():
    def __init__(self, cmd='', note=''):
        self.cmd = cmd
        self.note = note

class Server(Device):
    def __init__(self, name='', stype='', model='', cmd=''):
        super().__init__(name=name, stype=stype)
        super().__init__(cmd=cmd, note=note)
        self.model = model
        self.cmd = cmd
    
    def __str__(self):
        print(f'{self.name}, {self.stype}, {self.model}')
    
    def runcmd(self):
        if self.cmd == 'ping':
            cmd = 'ping ' + self.srv_name 
            return subprocess.getoutput(self, cmd)
    


# MAIN

srv = Server('dell', 'server', '740xd', 'ping')
print(srv.model)
srv.runcmd();
