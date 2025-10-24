name="archit"    #variable 
age= 23                #integer variable
price = -19.99                #float variable

print (name)
print (age)
print (price)   
print (f"Hello {name}, you are {age} years old and the price is {price}.")    
# Using f-string for formatted output
#[f-string is a way to format strings in Python, allowing you to embed expressions 
# inside string literals, using curly braces `{}`.]
print ('')

age= 25
#
# Using f-string for formatted output
print ("Hello {name}, you are {age} years old and the price is {price}.")
#strings
greeting = "Hello"

print (greeting *4
       )
print (name,"is my name")

print (name + " is my name")              # Concatenating strings

result = name + greeting + " " + name
print (result)

result1 = name + greeting + " " , name       # This will create a tuple with two elements
print (result1)

result3 = name + result
print (result3)          # This will concatenate name and result
print ('')
aA1 = 10
print (aA1)

print (type(name)
       )
print (type(age))
print (type(price)) 
print (type(greeting))
print (type(result))
print (type(result1))              # This will print the type of result1
print ('')

my_tuple = (1,"apple", 3.14, True, "banana"     
# A tuple containing different data types
            )
print (my_tuple)
print (type(my_tuple))
print (my_tuple[0])       # Accessing the first element of the tuple
print (my_tuple[1])       # Accessing the second element of the tuple
print (my_tuple[2])
print (my_tuple[3])
print (my_tuple[-1])      # Accessing the last element of the tuple
print (my_tuple[-2])      # Accessing the second last element of the tuple
print (my_tuple[1:3])     # Slicing the tuple to get elements from index 1 to 2
print (my_tuple[1:4])
print (my_tuple[1:4:2])   # Slicing the tuple with a step of 2
print (my_tuple[1:4:3])   # Slicing the tuple with a step of 3
print (my_tuple[1:4:1])
 #print (my_tuple[1:4:0])  ## This will raise an error because step cannot be zero
 #print (my_tuple[1:4:-1])  
 # # This will raise an error because step cannot be negative in this context
print ('')


#"hello"  string

for i in range(5):            # looping through a range of numbers
    print(i)

import math     
print(math.pi)          
print ('')

name = 'Archit'
print(name[0])  # Accessing the first character
print (name)
print(name[1])  # Accessing the second character
print ('')

a= True
b= None
print (b)  # Printing the value of b
print (type(b))  # Checking the type of b
print (type (a))  # Checking the type of a
print (a)  # Printing the value of a      


print (name[0:3])  # Slicing the string to get the first three characters
print (name[1:4])  # Slicing the string to get characters from index1 to 3
print (name[1:])  # Slicing the string from index1 to the end  
print ('')


a=59856389
b=38127487
sum = a * b
print("The sum of", a, "and", b, "is:", sum)        

print ("hello world")
# print ("hello world")
# print ("hello world")
# print ("hello world")        # ctrl + / to comment out this line and multiple lines
print ("hello world")
#gooooooooooooooooooooo     "bui
# jkb"       # This is a single-line comment

"""
bjhy
hvybu
"""
# This is a multi-line comment
print ('')


#arithmetic operations
a = 10
b = 5
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum:", sum)
print("Difference:", difference)

print("Product:", product)
print("Quotient:", quotient)  #this will print in only float format
print(a+b) # This will print the sum of a and b
print (a%b)  # This will print the remainder of a divided by b
print (a//b)  # This will print the integer division of a by b
print (a**b)  # This will print a raised to the power of b
print (a**2)  # This will print a raised to the power of 2
print ('')


#relational operations
a = 10
b = 5
print(a > b)   # Greater than  
      # This will print True if a is greater than b, otherwise False
print(a < b)   # Less than      
      # This will print True if a is less than b, otherwise False
print(a >= b)  # Greater than or equal to  
      # This will print True if a is greater than or equal to b, otherwise False
print(a <= b)  # Less than or equal to     
      # This will print True if a is less than or equal to b, otherwise False
print(a == b)  # Equal to      
      # This will print True if a is equal to b, otherwise False
print(a != b)  # Not equal to   
      # This will print True if a is not equal to b, otherwise False
print ('')


#assignment operations
a = 100   #Assigns value 100 to a
b = 5
print(a)  # Initial value of a
print(b)  # Initial value of b

a += b  # Equivalent to a = a + b     # This will add b to a
print(a)  # Now a is 105
a -= b  # Equivalent to a = a - b     # This will subtract b from a
print(a)  # Now a is 100 again
a *= b  # Equivalent to a = a * b     # This will multiply a by b
print(a)  # Now a is 500
a /= b  # Equivalent to a = a / b     # This will divide a by b
print(a)  # Now a is 100.0 (float division)
a %= b  # Equivalent to a = a % b     # This will get the remainder of a divided by b
print(a)  # Now a is 0.0 (remainder of 10 divided by 5)
a += b  # Equivalent to a = a + b     # This will add b to a
print(a)  # Now a is 5
a += b  # Equivalent to a = a + b     # This will add b to a again
print(a)  # Now a is 10
a //= b  # Equivalent to a = a // b   # This will perform integer division of a by b
print(a)  # Now a is 2.0 (integer division)
a **= b  # Equivalent to a = a ** b   # This will raise a to the power of b
print(a)  # Now a is 32.0 (0 raised to the power of 5 is still 0)
print ('')


#logical operations
     # This code demonstrates various logical operations in Python
a= 50
b= 20
print(a > b and b < a)  # True if both conditions are true
print(a < b or b > a)   # True if at least one condition is true
print(not (a > b))      # True if the condition is false
print (not False)       # True, since not False is True
print (not True)        # False, since not True is False
print((a==b) and (b<a))  # This will print False, since a is not equal to b
print((a==b) or (b<a))   # This will print True, since b is less than a
print((a!=b) and (b<a))  
# This will print True, since a is not equal to b and b is less than a
print((a!=b) or (b>a))   # This will print True, since a is not equal to b

print ('')
a = True
b = False
print(a and b,a or b)  # Logical AND   
      # This will print True if both a and b are True, otherwise False
print(a and not b)  # Logical AND with NOT
print(a or b)   # Logical OR
print(not a)    # Logical NOT
print ('')

a=True 
b=True
print ("and operator:",a and b)  # Logical AND
print ("or operator:",a or b)    # Logical OR
print ("not operator:",not a)     # Logical NOT
print ('')



#bitwise operations,membership operations,identity operations,bitwise assignment operations
# are left for the user to implement as per their requirements.



#type conversion or implicit type conversion
# Python automatically converts types when necessary, such as when adding an integer and a float.
a = 10
b = 5.5
c = "20"
sum = a + b  # Adding an integer and a float
print("Sum of a and b:", sum) # This will print the sum as a float
#15.5
a, b = 1, "2.5"
# Reassigning a and b
# #values can be assigned in a single line with a comma
#error sum = a + b  int + str
sum = a + float(b)
print("Sum of a and b:", sum)
print("Type of sum:", type(sum))  # This will print the type of sum as float
print ("")


#type casting or explicit type conversion
print("Type of c:", type(c))  # This will print the type of c as str

num = int(c)  # Converting string to integer
print("Converted c to integer:", num)  # This will print the converted value
print("Type of num:", type(num))  # This will print the type of num as int

num_str = str(num)
print("Converted num to string:", num_str)  # This will print the converted value
print("Type of num_str:", type(num_str))  # This will print the type of num_str as str


#INPUTS IN PYTHON
# ===============================
# INPUTS IN PYTHON (Definitions & Notes for Beginners)
# ===============================
#
# 1. The input() function is used to take user input in Python. It always returns data as a string.
#
# 2. To get numbers (like integers or floats) from the user, you must convert the input string using int() or float().
#    Example: age = int(input("Enter your age: "))
#
# 3. You can provide a prompt inside input() to tell the user what to enter.
#    Example: name = input("Enter your name: ")
#
# 4. If the user enters something that cannot be converted (like letters when a number is expected), Python will show an error.
#    You can use try/except to handle such errors and give friendly messages.
#
# 5. You can use .split() to get multiple values from one input line.
#    Example: a, b = input("Enter two numbers: ").split()
#
# 6. All input from input() is text (string) until you convert it.
#
# 7. For yes/no questions, you can use .strip().lower() to make the answer easier to check.
#    Example: answer = input("Do you like Python? (yes/no): ").strip().lower()
#
# 8. Good input prompts help users know what to enter and avoid mistakes.
#
# ===============================
# End of INPUTS IN PYTHON notes
# ===============================
# INPUTS IN PYTHON (Beginner Guide)
# ===============================

# # 1. Basic string input
# name = input("Enter your name: ")
# print("Hello,", name)

# # 2. Integer input
# age = int(input("Enter your age: "))
# print("You are", age, "years old.")

# # 3. Float input
# price = float(input("Enter the price: "))
# print("The price is", price)

# # 4. Multiple inputs in one line (split)
# data = input("Enter two numbers separated by space: ")
# num1, num2 = data.split()
# num1 = int(num1)
# num2 = int(num2)
# print("Sum:", num1 + num2)

# # 5. Error handling for invalid input
# try:
#        value = int(input("Enter an integer: "))
#        print("You entered:", value)
# except ValueError:
#        print("That's not a valid integer!")

# # 6. Input with prompt and explanation
# user_input = input("Type anything and press Enter: ")
# print("You typed:", user_input)

# # 7. Input for boolean (yes/no)
# answer = input("Do you like Python? (yes/no): ").strip().lower()
# if answer == "yes":
#       print("Great!")
# elif answer == "no":
#       print("Oh no!")
# else:
#       print("Please answer with yes or no.")

# ===============================
# End of INPUTS IN PYTHON section


#PRACTICE QUESTIONS OF LECTURE 1 YT
#Q1. Write a program to input 2 numbers and print their sum

# a= float(input("enter a number in  number format: "))
# b= float(input("enter another number in number format: "))
# sum= a+b
# print("The sum is:", sum)

# Q2. WAP to input side of a square and print its area

# s= float(input("Enter the side of the square: "))
# print("The area of the square is:", s*s) # or s**2

# Q3. WAP to input 2 floating point numbers & print their average

# a= float(input("enter a number in  number format: "))
# b= float(input("enter another number in number format: "))
# average= (a+b)/2
# print("The average is:", average)

#Q4. WAP to input 2 int numbers a and b.Print true if a is greater than or equal to b.If not print false.

# a= float(input("enter a number:"))
# b= float(input("enter another number:"))

# if a>= b:                 # print(a>=b) can be taken as well
#     print("True")
# else:
#     print("False")

print("")

#===================================
# |||  SECOND LECTURE OF PYTHON  ||| (STRINGS AND CONDITIONAL STATEMENTS)
#===================================


# Escape sequence characters 
# (special combinations of characters used in programming (especially in strings) to represent characters that are difficult or impossible to type directly)
# and their meanings:
# \n : Newline (line break) ; Used to move the cursor to a new line, creating a line break in the output.
# \t : Tab; Inserts a horizontal tab space, useful for aligning text.
# \\ : Backslash; Allows you to include a backslash character in a string
# \' : Single quote; Lets you use a single quote inside single-quoted strings.
# \" : Double quote; Lets you use double quotes inside double-quoted strings.
# \r : Carriage return; Moves the cursor to the beginning of the line (carriage return), sometimes used to overwrite text.
# \b : Backspace; Deletes the character before it (backspace effect).
# \f : Form feed; Advances the cursor to the next page (form feed), rarely used in modern output.
# \a : Bell (alert); Triggers a system alert sound (bell), if supported.
# \v : Vertical tab; Inserts a vertical tab, moving the cursor down but not to the start of the next line.
#
# Examples of their use in Python:
# print("Hello\nWorld")      # Output: Hello (newline) World
# print("A\tB")              # Output: A    B (tab between A and B)
# print("C\\D")              # Output: C\D (single backslash)
# print('It\'s ok')          # Output: It's ok (single quote inside string)
# print("She said \"Hi\"")   # Output: She said "Hi" (double quotes inside string)
# print("Line1\rLine2")      # Output: Line2 (carriage return)
# print("Back\bspace")       # Output: Bacspace (b removes previous character)
# print("Form\ffeed")        # Output: Form (next line-)feed (form feed character)
# print("Bell\a")            # Output: Bell (may trigger alert sound)
# print("Vertical\vTab")     # Output: Vertical↕Tab (vertical tab)

print("Line01\rLine2")
str1 = "This is a string.we are creating it in python"
str2 = "yay\twe are in python"
final_str  = str1 + " " + str2
print(final_str)
print(len(final_str))
print(len(str1))   #len function gives the length of the string
# print(str1[0])     #indexing starts from 0 #output - t

#indexing
ch = str1[0] #it follows lowercase and uppercase letters
print(ch)
#str1[2] = "X" # This will raise an error because strings are immutable in Python

#slicing-accessing parts of a string 
print(str1[:4])
print(str1[4:])
print(str1[4:10]) # This will give characters from index 4 to 9
print(str1[:])  # This will give the whole string
print(str1[1:len(str1)])  # This will give the whole string except the first character
print(str1[0:len(str1):2])  # This will give every second character of the string
print(str1[2:0]) # This will give an empty string because the start index is greater than the end index
#negative slicing
print(str1[-1])  # This will give the last character of the string
print(str1[-5:-3])  # This will give characters from index -5 to -4

#string functions
str1="i am a coder."  
print(str1.endswith("er.")) # This will return True
print(str1.startswith("i am")) # This will return True
print(str1.find("coder")) # This will return 7
print(str1.count("a")) # This will return 2
print(str1.replace("coder", "programmer")) # This will return "i am a programmer."
print(str1.capitalize()) # This will return "I am a coder."
print(str1.find("fin")) # This will return -1
print(str1.lower()) # This will return "i am a coder."
print(str1.upper()) # This will return "I AM A CODER."
print(str1.title()) # This will return "I Am A Coder."
print(str1.islower()) # This will return True # This will return True if all characters are lowercase
print(str1.isupper()) # This will return False # This will return True if all characters are
str1= str1.capitalize() # This will change the first character to uppercase
print(str1)  

#WAP to input user"s first name and print its length
# n= str(input("Enter your first name: "))
# print(len(n))

#WAP to find the occurence of "$" in a string
n= "$12222 and $hfedbf %$$$$ hudbj"
print(n.count("$"))


#conditional statements
# if, elif, else
age = 21
if age <= 18:
    print("You are a minor.You are not eligible for license")
else:
    print("You are eligible for license") 

light = "pink"
if light == "red":
    print("Stop") 
elif light == "yellow":
    print("Get ready")
elif light == "green":
    print("Go")
else:
      print("Wrong color")

print("program ended")

#if and elif conditions can be used multiple in same indentation level 
# but else is used only once at end in same indentation level
#WAP to input marks and print the corresponding grade
# m= int(input("Enter your marks: "))
# if m>=90 and m<=100:
#     print("Your grade is A")
# elif m>=80 and m<90:
#     print("Your grade is B")
# elif m>=70 and m<80:
#     print("Your grade is C")
# elif  0<m<70 :
#     print("Your grade is D")
# elif m>100 or m<0:
#     print("Invalid Input")

#nesting of if-else 

#WAP to input a number and check if it is even or odd
# n= int(input("Enter a number: "))
# if n==0:
#     print("The number is zero")
# elif n%2==0:
#     print("the no. is even")
# elif n<0:
#     print("The number is negative")
# else:
#     print("the no. is odd")

#WAP to input 3 numbers and print the greatest number
# a= int(input("Enter first number: "))
# b= int(input("Enter second number: "))
# c= int(input("Enter third number: "))
# d= int(input("Enter fourth number: "))
# if a>=b and a>=c and a>=d:
#       print("The greatest number is:", a)
# elif b>=c and b>=d:
#       print("The greatest number is:", b)
# elif c>=d:
#       print("The greatest number is:", c)
# else:
#       print("The greatest number is:", d)

#WAP to check if a no. is a multiple of 7 or not
# n= int(input("Enter a number: "))
# if n%7==0:
#       print("The number is a multiple of 7")
# else:
#       print("The number is not a multiple of 7")


#===================================
# |||  THIRD LECTURE OF PYTHON  ||| (LIST AND TUPLES) / 9/9/2025
#===================================

marks=[90.87, 85.25, 78.0, 92.0, 88.0]  #list of floats 
print(marks)
print(type(marks))  # This will print the type of marks as list
print(len(marks))   # This will print the length of the list marks
print(marks[0])     # This will print the first element of the list
print(marks[1])     # This will print the second element of the list

student= ["archit", 23, 5.9, True] #list of different data types
print(student)
student[0]= "Archit"  # Modifying the first element of the list
print(student)
print(student[0])      # This will print the modified first element of the list
print(student[-1])     # This will print the last element of the list
print(student[1:3])    # This will print elements from index 1 to
print(student[::2])    # This will print every second element of the list
print(student[::-1])   # This will print the list in reverse order
print(student[1:4:2])  # This will print elements from index 1 to 3 with a step of 2
print(student[-3:-1]) # This will print elements from index -3 to -2
print(student[-1:-3]) # This will print an empty list because the start index is


#list methods
list1=[1,3,2]
list1.append(4)  # This will add 4 to the end of the list
print(list1)     # Output: [1, 3, 2, 4]
list1.insert(1, 5)  # This will insert 5 at index 1
print(list1)     # Output: [1, 5, 3, 2, 4]
list1.remove(3)  # This will remove the first occurrence of 3 from the
print(list1)     # Output: [1, 5, 2, 4]
list1.sort()
print(list1)     # Output: [1, 2, 4, 5]
list1.sort(reverse=True)
print(list1)     # Output: [5, 4, 2, 1]
list1.reverse()
print(list1)     # Output: [1, 2, 4, 5]
list1.insert(2, 10)  # This will insert 10 at index 2
print(list1)     # Output: [1, 2, 10, 4, 5]

list2= [7, 8, 9,3,1,4]
list2.reverse()
list2.append(6)
list2.reverse()
print(list2)
list2.remove(6)
list2.insert(0,6)
print(list2)

list2.extend(list1)
print(list2)    # This will print the combined list of list2 and list1
print(list2.sort())    # This will print none because sort() modifies the list in place and returns None
print(list2)  # This will print the sorted list2
print(sorted(list2))  # This will print the sorted combined list without modifying list2

#adding list2.sort inside print is useless as it will return None
#because sort() modifies the list in place and returns None
#and therfore to use other funstion on sorted(list2) is used or write it before and then print list2

list2.pop(0) # This will remove the last element of the list
print(list2)  # This will print the list after popping the last element

#tuples in python
# A tuple is a collection which is ordered and unchangeable (immutable).
# Tuples are written with round brackets.
my_tuple = (1, "apple", 3.14, True)
tup=(87,12,46,76, 909)
print(tup[0])
for i in tup:
#     print("\t", i)  # This will print each element of the tuple on a new line with a tab space
    print(i, end=" ")  # This will print each element of the tuple on the same line separated by a space

tup1= ()
print(type(tup1))  # This will print the type of tup1 as tuple
tup2= (1,)  # This is a tuple with a single element

tup2.count(1)  # This will return 1
print(tup2.index(1))  # This will return 0
print(len(tup2))  # This will return 1
print(tup.count(76))  # This will return 1

#WAP to ask the user to enter names of thier 3 favourite movies and store them in a list

# m= input("enter your favourite movie:")
# m1= input("enter your 2nd favourite movie:")
# m2= input("enter your 3rd favourite movie:")
# list1 =[m,m1,m2]
# print(list1)  

# or
# movies = []
# m= input("enter your favourite movie:")
# m1= input("enter your 2nd favourite movie:")
# m2= input("enter your 3rd favourite movie:")

# movies.append(m)
# movies.append(m1)
# movies.append(m2)
# print(movies)

#or
# movies = []
# movies.append(input("enter your favourite movie:"))
# movies.append(input("enter your 2nd favourite movie:"))
# movies.append(input("enter your 3rd favourite movie:"))
# print(movies)

#WAP to check if a list contains a palindrome of elements.(hint:use copy() method)
list1= ["madam", "hello", "racecar", "world", "python"]
list2= list1.copy()  # This will create a copy of list1 
list2.reverse()  # This will reverse the copy of list1
if list1==list2:
    print("The list contains a palindrome")
else:
    print("The list does not contain a palindrome")

#or
a=[2,1,3,1,2]
a2=a.copy() 
a2.reverse()
if a==a2:
    print("it is a palindrome")
else:
    print("not a palindrome")

#WAP to count the number of students with the "a" grade in the following list
#ii) store the above data in list and store them from "a" to "d"
tuple=("c","a","d","b","a","a")
t2=tuple.count("a")
t3=tuple.index("a")
# t3.sort()
print(t2)

#===================================
# |||  FOURTH LECTURE OF PYTHON  ||| (DICTIONARY AND SET) / 17/9/2025
#===================================

#dictionary in python
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
my_dict = {
    "name": "Archit", 
    "age": 23, 
    "is_student": True,
    "learning": ["Python", "Java", "C++"],  # List as a value
    "topics": (1,2,3),  # Tuple as a value
    12.99 : 23,  # Float as a key
    100: "hundred"  # Integer as a key
}
print(my_dict)  # This will print the whole dictionary
print(type(my_dict))  # This will print the type of my_dict as dict
print(len(my_dict))  # This will print the number of key-value pairs in the dictionary
print(my_dict["name"])  # This will print the value associated with the key "name"
print(my_dict["learning"])  # This will print the list associated with the key "learning
# print(my_dict[12]) #key error if key not present
my_dict["name"] = "archit"  # This will change the value associated with the key "name"
print(my_dict["name"])  # This will print the modified value associated with the key "name"
my_dict["surname"] = "sharma"  # This will add a new key-value pair to the dictionary
print(my_dict)  # This will print the updated dictionary

nulldict = {}  # This will create an empty dictionary
print(nulldict)
nulldict[1] = "one"  # This will add a key-value pair to the empty dictionary
print(nulldict)  # This will print the dictionary with the new key-value pair

st={
    "name": "archit",    # the key can also be a variable that was defined earlier
    "age": 23,
    "price ": 19.99,
    "subjects": {
        "s1": {
            "name" : "maths",
            "ch1" : "algebra"
        },
    "s2": "science"
    },
    "xxx": "hello"
}

print(st["subjects"])
print(st["subjects"]["s1"]["name"])  # This will print the value associated with the key "s1" in the nested dictionary

#dictionary methods
print(st.keys())  # This will print all the keys in the dictionary
print(st.values())  # This will print all the values in the dictionary
print(list(st.keys()))

print(st.items())  # This will print all the key-value pairs in the dictionary as tuples
pairs=list(st.items())  # This will convert the key-value pairs into a list of tuples
print(pairs)  # This will print the list of key-value pairs as tuples

print(pairs[0])  # This will print the first key-value pair as a tuple
print(pairs[0][0])  # This will print the key of the first key-value pair
print(pairs[0][1][0])  # This will print the first character of the value of the first key-value pair


print(st.get("age"))  # This will print the value associated with the key "age
print(st.get("xyz"))  # This will print None because the key "xyz" is not present in the dictionary
print(st.get("xyz", "Key not found"))  # This will print "Key not found" because the key "xyz" is not present in the dictionary
#print(st["xyz"])  # This will raise a KeyError because the key "xyz" is not present in the dictionary

new_d={
    "city": "delhi",
    "country": "india"
}
st.update(new_d)  # This will add the key-value pairs from new_d to the dictionary st
print(st)  # This will print the updated dictionary
#or
st.update({"name": "up"})   # This will update the value associated with the key "name"
print(st)  # This will print the updated dictionary

print(st.pop("xxx"))  # This will remove the key-value pair with the key "xxx" and print its value
print(st)  # This will print the dictionary after popping the key-value pair with the key "xxx"
st.popitem()  # This will remove the last inserted key-value pair from the dictionary
st.popitem()
st.popitem() #will also remove sub dictionary inside a dictionary
print(st)  # This will print the dictionary after popping the last inserted key-value pair



#SETS IN PYTHON
# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets {}
#each element is unique and no duplicates are allowed and it is immutable
#list and dictionary cannot be a element of set as they are mutable

s = {0, "2", 3.8, (4, 9, 0,0), 5, True, 1, "2",None}  # Duplicate values will be ignored
print(s)  # This will print the set with unique elements
print(type(s))  # This will print the type of s as set
nullset = set()  # This will create an empty set
a={} # This will create an empty dictionary
print(type(nullset))  # This will print the type of nullset as set
print(len(s))  # This will print the number of unique elements in the set

#set methods

s.add(7)  # This will add 7 to the set
print(s)  # This will print the set after adding 7  
s.remove(3.8)  # This will remove 3.8 from the set
print(s)  # This will print the set after removing 3.8
print(s.pop())  # This will remove and return an arbitrary element from the set    
print(s.pop())  # This will print the set after popping an element
s.clear()  # This will remove all elements from the set
print(s)  # This will print the empty set
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))  # This will print the union of s1 and s2
print(s1.intersection(s2))  # This will print the intersection of s1 and s2
print(s1.difference(s2))  # This will print the difference of s1 and s2 (elements in s1 but not in s2)
print(s1.symmetric_difference(s2))  # This will print the symmetric difference of s1 and s2 (elements in either s1 or s2 but not in both)
print(s1.issubset(s2))  # This will print False because s1 is not a subset of s2
print(s1.issuperset(s2))  # This will print False because s1 is not a superset of s2
print(s1.isdisjoint(s2))  # This will print False because s1 and s2 have common elements
print("")


#questions
#q1.store followinf data in dictionary if there are 2 values of same key store them in a list/tuple/set against that key
d={"table": {"a piece of furniture","list"},"cat":"a small animal"} 
#or d={"table": ["a piece of furniture","list"],"cat":"a small animal"}
print(d)
print(type(d["table"]))

#q2.given list of students and subjects. assume 1 classroom is required for 1 subject.HOW many cr needed 
s={"maths","science","english","hindi","computer","maths","science","science","english","hindi","computer","maths","science"}
print(len(s))

#wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dict and add one by one.use subject name as key and marks as value.

# marks=["maths","sci","sst"]
# d={}
# for i in marks:
#     n=int(input(f"enter marks for {i}:"))
#     d.update({f"{i} marks":n})
# print(d)

s = {9, 9.0, '9.0000'}
print(s)  # Output: {9, '9.0000'}

##wap figure out a way to store 9 and 9.0 as separate values
# To force both 9 and 9.0 as separate, use tuples with type info:
s = {(9, 'int'), (9.0, 'float'), '9.0000'}
print(s)  # Output: {(9, 'int'), (9.0, 'float'), '9.0000'}


#===================================
# |||  SIXTH LECTURE OF PYTHON  ||| (FUNCTION AND RECURSION) / 2/10/2025
#===================================

def hi(a):
    return f"Hello {a}"
hi("archit")
#this will print in python or collab but not in vscode and spyder
print(hi("archit"))  # This will print "Hello archit" in everything

def hello_world():
    return "Hello World"
print(hello_world())  # This will print "Hello World"

def none_func():
    print("This function does not return anything")

a= none_func()  # This will call the function and print the message
print(a)  # This will print None because the function does not return anything

def avg(a,b,c):
    return (a+b+c)/3
avg(3,4,6)
print(avg(3,4,5))  # This will print the average of 3, 4 and 5

def abc(a,b=1):  # Default values for a and b
    return a+b, a-b, a*b, a/b
    print("This line will not be executed") # This line will not be executed because it is after the return statement

# print(abc())  # This will raise an error because the function requires 2 arguments if no default values are given
print(abc(5))  # This will print the result of 5+1, 5-1, 5*1 and 5/1

#questions
#WAP to find the length of a string and a list using function
def length(a):
    return len(a)
print(length("archit"))  # This will print the length of the string "archit"
print(length([1,2,7,4,5]))  # This will print the

#wap to print each element of a list using function
def elements(a):
    for i in a:
        print(i, end="\n")
    return
elements([1,2,3,4,5])  # This will print each element of the list on a new line

#wap to find the factorial of a number using function
def fact(n):
    for i in range(1,n):
        n= n*i
    print(n)
fact(11)  # This will print the factorial of 5

#wap to convert celsius to fahrenheit and vice versa using function
def converter(celsius):
    return (celsius * 9/5) + 32
print(converter(0))  # This will print 32.0
print(converter(100))  # This will print 212.0

def conververter(fahrenheit):
    return (fahrenheit - 32) * 5/9  
print(conververter(32))  # This will print 0.0
print(conververter(212))  # This will print 100.0

# def even():
#     if n%2==0:
#         return "True"
#     else:
#         return "False"
# n= int(input("Enter a number: "))
# print(even())  # This will print True if the number is even, otherwise False

#Recursion in python
# A recursive function is a function that calls itself in order to solve a problem.
# It typically has a base case to stop the recursion and a recursive case to continue the recursion
def recursive_function(n):
    if n <= 0:
        print(end="\n")
        return "Base case reached"
    else:
        print(n,end=" ")
        return recursive_function(n - 1)
    
print(recursive_function(5))  # This will print 5, 4, 3, 2, 1 and then "Base case reached"

def show(n):
    if n==0:
        return
    print(n,end=" ") #print before the recursive call
    show(n-1)
    print(n,end=" ") #print after the recursive call
show(5)  # This will print 5, 4, 3, 2, 1, 1, 2, 3, 4, 5

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print("\n\t",factorial(5))  # This will print 120
print(factorial(0))  # This will print 1

#recursion to find the nth fibonacci number
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))  # This will print 13
print(fibonacci(10))  # This will print 55

#WAP to find the sum of first n natural numbers using recursion
def sum_n(n):
    if n==0:
        return 0
    else:
        return n + sum_n(n-1)
print(sum_n(5))  # This will print 15

#WAP to find the sum of digits of a number using recursion
def sum_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_digits(n//10)
print(sum_digits(1234))  # This will print 10
print(sum_digits(5678))  # This will print 26

#WAP to find the reverse of a string using recursion
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("archit"))  # This will print "tihcra"

#WAP to check if a string is a palindrome using recursion
def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and is_palindrome(s[1:-1])
print(is_palindrome("madam"))  # This will print True
print(is_palindrome("hello"))  # This will print False

#rec func to print all elements of a list
def print_list(lst):
    if len(lst)==0:
        return
    else:
        print(lst[0], end=" ")
        print_list(lst[1:])
print_list([1,2,3,4,5])  # This will print 1 2 3 4 5

#or
def print_list2(lst, index=0):
    if index==len(lst):
        return
    else:
        print(lst[index], end=" ")
        print_list2(lst, index+1)

print_list2([1,2,3,4,5])  # This will print 1 2 3 4 5