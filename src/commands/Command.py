'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from subsystems.Subsystem import Subsystem
import time

class Command:
        
    def __init__(self):    
        self.name = id(self)
        self.required_subsystem = Subsystem()
        self.is_initialized = True
        self.is_set_up = False
        self.is_executing = False
        self.finished = False
        self.init_time = time.time()
        
        
    def requires(self, subsystem):
        self.required_subsystem = subsystem
        
    def get_required_subsystem(self):
        return self.required_subsystem

    def set_up(self):
        if(self.is_initialized):
            #Do Stuff
            print("Command Set Up")
        self.is_set_up = True
    
    def execute(self):
        if(self.is_set_up):
            self.is_executing = True
            print("Command Execute")
            if(self.is_finished()):
                print("Command Finished")
                self.is_executing = False
            self.finished = True
        
    def is_finished(self):
        print("is_finished = " + str(self.finished))
        return True
    
    def end(self):
        print("End")
        return
    
    def get_init_time(self):
        return self.init_time
    
    def toString(self):
        return str(self.name)
    
    def __str__(self):
        return self.toString()
    
    def get_name(self):
        return self.name
    
if __name__ == "__main__":
    command = Command()
    command.set_up()
    command.execute()
    command.is_finished()
    command.execute()
    command.end()
    print("Init time: %f" % (command.get_init_time()))
    