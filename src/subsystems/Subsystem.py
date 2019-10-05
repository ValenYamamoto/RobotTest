'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from commands import Command
class Subsystem:
    def __init__(self):
        self.name = id(self)
        
    def getName(self):
        return self.name
    
    def commandConflict(self, commands):
        firstCommand = commands[0]
        for command in commands:
            if(command.getInitTime() < firstCommand.getInitTime()):
                firstCommand = command
        return firstCommand
    