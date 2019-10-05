'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from datetime import datetime
from subsystems import Subsystem
class Command:
        
    def __init__(self):    
        self.name = id(self)
        self.initialize()

    def initialize(self):
        self.isInitialized = True
        self.isSetUp = False
        self.isExecuting = False
        self.isFinished = False
        self.requiredSubsystem = Subsystem()
        self.initTime = datetime.timestamp()
        
    def requires(self, subsystem):
        self.requiredSubsystem = subsystem
        
    def getRequiredSubsystem(self):
        return self.requiredSubsystem

    def setUp(self):
        if(self.isInitialized):
            #Do Stuff
            break
        self.isSetUp = True
    
    def Execute(self):
        if(self.isSetUp):
            self.isExecuting = True
            if(self.isFinished()):
                break
        self.isExecuting = False
        
    def isFinished(self):
        return True
    
    def end(self):
        return
    
    def getInitTime(self):
        return self.initTime