"""
Instructions
Now that you can tell the difference between pure and impure functions, let’s try it out.

Create a pure function to calculate the area of a circle given its radius.

Define a calculate_circle_area() function that takes the radius of the circle as input.
Compute the area of the circle using the formula: area=π∗r 
2
 .
Return the result.

"""

import math 

def calculate_circle_area(radius):
  return math.pi * (radius ** 2)
  # return 3.14 * radius ** 2

# radius_of_circle = 5
# area_of_circle = calculate_circle_area(radius_of_circle)
# print("Area of a circle:", area_of_circle)

print("Area of a circle:", calculate_circle_area(1))
print("Area of a circle:", calculate_circle_area(2))
print("Area of a circle:", calculate_circle_area(3))
print("Area of a circle:", calculate_circle_area(4))
print("Area of a circle:", calculate_circle_area(5))
