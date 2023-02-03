#Name:                  Task 2.py
#Author:                Derek Baker
#Date Created:          03-02-2023
#Date Last Modified:    03-02-2023
#
#Purpose:
#
#The purpose of this program is to ask the user if they want to calculate the area of a circle, rectangle, or triangle. 
#The program will ask for the length of each side, and then present the area and the perimeter to the user.
#Most of this code will be copied from Task 1


import math
answer = input("Please enter if you would like to calculate the area of a triangle, " + \
               "circle, or rectangle. Or if you would like to exit: ") #Get the user's choice 

while not(answer.strip().upper() == "TRIANGLE" or answer.strip().upper() == "CIRCLE" or answer.strip().upper() == "RECTANGLE" or answer.strip().upper() == "EXIT"):
    answer = input("Please enter a valid answer: ")                                        #if the user enters an invalid answer, it will loop until they do 

if answer.strip().upper() == "TRIANGLE":
    triangleLength = float(input("Please enter the length of triangle in centimetres: "))           #Have the user enter the triangle length
    
    triangleArea = (triangleLength * triangleLength) / 2                            #Calculating the area and the perimeter
    trianglePerimeter = triangleLength * 3
    
    print("The area of the triangle is: " + str(triangleArea) + "cm^2.")
    print("The perimeter of the triangle is " + str(trianglePerimeter) + "cm.")
    
if answer.strip().upper() == "RECTANGLE":
    rectangleLength = float(input("Please enter the length of the rectangle: "))                #Have the user enter the rectangle length
    
    rectangleArea = rectangleLength * 2                                                #Calculate the reactangle area and perimeter
    rectanglePerimeter = rectangleLength * 4 
    
    print("The area of the rectangle is " + str(rectangleArea) + "cm^2.")
    print("The perimeter of the rectangle is " + str(rectanglePerimeter) + "cm.")
    
if answer.strip().upper() == "CIRCLE":
    circleRadius = float(input("Please enter the radius of the circle: "))                        #Have the user enter the circle radius
    
    circleArea = math.pi * (circleRadius * circleRadius)
    circlePerimeter = 2 * math.pi * circleRadius
    
    print("The area of the circle is " + str(circleArea) + "cm^2.")                     #Calculate the area and perimeter of the circle
    print("The perimeter of the circle is " + str(circlePerimeter) + "cm.")
    
if answer.strip().upper() == "EXIT":                    #If the user enters "exit", the program will end
    print("OK, goodbye.")