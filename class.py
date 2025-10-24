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