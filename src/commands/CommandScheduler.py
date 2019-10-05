'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
class CommandScheduler:
    
    def __init__(self):
        self.scheduledCommands = {}
        self.inputCommands = []
        self.runningCommands = {}
        self.sortedCommands = {}
        
    def addCommand(self, command):
        self.inputCommands.append(command)
    
    def scheduleCommand(self):
        for command in self.inputCommands:
            self.sortedCommands[command.getRequiredSubsystem()].append(command)
            
        for subsystem in self.sortedCommands.keys():
            self.scheduluedCommands[subsystem] = subsystem.commandConflict(self.sortedCommands[subsystem])
        
    def executeCommands(self):
        for subsystem in self.sortedCommands.keys():
            self.runningCommands[subsystem] = subsystem.commandConflict(self.sortedCommands[subsystem])
        
        for command in self.runningCommands.values():
            if(not command.isSetUp):
                command.setUp()
            elif(command.isFinished()):
                command.end()
            else:
                command.execute()
                