# Euler's Method Calculator
This is a simple calculator that implements Euler's method for approximating solutions to first order differential equations.
As long as the expression for a differential equation is known, the algorithm uses a linear approximation of the function to
calculate the next position defined by the step.  
To get started, you will need to enter the differential equation for the function you wish to approximate.
This can be done so under the function DE(x,y) in the code.
## Example:
Newton's law of cooling states that the change in temperature with respect to time is proportional to the difference in
temperature between an object and its surroundings. 
```
#Function Definition
def DE(x,y):
    return -1*(y-0.1)
What is the step size?0.1
What is the initial value of the function? (Enter as a comma separated list: x,y)0,10
For what domain should the function be approximated? (Enter as a comma separeted list: lower,upper)0,10
```
![diffeq](https://user-images.githubusercontent.com/47088251/203002791-e5c1ecea-3e97-4a5e-9c2d-b646cd1f2dd0.jpg)
