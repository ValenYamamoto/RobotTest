# RobotTest
Trying to create a template for a hypothetical robot, written in python, based off WPI's FRC robot code structure

## Subsystems
Each subsystem on the robot is also sequestered in its own class in the code. All subsystem inherit from the base class subsystem, which sets default methods for construction and dealing with multiple command calls to its resources in the current loop. Child classes will then build upon the methods to specialize towards their functionalities.

``` python 
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
```

## Commands
Commands are used to execute instructions using a subsystem's resources. All commands are child classes of the base class Command, which lays out the general format and variables.

```python
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
```

## Scheduler and Scheduling Commands
When a command is called in the main loop, it must be scheduled with the CommandScheduler class. At the end of each loop, the scheduler will run through all the proposed commands and get rid of multiples or conflicts based on each class' command_conflict method.

```python
class CommandScheduler:
    
    def __init__(self):
        self.scheduled_commands = {}
        self.input_commands = []
        self.running_commands = {}
        self.sorted_commands = {}
        
    def add_command(self, command):
        self.input_commands.append(command)
    
    def schedule_commands(self):
        print(self.input_commands)
        for command in self.input_commands:
            if(id(command.get_required_subsystem()) in self.get_ids(self.sorted_commands.keys())):
                self.sorted_commands[command.get_required_subsystem()].append(command)
            else:
                self.sorted_commands[command.get_required_subsystem()] = [command]
            
        print("\n\n", self.sorted_commands, sep = "")
        
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
                
    def get_ids(self, l):
        type_list = []
        for x in l:
            type_list.append(id(x))
        return type_list
```
