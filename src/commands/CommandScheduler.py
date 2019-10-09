'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
class CommandScheduler:
    
    def __init__(self):
        self.scheduled_commands = {}
        self.input_commands = []
        self.running_commands = {}
        self.sorted_commands = {}
        
    def add_command(self, command):
        self.input_commands.append(command)
    
    def schedule_commands(self):
        for command in self.input_commands:
            if(command.get_required_subsystem in self.sorted_commands.keys()):
                self.sorted_commands[command.get_required_subsystem()].append(command)
            else:
                self.sorted_commands[command.get_required_subsystem()] = [command]
            
        for subsystem in self.sorted_commands.keys():
            self.scheduled_commands[subsystem] = subsystem.command_conflict(self.sorted_commands[subsystem])
        
    def execute_commands(self):
        for subsystem in self.sorted_commands.keys():
            self.running_commands[subsystem] = subsystem.command_conflict(self.sorted_commands[subsystem])
        
        for command in self.running_commands.values():
            if(not command.is_set_up):
                command.set_up()
            elif(command.is_finished()):
                command.end()
            else:
                command.execute()
                
    
    