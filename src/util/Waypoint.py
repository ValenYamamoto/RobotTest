'''
Created on Nov 21, 2019

@author: Valen Yamamoto
'''
from cmath import sqrt
class Waypoint:
    
    def __init__(self, x, y, curv, t_vel, dist):
        self._x = x
        self._y = y
        self._curv = curv
        self._t_vel = t_vel
        self._dist = dist
        
    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x
        
    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y
        
    def get_curv(self):
        return self._curv
    
    def set_curv(self, curv):
        self._curv = curv
        
    def get_vel(self):
        return self._t_vel
    
    def set_vel(self, vel):
        self._t_vel = vel
        
    def get_dist(self):
        return self._dist
    
    def set_dist(self, dist):
        self._dist = dist
        
    def get_distance(self, waypoint):
        return sqrt((self.x - waypoint.x) ** 2 + (self.y - waypoint.y) ** 2)
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    curv = property(get_curv, set_curv)
    vel = property(get_vel, set_vel)
    dist = property(get_dist, set_dist)
    