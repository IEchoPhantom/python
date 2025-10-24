# n1=int(input("enter a no.:"))
# n2=int(input("enter another no.:"))
# o= input("enter a operator u want to use(+,-,*,/,%):")
# if o=='+':
#     print(n1+n2)
# elif o=='-':
#     print(n1-n2)
# elif o=='*':
#     print(n1*n2)
# elif o=='/':
#     print(n1/n2)
# elif o=='%':
#     print(n1%n2)
# else:
#     print("invalid operator")

# age=int(input("Enter your age:"))
# if age>=18:
#     print("major")
# else:
#     print("minor")

#loops
# n=1
# while n<=10:
#     print(n)
#     n=n+1

#WAP to ask the user a no. that he wants a no. of multiplication table
# n=int(input("enter a no.:"))
# a=1
# while a<=10:
#     print(f"{n} * {a} =",n*a)
#     a=a+1

#loops
# for i in range(1,11,2):
#     print(i)

#wap to print even nos. from 0 to 100 and constraint is to add in range 0 but not print it
# for i in range(0,101,2):
#     if i==0:
#         continue   #continue is used to skip the code and repeat the loop
#     else:
#         print(i)

#break 
# for i in range(1,11):
#     if i==5:
#         break   #break is used to stop the loop
#     else:
#         print(i)

#wap to print nos. from 1 to 20 but skip multiple of 3 using while loop
# i=1
# while i<=20:
#     if i%3==0:
    
#     else:
#         print(i)
#     i+=1


# i=1
# while i<=20:
#     if i%3==0:
#         i=i+1
#         continue
    
#     else:
#         print(i)
#     i+=1

# n=int(input("Enter a no.:"))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("it is not a prime no.")
#             break
#     else:
#         print("it is a prime no.")
# else:
#     print("Number should be greater than 1 to check for prime.")


#if...else → decision for each item.
#for...else → decision about the whole loop.

#WAP to print sum of first 20 natural nos.
# x=0
# for i in range (1,21):
#     x=x+i
# print(x) #this allows the loop to finish and 
#then run print func so it full output after sum 

#WAP to ask user email and password until he enters correct password
# a=input("enter your email:")
# while True:
#     b=input("enter your pass:")
#     if b == "Python":
#         print("you are welcome")
#         break

# WAP Take a number and check if it is positive, negative, or zero.
# n=float(input("enter a number:"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")

#wap Take a number and check if it is even or odd.
# n=int(input("enter a number:"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

#Take marks (0–100) as input and print:
# •	90+ = A
# •	75-89 = B
# •	50-74 = C
# •	Below 50 = Fail

# n=float(input("enter your marks:"))
# if 0<=n<=100:
#     if n>=90:
#         print("a grade")
#     elif 75<=n<=89:
#         print("b grade")
#     elif 50<=n<=74:
#         print("c grade")
#     else:
#         print("fail")
# else:
#     print("invalid input")

#Take an age and print if the person is child (<13), teenager (13–19), or adult (20+).
# n=int(input("enter your age:"))
# if n>0:
#     if n>=20:
#         print("adult")
#     elif 13<=n<=19:
#         print("teenager")
#     else:
#         print("child")
# else:
#     print("invalid age")

#Take a number from the user and check if it is divisible by both 3 and 5.
# n=int(input("enter a no.:"))
# if n%3==0 and n%5==0:
#     print("divisible")
# else:
#     print("not divisible")
 
#Print numbers from 1 to 10, but skip 5 (use continue ).
# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i)

#Print numbers from 1 to 10, but stop if you reach 7 (use break ).
# for i in range(1,11):
#     if i==7:
#         break
#     else:
#         print(i)

#Keep taking numbers from the user, stop if they enter a negative number.
# while True:
#     n=int(input("enter a no.:"))
#     if n>=0:
#         continue
#     else:
#         break

#1.	Print numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)

#2.	Print the square of numbers from 1 to 5.
# for i in range(1,6):
#     print(i**2)

# 3.	Print all numbers from 1 to 50 that are even.
# for i in range(1,51):
#     if i%2==0:
#         print(i)
#     else:
#         continue

#4.	Print the multiplication table of 7 (from 7×1 up to 7×10).
# n=int(input("enter a no.:"))
# for x in range(1,11):
#       print(f"{n}*{x} = {n*x}")

#wap using while loop print all element of tuple or list
t1=("abc","bcd","cde")
s=len(t1)
x=0
while x<s:
    print(t1[x])
    x=x+1