'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
class Motor:
    
    def __init__(self, port):
        self.port = port
        self.power = 0
        
    def set(self, power):
        self.power = power
        
        