'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
# from subsystems.DrivetrainSubsystem import drivetrain 
# from subsystems.TurretSubsystem import turret 

from commands.CommandScheduler import CommandScheduler
from commands.DriveForwardRotate import DriveForwardRotate
from commands.TurretPID import TurretPID
from commands.RotateTurret import RotateTurret
import time
from commands.DrivetrainPID import DrivetrainPID

scheduler = CommandScheduler()

drive_command_1 = DriveForwardRotate(1, 1)
drive_command_2 = DriveForwardRotate(0, 0)

drivePID = DrivetrainPID(0)
print("Instantiating DrivePID 1 at", str(id(drivePID)), "at time", drivePID.get_init_time())

drivePID1 = DrivetrainPID(0)
print("Instantiating DrivePID 2 at", str(id(drivePID1)), "at time", drivePID.get_init_time())

drivePID2 = DrivetrainPID(0)
print("Instantiating DrivePID 3 at", str(id(drivePID2)), "at time", drivePID.get_init_time())

drivePID3 = DrivetrainPID(0)
print("Instantiating DrivePID 4 at", str(id(drivePID3)), "at time", drivePID.get_init_time())

scheduler.add_command(drive_command_1)
scheduler.add_command(drive_command_2)
scheduler.add_command(drivePID)
scheduler.add_command(drivePID1)
scheduler.add_command(drivePID2)
scheduler.add_command(drivePID3)

# print(scheduler.scheduled_commands)

turretPID = TurretPID(0)
print("Instantiating TurretPID 1 at", str(id(turretPID)), "at time", turretPID.get_init_time())
print(id(turretPID.get_required_subsystem()))
time.sleep(1)

turretPID1 = TurretPID(1)
print("Instantiating TurretPID 2 at", str(id(turretPID1)), "at time", turretPID1.get_init_time())
print(id(turretPID1.get_required_subsystem()))

turretPID2 = TurretPID(2)
print("Instantiating TurretPID 3 at", str(id(turretPID2)), "at time", turretPID2.get_init_time())
print(id(turretPID2.get_required_subsystem()))

turretPID3 = TurretPID(3)
print("Instantiating TurretPID 4 at", str(id(turretPID3)), "at time", turretPID3.get_init_time())
print(id(turretPID3.get_required_subsystem()))

rotateTurret = RotateTurret(0)

scheduler.add_command(turretPID)
scheduler.add_command(turretPID1)
scheduler.add_command(turretPID2)
scheduler.add_command(turretPID3)
scheduler.add_command(rotateTurret)

print("\n\ninput commands")
for key in scheduler.input_commands:    
    print(key)

scheduler.schedule_commands()

print("\n\nscheduled commands")
for key in scheduler.scheduled_commands.keys():
    print(key, scheduler.scheduled_commands[key])


def execute_loop():
    #stuff here
    
    scheduler.schedule_commands()
    scheduler.execute_commands()


# drivetrain.drive_fwd_rot(1, 1)
# turret.set_power(1)
        
        

