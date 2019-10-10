'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from externals.Motor import Motor
from subsystems.Subsystem import Subsystem
import commands.TurretPID

class TurretSubsystem(Subsystem):
    class TurretPIDConstants:
        k_p = 0
        k_i = 0
        k_d = 0
        
    def __init__(self):
        self.name = "TurretSubsystem"
        self.turret_motor = Motor(3)
        
    def set_power(self, power):
        self.turret_motor.set(power)
        
    def command_conflict(self, commands):
        print(commands)
        first_command = commands[0]
        names = self.get_names(commands)
        
        for name in names:
            if("TurretPIDCommand" in name): 
                for command in commands:
                    if("TurretPIDCommand" not in command.get_name()):
                        commands.pop(command)
                
            break
        
        print(commands)
        
        
#         command_dict = {}
#         
#         for index in range(len(commands)):
#             command_dict[commands[index]] = name[index]
#             
#         print("command_dict", command_dict, len(command_dict))
#             
#         if(type(commands.TurretPID.TurretPID) in command_dict.values()):
#             commands = [command_dict.keys()[x] for x in range(len(command_dict.values())) 
#                            if command_dict.values()[x] is type(commands.TurretPID.TurretPID)]
#             
#         print("sorted commands", commands)
        
        for command in commands:
            
            if(command.get_init_time() < first_command.get_init_time()):
                first_command = command
        return first_command
    
    def toString(self):
        return self.name
    
turret = TurretSubsystem()

if __name__ == "__main__":
    turret.set_power(1)
    print("Turret Motor Power: %f" % (turret.turret_motor.get_power()))