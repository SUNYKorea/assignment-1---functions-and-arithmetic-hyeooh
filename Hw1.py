# Name:Hyeonseo Oh
# SBUID:115262920
##################### SCORE ######################
####### Score:  7.5/10

#################################################
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear().


######################Entire code without main method!! --> no output #########################

def farenheit2celsius(farenheit):
    return 5/9*(farenheit-32)


def what_to_wear(celcius):
    if(celcius<-10):
        print("Wear a Puffy jacket")
    elif(-10<=celcius) and (celcius<=0):
        print("Wear a Scarf")
    elif(celcius>=0) and (celcius<=10):
        print("Wear a Sweater")
    elif(celcius>=10) and (celcius<=20):
        print("Wear a Light jacket")
    else:
        print("Wear a T-shirt")


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs (((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2)) / 2)
    return area

def euclidean_distance(x1, y1, x2, y2):
    distance = (((x1 - x2)**2)+((y1 + y2)**2))**(1/2)
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = euclidean_distance(x1, y1, x2, y2)
    side2 = euclidean_distance(x2, y2, x3, y3)
    side3 = euclidean_distance(x3, y3, x1, y1)
    perimeter = side1 + side2 + side3
    perimeter = ((((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)) + ((((x3 - x2)**2) + ((y3 - y2)**2))**(1/2)) + ((((x1 - x3)**2) + ((y1 - y3)**2))**(1/2))
    return perimeter


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    return math.pi * degrees / 180

def apothem(number_sides, length_side):
   n = number_sides
   s = length_side
   a = s / 2*tan(180 / n)
   angle = 180 / n
   radian = deg2rad(angle)
   return s / (2* math.tan (radian))

def polygon_area(number_sides, length_side):
    A = n*s*a / 2
    a = apothem (n, s)
    return (n * s* a) / 2



# #########################################################################################################Code shared by professor

# Name:Hyeonseo Oh
# SBUID:115262920
## Score: 7/10
# your output

# (base) D:\sortVMAF>D:/anaconda/python.exe j:/HO.py
# Wear a Sweater
# The area of the triangle is : 32.0 , its perimeter is : 27.440161448987652
# Traceback (most recent call last):
#   File "j:\HO.py", line 87, in <module>
#     print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))
#   File "j:\HO.py", line 66, in polygon_area
#     A = n*s*a / 2
# NameError: name 'n' is not defined
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear().
import math
def fahrenheit2celsius(farenheit):
    return 5/9*(farenheit-32)


def what_to_wear(celcius):
    if(celcius<-10):
        print("Wear a Puffy jacket")
    elif(-10<=celcius) and (celcius<=0):
        print("Wear a Scarf")
    elif(celcius>=0) and (celcius<=10):
        print("Wear a Sweater")
    elif(celcius>=10) and (celcius<=20):
        print("Wear a Light jacket")
    else:
        print("Wear a T-shirt")


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs (((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2)) / 2)
    return area

def euclidean_distance(x1, y1, x2, y2):
    distance = (((x1 - x2)**2)+((y1 + y2)**2))**(1/2)
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = euclidean_distance(x1, y1, x2, y2)
    side2 = euclidean_distance(x2, y2, x3, y3)
    side3 = euclidean_distance(x3, y3, x1, y1)
    perimeter = side1 + side2 + side3
    perimeter = ((((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)) + ((((x3 - x2)**2) + ((y3 - y2)**2))**(1/2)) + ((((x1 - x3)**2) + ((y1 - y3)**2))**(1/2))
    return perimeter


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    return math.pi * degrees / 180

def apothem(number_sides, length_side):
   n = number_sides
   s = length_side
   a = s / 2*tan(180 / n)
   angle = 180 / n
   radian = deg2rad(angle)
   return s / (2* math.tan (radian))

def polygon_area(number_sides, length_side):
    A = n*s*a / 2
    a = apothem (n, s)
    return (n * s* a) / 2

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))