def xyz(S):
    a=[]
    for n in S:
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                a.append(n)
    s=set()
    for i in range(-1,-len(a)-1,-1):
        s.add(a[i])
    print("{" + ", ".join(str(x) for x in a[::-1]) + "}")
                
                
n=int(input())
S=[]
for i in range(-1,-n-1,-1):
    j=int(input())
    S.append(j)
print(S)
xyz(S)