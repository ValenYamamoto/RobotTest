'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
# from subsystems.DrivetrainSubsystem import drivetrain 
# from subsystems.TurretSubsystem import turret 

from commands.CommandScheduler import CommandScheduler
from commands.DriveForwardRotate import DriveForwardRotate
from commands.TurretPID import TurretPID

scheduler = CommandScheduler()

drive_command_1 = DriveForwardRotate(1, 1)
drive_command_2 = DriveForwardRotate(0, 0)

scheduler.add_command(drive_command_1)
scheduler.add_command(drive_command_2)

for key in scheduler.input_commands:
    
    print(key)

scheduler.schedule_commands()
for key in scheduler.scheduled_commands.keys():
    print(key, scheduler.scheduled_commands[key])
# print(scheduler.scheduled_commands)

turretPID = TurretPID(0)
turretPID1 = TurretPID(1)
turretPID2 = TurretPID(2)
turretPID3 = TurretPID(3)

scheduler.add_command(turretPID)
scheduler.add_command(turretPID1)
scheduler.add_command(turretPID2)
scheduler.add_command(turretPID3)

scheduler.schedule_commands()

print(type(turretPID) is TurretPID)


# drivetrain.drive_fwd_rot(1, 1)
# turret.set_power(1)

