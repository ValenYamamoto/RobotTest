'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
class Subsystem:
    def __init__(self):
        self.name = id(self)
        
    def get_name(self):
        return self.name
    
    def get_types(self, l):
        type_list = []
        for x in l:
            type_list.append(type(x))
        return type_list
    
    def get_names(self, l):
        type_list = []
        for x in l:
            type_list.append(x.get_name())
        return type_list
    
    def command_conflict(self, commands):
        first_command = commands[0]
        for command in commands:
            if(command.get_init_time() < first_command.get_init_time()):
                first_command = command
        return first_command
    
    def __str__(self):
        return self.toString()
    
    def toString(self):
        return self.name
    
if __name__ == "__main__":
    subsystem = Subsystem()
    print(subsystem.get_name())
    