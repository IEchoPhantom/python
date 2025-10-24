#wap to check whether the given year is a leap year or not. without using elif,function.
# a = input("Enter a number: ")
# print(type(a))
# a = int(a)
# print(type(a))

# if a % 4 == 0 and a % 100 != 0:
#     print("leap year.")
# else:
#     if a % 400 == 0:
#         print("leap year")
#     else:
#         print("not a leap year")

#or
# a=int(input("Enter a year: "))
# if (a%4==0 and a%100!=0) or a%400==0:
#     print("leap year")
# else:
#     print("not a leap year")

# wap to check whether the given number is even or odd without using arithmatic operators
# x=int(input("Enter a number: "))
# for i in range(0,x+1,2):
#     if i==x :
#         print("even")
#         break
# else:
#     print("odd")

d={
    'a' :'apple',
    'b' :'banana',
    'c' :'cherry',
    'd' :'dates',
    'e' :'eggfruit',
    'f' :'figs'
}

x=list(d.keys())
y=list(d.values())
x.reverse()
print(x)
n={}
# print(n.update({y, z})) it only takes one argument and returns None
# print(n.update(zip(y, z))) it returns None
n.update(zip(x,y))
print(n)
print(dict(zip(x,y)))


#or

x=list(d.keys())
y=list(d.values())
x.reverse()
n={}
n.update([(x[i], y[i]) for i in range(len(x))])
print(n)

#or 
x=list(d.keys())
y=list(d.values())
n={}
for i in range(len(x)-1,-1,-1):
    n[x[i]]=y[i]
print(n)


#functions 
def show_info():
    n = int(input("Enter number of key-value pairs: "))
    d = {}
    for i in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        d[key] = value
    print(d)

show_info()

