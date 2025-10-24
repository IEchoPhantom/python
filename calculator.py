n=float(input("enter a number:"))
m2='y'
while m2=="y":
    m=input("enter a operation(+,-,*,/):")
    n1=float(input("enter another no.:"))
    m1= input("enter =:")
    if m1 == "=":
        if m=="+":
            n=n+n1
        elif m=="-":
            n=n-n1
        elif m=="*":
            n=n*n1
        elif m=="/":
            n=n/n1
        print(n)
    print()
    m2=input("do u want to want to continue(y/n):")
    print()
    if m2.lower()=="y":
        continue
    else:
        break
print("Thank you")