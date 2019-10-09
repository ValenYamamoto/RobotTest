'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
class Motor:
    
    def __init__(self, port):
        self.port = port
        self.power = 0
        
    def set(self, power):
        self.power = power
        
    def get_power(self):
        return self.power
        
if __name__ == "__main__":
    motor = Motor(1)
    motor.set(0.9)
    print("Motor Power: %f" % (motor.get_power()))