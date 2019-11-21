'''
Created on Oct 14, 2019

@author: Valen Yamamoto
'''
import math
class Point:
    def __init__(self, x = 0, y = 0, heading = 0):
        self._x = x
        self._y = y
        self.heading = heading
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x
        
    def set_y(self, y):
        self._y = y

    def get_heading(self):
        return self.heading
    
    def set_heading(self, heading):
        self.heading = heading
        
    def distance(self, point2):
        return math.sqrt((self._x - point2.get_x())**2 + (self._y - point2.get_y())**2)
    
    def heading_diff(self, point2):
        return point2.get_heading() - self.heading

    x = property()
    x = x.getter(get_x)
    x = x.setter(set_x)
    
    y = property()
    y = y.getter(get_y)
    y = y.setter(set_y)
    
    def __repr__(self):
        return "(%.2f, %.2f)" % (self.get_x(), self.get_y())
    