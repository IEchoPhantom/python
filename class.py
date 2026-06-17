# class work of fundamental of computer programming (3-8-2025)
# 1st code
# # get potential energy of an object
# m = float(input("Enter mass of the object in kg: "))
# g = float(input("Enter acceleration due to gravity in m/s^2: "))
# h = float(input("Enter height of the object in meters: "))
# if m < 0:
#     print("Invalid input. Mass must be non-negative.")
# elif h < 0:
#     print("Invalid input. Height must be non-negative.")
# else:
#     pe = m * g * h
#     print("The potential energy of the object is: ", pe, "Joules")
# # end of code


# # 2nd code 
# #tell which no. is smaller
# print("\t telling which number is smaller")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# if num1 < num2:
#     print("The smaller number is: ", num1)
# elif num2 < num1:
#     print("The smaller number is: ", num2)
# else:
#     print("Both numbers are equal.")
# # end of code


# # 3rd code                  ,my example : for if they can enter the club or not 
# age = int(input("Enter your age: "))
# has_ticket = input("Do you have a ticket? (yes/no): ")

# if age >= 18 and has_ticket == "yes":
#     print("Welcome to the club!")
# else:
#     print("Sorry, you can't enter.")
    
#Lab 2 (11/8/2025)

# i=10                  #Python variables are case sensitive
# print(type(i))        #type prints the data type of the variable 
# print(id(i))
#                       #id prints the memory address of the variable

#Commands to create variables of different data types
# i=10
# j=int(10)
# k=1.5
# l=float(1.5)
# m= "Anil is a good person"
# n=str("Anil is a good person")
# o= False
# p= bool(False)
# q=10+5j
# r= complex(10+5j)

#Execute the following:
# print(12,"is larger than",11)
# print("sum of",2,"and",3,"is",2+3)
# print("hi\nHi\nHi")
# print("hi\tHi\tHi")
# print("hi",end="**")
# #If you print something else after this, it will appear on the same line, right after the **.
# print("hi",end="")
# #This is useful when you want to print multiple items on the same line.
# print("hi")
# name= "alice"
# age= "30"
# print(f"{name}. you are {age} years old") 
#F-strings allow you to easily insert variable values into strings.

#type conversion
# i=10.5   
# print(type(i))    
# j=int(i)
# print(type(j))


#Write a program to find the grade of a student. Take marks as input from user. Also discuss the possible test cases.
 
# Marks= float(input("Enter your marks:"))
# if  100>=Marks>90:
#     print("Your grade is A")
# elif 90>=Marks>70:
#     print("Your grade is B")
# elif 70>=Marks>50:
#     print("Your grade is C")
# elif 50>=Marks>=0:
#     print("You have failed")
# else:
#     print("Invalid marks")
#     print("Please enter marks between 0 and 100.")

#Write a program to take a number as input and check the number is negative or positive. Add proper comment and show all possible test cases.

# a= float(input("Enter a number: "))
# if a>0:
#     print("The number is positive.")
# elif a<0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

#Write a program to take a number as input. Check whether the number is divisible by both 2 and 5. Add proper comment and show all possible test cases.

# a= float(input("enter your number: "))
# if a % 2 == 0 and a % 5 == 0:
#     print("The number is divisible by both 2 and 5.")
# else:
#     print("The number is not divisible by both 2 and 5.")


#Write a program to substract two complex numbers. Add proper comment and show all possible test cases.

# a = 2 + 3j
# b = 1 + 1j
# c = a - b
# print("The result of subtraction is:", c)
#end of code

# x=0b1101
# y=0b1111
# z=x+y
# print(bin(z))    #Numbers using only 0 and 1, written with 0b
# print(oct(z))    #Octal: Numbers using base 8,using digits 0–7, written with 0o 
# print(hex(z))    #Hexadecimal: Numbers using base 16,using digits 0–9 and letters A–F, written with 0x
# print(z)

# 

# ch=input("Enter a character:")
# print(ord(ch))  #ord() function returns the Unicode code point for a given character.


# _#v=20 
# #Variable name should not contain special charecters
# print(_#v)
# ==10
# if 10+10:
#    print(10)

# B=13
# b=18
# print(B+3)
# print(b+3)

# n1 = input('Enter a number:')
# n2 = input('Enter another number:')
# s = n1 + n2
# print('The sum of', n1, 'and', n2, 'is', s)
# The above code concatenates the two input strings instead of adding them as numbers.
# To fix this, we need to convert the input strings to numbers before adding them.
# n1 = float(input('Enter a number:'))
# n2 = float(input('Enter another number:'))
# s = n1 + n2
# print('The sum of', n1, 'and', n2, 'is', s)

# a=float(input("Enter a number:"))
# y=float(input("Enter a number:"))
# print(a/y)

# a=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# print(a%y)

# i=10+ "Amit Kumar"

# a=int("Amar")
# b=float("Anita")

# print(e)
# i=10
# l=i+w

#lab 4 18-8-25

# for x in range(2, 10, 3):
#   print(x,end=" ")

# for x in range(2, 10):
#   print(x,end=" ")

# for x in range(10):
#   print(x,end=" ")

# def nam(x):
#   n=int(input("Enter a number:"))
#   for i in range(1,n+1,x):
#     print(i,end=" ")

# #nam(1)
# nam(2)

# a = -1
# n=int(input("Enter a number:"))  #output= -1 3 -5 7 -9,…n
# for i in range(1, n+1, 2):
#     if a == -1:
#         print(i*a, end=" + ")
#     else:
#         print(i*a, end=" ")
#     a= a* -1

#or 
# n = int(input("enter number"))

# for i in range(1,n+1,2):
#   if i% 4 == 3:
#      print(i, end = " ")
#   else:
#     print(-i, end = " +")


# n=int(input("Enter a number:"))  
# a = -1
# s=0
# for i in range(1, n+1):
#     if a == -1:
#         s += i*a
#         print(i*a, end=" +")

#     else:
#         s += i*a
#         print(i*a, end=" ")
#     a= a* -1
# print("=",s)

# n=int(input("Enter a number:"))
# f=1
# for i in range(1, n+1):
#     f *= i
# print("The factorial of", n, "is", f)

# n=int(input("enter a no.:"))
# for i in range(1,n+1):
#     if i%3==0:
#         print("yay:",i)
#         continue
#     elif i%7==0:
#         print("ball:",i)
#         break
#     print("current:",i)

# n=input("Enter a number:") 
# s=0
# if not n.isdigit() or int(n)<=0:  #isdigit() checks if all characters in the string are digits
#     print("Invalid input. Please enter an +ve integer.")
# else:
#     n=int(n)
#     for i in range(1, n+1):
#         if i<n:
#             print(i, end=" + ")
#             s += i
#         else:
#             print(i, end=" ")
#             print("=",s)

# n=input("Enter a number:") 
# a=-1
# s=0
# if not n.isdigit() or int(n)<=0:
#     print("Invalid input. Please enter an +ve integer.")
# else:
#     for i in range(1, n+1):
#         if a == -1:
#             s += i*a
#             print(i*a, end=" +")

#         else:
#             s += i*a
#             print(i*a, end=" ")
#         a= a* -1
#     print("=",s)

# n = input("Enter a positive integer: ")
# if not n.isdigit():
#     print(" Invalid input! Please enter a positive integer.")
# else:
#     n = int(n)
#     print(f"Digits of {n}:")
#     while n > 0:
#         digit = n % 10 #to extract last digit
#         print(digit)
#         n //= 10  #to remove the last digit

# i = 0
# while i < 10:
#     i += 1

#     if i == 3:
#         print("Skipping 3 using continue")
#         continue

#     elif i == 6:
#         print("Breaking at 6 using break")
#         break

#     elif i == 5:
#         pass  # does nothing
#         print("Pass statement at 5 (no effect)")

#     print("Number:", i)

# n=input("Enter a number:") 
# s=0
# if not n.isdigit() or int(n)<=0:  #isdigit() checks if all characters in the string are digits
#     print("Invalid input. Please enter an +ve integer.")
# else:
#     n=int(n)
#     for i in range(1, n+1):
#         if n%i==0:
#             print(i)

# n=input("Enter a number:") 
# s=0
# if not n.isdigit() or int(n)<=0:  
#     print("Invalid input. Please enter an +ve integer.")
# else:
#     n=int(n)
#     for i in range(1, n+1):
#         if n%i!=0:
#             print("composite no:",i)

# #* prime number between 1 to n******
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,end=" ")

# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     print("1 " * i)

# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# n = int(input("How many terms? "))
# a, b = 0, 1
# for _ in range(n):
#     print(a,end=" ")
#     b = a + b
#     a = b - a

# Print the sum of the digits of the given number.
# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     digit = n % 10  #to extract last digit
#     sum += digit
#     n //= 10   #to remove the last digit
# print("Sum of digits:", sum)

#Q4 Create a function reverse() that returns the reverse of a number.
# def reverse(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10
#     return rev
# n = int(input("Enter a number: "))
# print("Reversed number:", reverse(n))

# #Write a program to check the given positive integer is prime or not.
# Test cases:n=0(not a positive integer), n=1 (1 is neither prime nor composite), n=3 , n=-5 (it is a negative number), n= 10, n= Ten (not a positive integer)

# n=input("Enter a number: ")
# if not n.isdigit() or int(n)<=0:  
#     print("Invalid input. Please enter an +ve integer.")
# else:
#     n=int(n)
#     if n <= 1:
#         print(f"{n} is neither prime nor composite.")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 print(f"{n} is a composite number.")
#                 break
#         else:
#             print(f"{n} is a prime number!")

# def add(n):
#    return n * (n+1)//2
# n = int(input("Enter a number: "))
# print("Sum of series 1 to",n, "is:",add(n))

# def prime(n):
#   if n <= 1:
#      return False
#   for i in range(2,n):
#      if n % i == 0:
#          return False
#   return True

# print(prime(6))
# print(prime(7))
# print(prime(1))

# def primefactors(num):
#    x = []
#    for i in range(2, num + 1):
#        if num % i == 0 and prime(i):
#            x.append(i)
#    return x
# n = int(input("Enter a no: "))
# print("Prime factors of", n , "are: ", primefactors(n))

# L = []
# L.append("apple")
# L.append(1)
# L.append(12.6)
# print(L)

# # Q2 Write a program to create a list of even numbers from 1 to 50.
# even_numbers = []
# for i in range(1, 51):
#     if i % 2 == 0:
#         even_numbers.append(i)
# print("Even numbers from 1 to 50 are:", even_numbers)

# # Q3 Answer the following questions for the list created in Q1. Use inbuilt methods to perform these operations.
# # Insert 14 at position 1 in the list.
# even_numbers.insert(1, 14)
# # Add 105 at the end of the list.
# even_numbers.append(105)
# # Count the number of 14 in the list.
# count_14 = even_numbers.count(14)
# # Remove element at location 2.
# even_numbers.pop(2)
# # Remove “12” from the list.
# even_numbers.remove(12)
# # Add the elements [1,2,36] at the end of the list.
# even_numbers.extend([1, 2, 36])
# # Print the index of element “14” in the list.
# index_14 = even_numbers.index(14)
# print(even_numbers)
# # Clear the list.
# even_numbers.clear()


# A = [
#     [4, 9, 3],
#     [4, 7, 9],
#     [1, 9, 1]
# ]
# B = [
#     [16, 4, 2],
#     [4, 3, 1],
#     [7, 89, 5]
# ]
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]

# for i in range(len(A)):              
#     for j in range(len(A[0])):       
#         result[i][j] = A[i][j] - B[i][j]

# print("Resultant Matrix (A - B):")
# for r in result:
#     print(r)

# n= int(input("Enter a number: "))
# print([i for i in range(1,n+1,2)])


# j=[1,2,3,4,5,2,3,4]
# result=[x for x in j if x<3]
# print(result)

# j = [1, 2, 3, 4, 5, 4]
# result = [6 if x == 4 else x for x in j]
# print("The updated list is", result)

# marks = [80, 50, 40, 90, 99]
# grades = ["A" if 90 <= i <= 100 else
#           "B" if 80 <= i < 90 else
#           "C" if 50 <= i < 80 else
#           "D" if 40 <= i < 50 else
#           "E" if 20 <= i < 40 else
#           "NC"
#           for i in marks]
# print(grades)

# fruits = ("Apple", "Banana", "Cherry", "Apple", "Orange",2, [1,2,3,4,5])
# print("Tuple:", fruits)
# print("First two elements:", fruits[:2])
# print("Last two elements:", fruits[-2:])
# print("Individual elements:")
# for fruit in fruits:
#     print(fruit)
# count = fruits.count("Apple")
# print("Number of times 'Apple' appears:", count)
# index = fruits.index("Apple")
# print("Index of 'Apple':", index)

#Q1 Write a function that returns the grade of a student. Pass marks of the student as argument to the function.
# def grade(marks):
#     if not marks.isdigit() or float(marks)<0:  
#         return "Invalid input. Please enter marks between 0 and 100."
#     else:
#         if  100>=float(marks)>90:
#             return "A"
#         elif 90>=float(marks)>70:
#             return "B"
#         elif 70>=float(marks)>50:
#             return "C"
#         elif 50>=float(marks)>=0:
#             return "You have failed"
# marks = input("Enter your marks:")
# print("Your grade is", grade(marks))

#Q2 Write a recursive function to return the summation of the series 1,2,3,4,5,…n.
# def add(n):
#    if n == 1:
#        return 1
#    else:
#        return n + add(n-1)
# n = int(input("Enter a number: "))
# print("Sum of series 1 to",n, "is:",add(n))

# Q3 Write a function to return the Fibonacci series. Pass n as parameter in the function.
#         Fibonacci series: 0,1,1,2,3,5…n
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=", ")
#         a, b = b, a + b
# n = int(input("Enter a number: "))
# fibonacci(n)

# dim= [int(x) for x in input().split()]
# def matrix(M1):
#     for row in range(dim[0]):
#         s=[int(x) for x in input().split()]
#         M1.append(s)
#     return M1

# l=[]
# m=[]
# matrix(l)
# matrix(m)

# result=[]
# for i in range(dim[0]):
#     row_sum=[]
#     for j in range(dim[1]):
#         row_sum.append(l[i][j] + m[i][j])
#     result.append(row_sum)
# print(result)

# import numpy as np
# import matplotlib.pyplot as plt

# plt.figure(figsize=(8, 6))
# plt.axis("equal")
# plt.title("Temple")
# plt.axis("off")

# # --- Base steps ---
# steps = [
#     (-6, -3, 12, 0.6),
#     (-5, -2.4, 10, 0.6),
#     (-4, -1.8, 8, 0.6),
# ]
# for (x, y, w, h) in steps:
#     plt.fill([x, x+w, x+w, x], [y, y, y+h, y+h], color="lightgray")

# # --- Floor ---
# plt.fill([-3.5, 3.5, 3.5, -3.5], [-1.2, -1.2, -1, -1], color="gray")

# # --- Pillars ---
# pillar_x_positions = [-3, -1, 1, 3]
# for px in pillar_x_positions:
#     plt.fill([px-0.3, px+0.3, px+0.3, px-0.3],
#              [-1, -1, 3, 3],
#              color="white", edgecolor="black")

# # --- Roof base ---
# plt.fill([-4, 4, 4, -4], [3, 3, 3.4, 3.4], color="gray")

# # --- Triangular roof ---
# roof_x = [-5, 5, 0]
# roof_y = [3.4, 3.4, 6]
# plt.fill(roof_x, roof_y, color="tan", edgecolor="black")

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# plt.figure(figsize=(10, 6))
# plt.axis("equal")
# plt.axis("off")
# plt.title("Shree Ram Mandir – Symbolic Representation")

# # ---------- Helper to draw polygons ----------
# def poly(points, color="gold", edge="brown"):
#     xs, ys = zip(*points)
#     plt.fill(xs, ys, color=color, edgecolor=edge)

# # ---------- Base Platform ----------
# poly([(-10, -3), (10, -3), (10, -1), (-10, -1)], "burlywood")

# # ---------- Steps ----------
# poly([(-12, -3), (12, -3), (12, -4), (-12, -4)], "tan")
# poly([(-13, -4), (13, -4), (13, -5), (-13, -5)], "wheat")

# # ---------- Main Mandapa (Hall) ----------
# poly([(-6, -1), (6, -1), (6, 3), (-6, 3)], "gold")

# # ---------- Side Mandapas ----------
# poly([(-10, -1), (-6, -1), (-6, 2), (-10, 2)], "goldenrod")
# poly([(6, -1), (10, -1), (10, 2), (6, 2)], "goldenrod")

# # ---------- Roof tiers ----------
# poly([(-7, 3), (7, 3), (0, 6)], "orange")
# poly([(-5, 6), (5, 6), (0, 8)], "darkorange")
# poly([(-3, 8), (3, 8), (0, 10)], "orangered")

# # ---------- Shikhar (Main Tower) ----------
# poly([(-1.5, 10), (1.5, 10), (0, 13)], "red")

# # ---------- Side Shikhars ----------
# poly([(-8, 2), (-6, 2), (-7, 5)], "indianred")
# poly([(6, 2), (8, 2), (7, 5)], "indianred")

# plt.show()

# print(sum(map(int, input("Enter a number: "))))
# import math

# # Calculate the cosine of different angles in radians

# angle_zero = 0.0
# angle_pi_over_3 = math.pi / 3    # 60 degrees
# angle_90_degrees = math.radians(90) # Convert 90 degrees to radians

# # Print the results
# print(f"The cosine of {angle_zero} radians is: {math.cos(angle_zero)}")
# print(f"The cosine of pi/3 radians is: {math.cos(angle_pi_over_3)}")
# print(f"The cosine of 90 degrees is: {math.cos(angle_90_degrees)}")
# print(math.inf)

# import random

# print(random.randint(6,8))
# # Output: 0.12345678901234567 (example, will vary)
# from numpy import random 
# x = random.rand() 
# print(x)

# from numpy import random 
# x=random.randint(100, size=(5)) 
# print(x)
# from numpy import random 
# x = random.rand(3, 5) 
# print(x)

# from numpy import random 
# x = random.choice([3, 5, 7, 9], size=(4, 5)) 
# print(x)
# import numpy as np 
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# # print(arr[0,0])
# # print(arr[1, 0:2])
# print(arr[0:2,0::2]) 
# # print(arr)
# import numpy as np 
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr[0,0,0])
# print(arr[0,0,-1]) 
# print(arr)
# #Print number of dimensions in the array
# print(arr.ndim)
# a=arr.shape #
# # print(a)
# # print(b)
# print(type(arr))

# arr = np.array(['1', '2', '3'], dtype=np.int16)
# print(arr)
# print(arr.dtype)

# import numpy as np 
# arr1 = np.array([8, 2, 3]) 
# arr2 = np.array([4, 5, 4])
# x = np.where(arr2 == 4)
# print(x)
# arr1=np.sort(arr1) 
# arr = np.concatenate((arr1, arr2)) 
# # print(arr)
# from scipy import constants

# print(constants.liter) 

# from scipy import constants 
# print("pi =",constants.pi) 
# print("gas constant:",constants.gas_constant)
# print(constants.find())
# import scipy.integrate
# from numpy import exp
# f= lambda x:exp(-x**2)
# i = scipy.integrate.quad(f, 0, 1)
# #for definite integrals we use quad
# print(i)
# #In output first value is the output of integration, second value is error margin
# import numpy as np
# # defining polynomial function
# var = np.poly1d([3, 2, 1])
# print("Polynomial function, f(x):\n", var)
# # calculating the derivative
# derivative = var.deriv()
# print("Derivative, f(x)'=", derivative)
# # calculates the derivative of after
# # given value of x
# print("When x=5 f(x)'=", derivative(5))

# import pandas as pd
# # Creating a DataFrame from a dictionary
# data = {
# "Name": ["Aarav", "Vanya", "Rohit", "Diya"],
# "Age": [23, 21, 24, 22],
# "City": ["Mumbai", "Delhi", "Bangalore", "Chennai"]
# }
# df = pd.DataFrame(data)
# #Writes the dataframe record in the csv file
# df.to_csv("D:\\out.csv")
# print(df) #Prints the complete dataframe
# print(df[:2]) #Prints first two rows in the dataframe
# print(df[-2::1]) #Prints the last two rows in the dataframe

# import pandas as pd  # Import pandas library for data manipulation

# # Create sample DataFrame matching the products.csv data
# data = {
#     'Product': ['Laptop', 'Phone', 'Table', 'Chair'],
#     'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture'],
#     'Price': [60000, 40000, 20000, 5000],
#     'Quantity': [10, 15, 5, 20]
# }
# df = pd.DataFrame(data)  # pd.DataFrame(): Creates a 2D tabular data structure from dictionary
# print("Original DataFrame:")
# print(df)

# # Calculate total value (Price * Quantity) and add as new column
# df['Total Value'] = df['Price'] * df['Quantity']  # Vectorized multiplication using pandas Series operations
# print("\nDataFrame with Total Value column:")
# print(df)
# import pandas as pd  # Import pandas library

# # Dictionary data as specified in question
# d1 = {
#     'Name': ['Aditya', 'Suman', 'Krish', 'Mark', 'Thomas'],
#     'Age': [20, 21, 19, 18, 20]
# }

# # Create DataFrame from dictionary
# df_student = pd.DataFrame(d1)  # pd.DataFrame(): Constructs DataFrame from dict of equal-length lists
# print("Student DataFrame:")
# print(df_student)

# # Save DataFrame to CSV file
# df_student.to_csv("D:\\new archit\\codes py\\student_data.csv", index=False)  # DataFrame.to_csv(): Exports DataFrame to CSV format, index=False excludes row indices
# print("\nDataFrame saved to D:\\new archit\\codes py\\student_data.csv")

# import pandas as pd  # Import pandas for CSV handling and data analysis
# import numpy as np   # Import numpy for NaN handling

# # Create sample salesdata.csv DataFrame
# sales_data = {
#     'Month': ['January', 'January', 'February', 'February', 'March', 'March'],
#     'Product': ['Laptop', 'Mobile', 'Laptop', 'Mobile', 'Laptop', 'Mobile'],
#     'UnitsSold': [100, 150, 120, np.nan, 130, 160],  # np.nan creates missing value
#     'Revenue': [500000, 300000, 600000, 400000, 650000, 450000]
# }
# df_sales = pd.DataFrame(sales_data)  # pd.DataFrame(): Converts dictionary to tabular DataFrame
# print("Original sales data:")
# print(df_sales)

# # a. Fill missing values in UnitsSold with column mean
# mean_units = df_sales['UnitsSold'].mean()  # Series.mean(): Computes arithmetic mean ignoring NaN
# df_sales['UnitsSold'].fillna(mean_units, inplace=True)  # DataFrame.fillna(): Replaces NaN values with specified value
# print("\nAfter filling missing UnitsSold with mean:")
# print(df_sales)

# # b. Total revenue per product using groupby
# total_revenue = df_sales.groupby('Product')['Revenue'].sum()  # groupby(): Groups data by category, sum(): Aggregates values
# print("\nTotal Revenue per Product:")
# print(total_revenue)

# # c. Product with highest revenue
# highest_revenue_product = total_revenue.idxmax()  # Series.idxmax(): Returns index of maximum value
# print(f"\nProduct with highest revenue: {highest_revenue_product}")
# import pandas as pd
# # df = pd.DataFrame({'A': range(10)})
# # print(df.head())   # Rows 0-4
# # print(df.tail())   # Rows 5-9
# df = pd.DataFrame({'A': [1, None, 3]})
# new_df = df.dropna()        # Original df unchanged
# df.dropna(inplace=True)     # Original df modified
# print(new_df)
# print(df)
# from abc import ABC, abstractmethod  # ABC module for abstract classes

# a) Person class
# class Person:
#     def __init__(self, name, dob):  # Initializes object attributes
#         self.name = name
#         self.dob = dob

# # b,d) Abstract Payment system
# class Payment(ABC):  # Abstract base class
#     @abstractmethod
#     def pay(self, amount):  # Abstract method - must be implemented
#         pass

# class CreditCardPayment(Payment):  # Inheritance + polymorphism
#     def pay(self, amount):
#         return f"Paid ${amount} via Credit Card"

# class PayPalPayment(Payment):
#     def pay(self, amount):
#         return f"Paid ${amount} via PayPal"

# def process_payment(payment_method, amount):  # Polymorphism - accepts any Payment
#     return payment_method.pay(amount)

# # Demonstration
# cc = CreditCardPayment()
# paypal = PayPalPayment()
# print(process_payment(cc, 100))     # Credit Card payment
# print(process_payment(paypal, 200))  # PayPal payment

text = "Hello World! Python is great."

print("replace(): Replaces substring")
print(text.replace("World", "Universe"))  # Replaces first occurrence

print("\nsplit(): Splits string into list")
words = text.split()  # Splits on whitespace -> ['Hello', 'World!', ...]
print(words)

print("\njoin(): Joins list elements into string")
print(" ".join(words))  # Joins with space separator
my_list = [1, 2, 3]

my_list.append([4, 5])      # Adds as SINGLE element [1,2,3,[4,5]]
my_list2 = [1, 2]
my_list2.extend([3, 4])     # Adds EACH element [1,2,3,4]
my_list2.insert(1, 99)      # Inserts at specific index [1,99,2,3,4]
print(my_list)
print(my_list2)
import pandas as pd
# df = pd.DataFrame({'A': range(10)})
# print(df.head(3))   # First 3 rows
# print(df.tail(2))   # Last 2 rows
df = pd.DataFrame({'A': [1, None, 3]})
print(df.fillna(0))         # Replaces NaN with 0
print(df.replace({None:9},regex=True)) # Replaces None values (not just NaN)

df = pd.DataFrame({'A': [10, 20, 30]}, index=['x', 'y', 'z'])
print(df.iloc[0])    # Position-based: row 0
print(df.loc['y'])   # Label-based: row 'y'
d = {'a': 1, 'b': 2}
d.update({'c': 3})      # Adds/updates multiple key-value pairs
d.popitem()             # Removes and returns last item
print(d.setdefault('d', 4))       # Adds key with default if missing
print(d.get('x', 0))    # Returns value or default (0)

with open('ego.txt', 'w') as f:
    f.write("Line1\nLine2\nLine3")

with open('ego.txt', 'r') as f:
    print(f.read())         # Reads entire file
    f.seek(0)               # Reset position
    print(f.readline())     # Reads first line + \n
    f.seek(0)
    print(f.readlines())    # Reads all lines as list
text = "pYthOn aSd"
print(text.capitalize())    # Python
print(text.title())         # Python
print(text.lower())         # PYTHON
print(text.casefold())      # python (Unicode-aware)
import numpy as np

matrix = np.array([[6, 3], [2, 8]])
det = np.linalg.det(matrix)  # Calculate determinant

if abs(det) < 1e-10:
    print("Matrix is not invertible (determinant ≈ 0)")
else:
    print(f"Determinant: {det}")
    inverse = np.linalg.inv(matrix)  # Calculate inverse
    print("Inverse:")
    print(inverse)
# Output: det=42, invertible matrix

