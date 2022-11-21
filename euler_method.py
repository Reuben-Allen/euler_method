"""
Reuben Allen
Created on Thu Apr 8 2021
"""
from matplotlib import pyplot as plt
import math

#User input for variables
step = float(input("What is the step size?"))
if step == 0:
    print("Error: Zero not a valid step")
initial = input("What is the initial value of the function? (Enter as a comma separated list: x,y)").split(',')
domain = list(map(float, input("For what domain should the function be approximated? (Enter as a comma separeted list: lower,upper)").split(',')))
x_list = [float(initial[0])]
y_list = [float(initial[1])]

if domain[0] > x_list[0] or domain[1] < x_list[0]:
    print("Error: Initial value should be included in the domain")

#Determining the number of steps
steps_pos = round((domain[1] - x_list[0]) / step)
steps_neg = round((x_list[0] - domain[0]) / step)

#Function Definition
def DE(x,y):
    return -1*(y-0.1)

#Euler's Method
for n in range(steps_pos):
    y_0 = y_list[n]
    x_0 = x_list[n]
    x = step + x_0
    y = y_0 + step * DE(x_0,y_0)
    x_list.append(x)
    y_list.append(y)
if steps_neg != 0:
    for n in range(steps_neg):
        y_0 = y_list[0]
        x_0 = x_list[0]
        x = x_0 - step
        y = y_0 - step * DE(x_0,y_0)
        x_list.insert(0, x)
        y_list.insert(0, y)
    
#Plot
plt.plot(x_list,y_list)
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, linestyle = "dashed", color = "r")
plt.axvline(0, linestyle = "dashed", color = "r")
plt.show()