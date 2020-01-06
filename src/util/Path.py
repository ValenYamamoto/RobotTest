'''
Created on Nov 21, 2019

@author: Valen Yamamoto
'''
from algorithms.Spline import Spline
from util.Waypoint import Waypoint
from util.Point import Point
from math import sqrt, pow, sin, cos
import matplotlib.pyplot as plot
import numpy as np
import csv as csv
from datetime import datetime

class Path:
    
    def __init__(self, points, trackwidth=0, max_vel=5, max_accel=2, k=1, step=0.1):
        x, y = Spline(points, step=step).spline
        
        self.waypoints = []
        x, y = self.smoothPath(x, y, 0.05, 0.95, 0.001)
        for i in range(len(x)):
            self.waypoints.append(Waypoint(x[i], y[i], 0, 0, 0))
        
        self.trackwidth = trackwidth
        self.max_vel = max_vel
        self.max_accel = max_accel
        self.k = k
        self.calc_curv()
        self.calc_dist()
        self.calc_vel()
        
        
    def calc_curv(self):
        self.waypoints[0].curv = 0
        self.waypoints[-1].curv = 0
        for i in range(1, len(self.waypoints) - 1):
            p = self.waypoints[i]
            q = self.waypoints[i - 1]
            r = self.waypoints[i + 1]
            
            area = (p.x * (q.y - r.y) + q.x * (r.y - p.y) + r.x * (p.y - q.y)) / 2
            area = area
            pq = p.get_distance(q)
            qr = q.get_distance(r)
            rp = r.get_distance(p)
             
            curvature = 4 * area / (rp * qr * pq)
             
            self.waypoints[i].curv = curvature
            
            
    def calc_dist(self):
        self.waypoints[0].dist = 0
        
        for i in range(1, len(self.waypoints)):
            self.waypoints[i].dist = self.waypoints[i].get_distance(self.waypoints[i - 1]) + self.waypoints[i - 1].dist
            
            
    def calc_vel(self):
        self.waypoints[0].vel = self.max_vel
        
        for i in range(1, len(self.waypoints)):
            try:
                self.waypoints[i].vel = min([abs(self.k/self.waypoints[i].curv), abs(self.max_vel)])
            except ZeroDivisionError:
                self.waypoints[i].vel = self.max_vel
                
        for i in range(1, len(self.waypoints)):
            new_v = sqrt(self.waypoints[i - 1].vel ** 2 + 2 * self.max_accel * self.waypoints[i - 1].get_distance(self.waypoints[i]))
            self.waypoints[i].vel = min([self.waypoints[i].vel, new_v])
    
    def smoother(self, lst):
        s = 0
        square = 0
        for i in range(1, len(lst)):
            s += abs(lst[i] - lst[i - 1])
            square += abs(lst[i] - lst[i - 1]) ** 2
        avg_diff = s/(len(lst) - 1)
        std_dev = sqrt(square / (len(lst) - 1))
        
        thresh = avg_diff + std_dev
        print(thresh)
        final = []
        final.append(lst[0])
        for i in range(1, len(lst) - 1):
            if abs(lst[i] - lst[i - 1]) <= thresh:
                final.append(lst[i])
            else:
#                 print("moved", lst[i] - lst[i - 1])
#                 if lst[i] - lst[i - 1] < 0:
                final.append((lst[i - 1] + lst[i + 1]) / 2)
#                 if lst[i] - lst[i - 1] > 0:
#                     final.append(lst[i] - thresh)
        final.append(lst[i])
                    
        return final
                
                
    def smoothPath(self, x, y, a, b, tolerance):
#         newPath = path[:];
        path_x = x[:]
        path_y = y[:]
        
        change = tolerance;
        
        while(change >= tolerance):
            change = 0;
            for i in range(1, len(x) - 1):
                origX = x[i]
                origY = y[i]
                
                newX = path_x[i]
                newY = path_y[i]
                
                lastX = path_x[i-1]
                lastY = path_y[i-1]
                
                nextX = path_x[i+1]
                nextY = path_y[i+1]
                
                augX = newX + a * (origX - newX) + b * (lastX + nextX - (2 * newX))
                augY = newY + a * (origY - newY) + b * (lastY + nextY - (2 * newY))
#                 print("x: %f\ny: %f\n" % (a*(origX-newX) + b*(lastX + nextX - (2*newX)),(origY-newY) + b*(lastY + nextY - (2*newY))))
                
                path_x[i] = augX
                path_y[i] = augY
                
                deltaX = abs(augX - newX)
                deltaY = abs(augY - newY)
#                 print("i = %d\n  ^x: %f\n  ^y: %f\n" % (i, deltaX, deltaY))
#                 print("i = %d, origX: %.2f, origY: %.2f, newX: %.4f, newY: %.4f, lastX: %.2f, lastY: %.2f, nextX: %.2f, nextY: %.2f, augX: %.4f, augY: %.4f, Delta X: %.4f, Delta Y: %.4f\n" % \
#                       (i, origX, origY, newX, newY, lastX, lastY, nextX, nextY, augX, augY, deltaX, deltaY))
                
                change += deltaX + deltaY
#                 print("change: %f\n" % (change))
        
        return path_x, path_y;
        
    def get(self):
        x = []
        y = []
        curv = []
        dist = []
        v = []
        
        for waypoint in self.waypoints:
            x.append(waypoint.x)
            y.append(waypoint.y)
            curv.append(waypoint.curv)
            dist.append(waypoint.dist)
            v.append(waypoint.vel)
            
        return x, y, curv, dist, v
        
    def __repr__(self):
        s = ""
        
        for waypoint in self.waypoints:
            s += str(waypoint) + "\n"
        return s
    
if __name__ == "__main__":
    points = [Point(0,0), Point(5, 0), Point(6, 5)]
#     points = [Point(0,0), Point(-5, 0), Point(-6, 5)]
#     path = Path(points, k=2, step = 0.1)
    
    x = [i for i in range(14)]
    y = [cos(i) + sin(i) for i in x]
#     points = [Point(x[i], y[i]) for i in range(len(x))]
    path = Path(points, k=1, step = 0.1)

    x, y, curv, dist, v = path.get()
# # #     
    plot.subplot(4, 1, 1)
    plot.scatter(x, y)
#      
    plot.subplot(4, 1, 2)
    plot.scatter(x, curv)
#     plot.show()
#     plot.plot(x, curv)
#     highest = 0
#     index = 0
#     for i in range(len(curv)):
#         if abs(curv[i]) > highest:
#             highest = curv[i]
#             index = i
#         
#     print(highest)
#     print(x[index], y[index], curv[index], index)
#      
    plot.subplot(4, 1, 3)
    plot.plot(x, dist)
      
    plot.subplot(4, 1, 4)
    plot.plot(x, v)
    plot.show()
    
#      
#     path1 = Path(points, k=1, step=0.01)
 
#     path1 = Path(points, k=1, step=0.01)
#     path2 = Path(points, k=2, step=0.01)
#     path3 = Path(points, k=3, step=0.01)
#     path4 = Path(points, k=4, step=0.01)
#     path5 = Path(points, k=5, step=0.01)
#     print(path)
     
#     x, y, curv, dist, v = path1.get()
#     
# #     plot.subplot(4, 1, 1)
# #     plot.scatter(x, y)
# #     
# #     plot.subplot(4, 1, 2)
# #     plot.plot(x, curv)
# #     
# #     plot.subplot(4, 1, 3)
# #     plot.plot(x, dist)
# #     
# #     plot.subplot(4, 1, 4)
# #     plot.plot(x, v)
 
#     p1 = path1.get()
#     p2 = path2.get()
#     p3 = path3.get()
#     p4 = path4.get()
#     p5 = path5.get()
#      
#     plot.subplot(6, 2, 1)
#     plot.plot(x, y)
#      
#     plot.subplot(6, 2, 3)
#     plot.title("k=1")
#     plot.scatter(p1[0], p1[4])
#      
#     plot.subplot(6, 2, 5)
#     plot.title("k=2")
#     plot.scatter(p1[0], p2[4])
#      
#     plot.subplot(6, 2, 7)
#     plot.title("k=3")
#     plot.scatter(p1[0], p3[4])
#      
#     plot.subplot(6, 2, 9)
#     plot.title("k=4")
#     plot.scatter(p1[0], p4[4])
#      
#     plot.subplot(6, 2, 11)
#     plot.title("k=5")
#     plot.scatter(p5[0], p5[4])
#      
# #     plot.show()
#      
#     plot.subplot(6, 2, 2)
#     plot.plot(x, y)
#      
#     plot.subplot(6, 2, 4)
#     plot.title("k=1")
#     plot.scatter(p1[0], path1.smoother(p1[4]))
#      
#     plot.subplot(6, 2, 6)
#     plot.title("k=2")
#     plot.scatter(p1[0], path2.smoother(p2[4]))
#      
#     plot.subplot(6, 2, 8)
#     plot.title("k=3")
#     plot.scatter(p1[0], path3.smoother(p3[4]))
#      
#     plot.subplot(6, 2, 10)
#     plot.title("k=4")
#     plot.scatter(p1[0], path4.smoother(p4[4]))
#      
#     plot.subplot(6, 2, 12)
#     plot.title("k=5")
#     plot.scatter(p5[0], path5.smoother(p5[4]))
#      
#     plot.show()


#     dt = datetime.now()
#     time = "{}{}{}{}{}{}".format(dt.month, dt.day, dt.year, dt.hour, dt.minute, dt.second)
#     print(time)
#     file = open("PathOuput" + time + ".csv", 'w')
#     file.write("%s, %s, %s, %s, %s\n" % ('x', 'y', 'curvature', 'distance', 'velocity'))
#     for i in range(len(x)):
#         file.write("%.4f, %.4f, %.4f, %.4f, %.4f\n" % (x[i], y[i], curv[i], dist[i], v[i]))
#     file.close()
#     print("finished writing")
# #     