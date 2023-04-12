# Name:Hyeonseo Oh
# SBUID:115262920
##################### SCORE ######################
####### Score:  4/10
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
