#QUESTION THAT TO MIND
#Q1 HOW TO TAKE INPUT AND PRINT REVERSE OF WHATEVER IS THE INPUT EX HELOO WORLD TO WORLD HELLO


# print(*sorted(input().split(), reverse=True))
# print(*input().split()[::-1])                          better

# print(input().split()[::-1])

# SELECTION SORTING
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part 
# and putting it at the beginning. The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

# shortcut to remember: selection sort is like selection of minimum element and putting it at the beginning of the array.
#diagram: "D:\new archit\codes py\python\dsa logic images\sorting.png"
# The selection sort algorithm is not a stable sorting algorithm. It is an in-place sorting algorithm.
# Time complexity: O(n^2) in all cases

import numpy as np 
def selection_sort():
    a=np.array([int(i) for i in input().split()])
    n=len(a)
    for i in range (0,n):
        mi=i
        for j in range(i+1,n):
            if a[j]<a[mi]:
                mi=j
        if a[i]>a[mi]:
            a[i],a[mi]=a[mi],a[i]
        print (f"Pass {i+1}: {a}")

#selection_sort()

#BUBBLE SORTING
# The bubble sort algorithm is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements 
# and swaps them if they are in the wrong order.
# The algorithm gets its name from the way smaller elements "bubble" to the top of the list (beginning of the array)
# The bubble sort algorithm is a stable sorting algorithm. It is an in-place sorting algorithm.
# Time complexity: O(n^2) in all cases
#diagram: "D:\new archit\codes py\python\dsa logic images\sorting.png"
#SHORTCUT TO REMEMBER: BUBBLE SORT IS LIKE BUBBLING UP THE LARGER ELEMENTS TO THE END OF THE ARRAY.

def bubble_sort():
    a= np.array([int(i) for i in input().split(" ")])
    x=len(a)
    for i in range (0,x):
        swap=False
        for j in range(0,x-i-1):
            if a[j]>a[j+1]:
                swap=True
                a[j],a[j+1]=a[j+1],a[j]
        print (f"Pass {i+1}: {a}")        
        if swap==False:
            break
#bubble_sort()


#INSERTION SORTING
# The insertion sort algorithm is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
# It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
# The insertion sort algorithm is a stable sorting algorithm. It is an in-place sorting algorithm.
# Time complexity: O(n^2) in all cases
#best case: O(n) when the array is already sorted.
#diagram: "D:\new archit\codes py\python\dsa logic images\
#remember: insertion sort is like inserting the elements in their correct position in the sorted part of the array.

def insertion_sort():
    a=np.array([int(i) for i in input().split()])
    n=len(a)
    for j in range(1,n):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
        print(f"Pass {j}:{a}")

# insertion_sort()


#MERGE SORTING
# The merge sort algorithm is a divide and conquer algorithm that sorts an array by recursively dividing it into smaller subarrays until each subarray contains a single element, and then merging those subarrays back together in sorted order.
# The merge sort algorithm is a stable sorting algorithm. It is not an in-place sorting algorithm
# Time complexity: O(n log n) in all cases
#diagram: "D:\new archit\codes py\python\dsa logic images\sorting.png"
#shortcut to remember: merge sort is like dividing the array into smaller subarrays and then merging
# those subarrays back together in sorted order.
# The merge sort algorithm is a recursive algorithm that divides the array into two halves, sorts each half, and then merges the sorted halves back together. The merge function is responsible for merging two sorted subarrays into a single sorted array.
#remember: merge sort is like dividing the array into smaller subarrays and then merging those subarrays back together in sorted order.

def merge(a,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if a[left]<=a[right]:
            temp.append(a[left])
            left+=1
        else:
            temp.append(a[right])
            right+=1
    while left<=mid:
        temp.append(a[left])
        left+=1
    while right<=high:
        temp.append(a[right])
        right+=1
    for i in range(len(temp)):
        a[low+i]=temp[i]
    
def mergesort(a,low,high):
    if low<high:
        mid=(low+high)//2
        mergesort(a,low,mid)
        mergesort(a,mid+1,high)
        merge(a,low,mid,high)
# a=np.array([int(x) for x in input().split()])
# low=0
# high=len(a)-1             
# mergesort(a,low,high)
# print(a)



#BINARY SEARCH
# The binary search algorithm is a search algorithm that finds the position of a target value within a
#sorted array. The binary search algorithm is a divide and conquer algorithm that works by repeatedly dividing the search interval in half until the target value is found or the search interval is empty.
# The binary search algorithm is a logarithmic time complexity algorithm with a time complexity of O(log n) in all cases. The binary search algorithm is not a stable sorting algorithm. It is an in-place sorting algorithm.
#REMEMBER: BINARY SEARCH IS LIKE DIVIDING THE SEARCH INTERVAL IN HALF UNTIL THE TARGET VALUE IS FOUND OR THE SEARCH INTERVAL IS EMPTY.

def binarysearch(a,target):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if target==a[mid]:
            print(f"found at {mid} index")
            return mid
        elif target>a[mid]:
            low=mid+1
        else:
            high=mid-1
    print("not found")
# a=np.array(sorted([int(x) for x in input().split()]))
# t=8
# binarysearch(a,t)


# Patterns 
# ****
# ****
# ****
# ****
def pattern1():
    n=int(input())
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

# pattern1()
# c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     for (int i = 0; i < 4; i++) {
#         for (int j = 0; j < 4; j++) {
#             cout << "*";
#         }
#         cout << endl;
#     }
#     return 0;
# }

#pattern 2
# *
# **
# ***
# ****
def pattern2():
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
# pattern2()
# c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     for (int i = 0; i < 4; i++) {
#         for (int j = 0; j < i + 1; j++) {
#             cout << "*";
#         }
#         cout << endl;
#     }
#     return 0;
# }

#pattern 3
# 1
# 12
# 123
def pattern3():
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        print()
# pattern3()
#OR
def pattern3():
    n=int(input())
    list1=[]
    for i in range(1,n+1):
        for j in range(i,i+1):
            list1.append(j)
            print(*list1)
# pattern3()
#c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n+1; i++) {
#         for (int j = 0; j < i + 1; j++) {
#             cout << j + 1;
#         }
#         cout << endl;
#     }
#     return 0;
# }


#pattern 4
# ****
# ***
# **
# *
def pattern4():
    n=int(input())
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        print()
# pattern4()
# #include <iostream>
# using namespace std;
# int main() {
#     for (int i=0;i<4;i++){for (int j=i;j<4;j++){cout<<"* ";}cout<<"\n";}return 0;}


#pattern 5
# 1
# 22
# 333
def pattern5():
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print()
# pattern5()
#c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j < i + 1; j++) {
#             cout << i + 1;
#         }
#         cout << endl;
#     }
#     return 0;
# }

#pattern 6
# 1 2 3 4
# 1 2 3
# 1 2
# 1
def pattern6():
    n=int(input())
    for i in range(n):
        for j in range(i,n):
            print(j+1,end=" ")
        print()
# pattern6()
#c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = i; j < n; j++) {
#             cout << j + 1 << " ";
#         }
#         cout << endl;
#     }
#     return 0;
# }


#pattern 7
#   *
#  ***
# *****
def pattern7():
    n=int(input())
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
# pattern7()
#c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j < n - i - 1; j++) {
#             cout << " ";
#         }
#         for (int k = 0; k < 2 * i + 1; k++) {
#             cout << "*";
#         }
#         cout << endl;
#     }
#     return 0;
# }

#pattern 8
# *****
#  ***
#   *
def pattern8():
    n=int(input())
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(n-i)-1):
            print("*",end="")
        print()
# pattern8()
#c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j < i; j++) {
#             cout << " ";
#         }
#         for (int k = 0; k < 2 * (n - i) - 1; k++) {
#             cout << "*";
#         }
#         cout << endl;
#     }
#     return 0;
# }

#pattern 9
# *
# **
# ***
# **
# *
def pattern8():
    n = int(input())
    mid = -(-n // 2)  
    for j in range(1, mid + 1):
        print("n" * j)
    for j in range(n-mid , 0, -1):
        print("n" * j)

#or
def pattern9():
    n=int(input())
    mid=-(-n//2)
    for j in range(mid):
        for k in range(j+1):
            print("n",end="")
        print()
    for j in range(n - mid):
        for k in range(j, n-mid ):
            print("n",end="")
        print()    

# pattern9()
#c++ code
# #include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j < i + 1; j++) {
#             cout << "*";
#         }
#         cout << endl;
#     }
#     for (int i = 0; i < n - 1; i++)
#     {
#         for (int j = 0; j < n - i - 1; j++)
#         {
#             cout << "*";
#         }
#         cout << endl;
#     }
#     return 0;
# }

#pattern 10
# 1
# 01
# 101
# 0101
# 10101
#c++code
#include <iostream>
# using namespace std;
# int main() {
#     int n;
#     cin>> n ;
#     for (int i =0;i<n;i++){
#         for (int j=0;j<=i;j++){
#             cout << ((i+j)%2==0 ? "1" :"0");
#         }
#         cout<<endl;
#     }

#     return 0;
# }

def pattern10():
    n=int(input())
    start=1
    for i in range (n):
        if i%2==0:
            start =1
        else:
            start=0
        for _ in range(i+1):
            print(start,end="")
            start=1-start
        print()
# pattern10()

#pattern 11
#   *
#  ***
# *****
#  ***
#   *
def pattern11():
    pattern7()
    pattern8()
# pattern11()



#pattern 12
#1      1
#12    21
#123  321
#12344321
def pattern12():
    n=int(input())
    for i in range (n):
        for j in range(1,i+2):
            print(j,end="")
        print("-"*2*(n-i-1),end="")
        for j in range(i+1,0,-1):
            print(j,end="")
        
        print()
# pattern12()
#c++ code
# #include <iostream>
# using namespace std;
# void pattern12() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = 1; j <= i + 1; j++) {
#             cout << j;
#         }
#         cout << string(2 * (n - i - 1), ' ');
#         for (int j = i + 1; j > 0; j--) {
#             cout << j;
#         }
#         cout << endl;
#    }  }


#pattern 13
# 1
# 2 3
# 4 5 6
def pattern13():
    n=int(input())
    a=1
    for i in range (n):
        for j in range(1,i+2):
            print(a,end=" ")
            a+=1
        
        print()
# pattern13()
#c++ code
# #include <iostream>
# using namespace std;
# void pattern13() {
#     int n;
#     cin >> n;
#     int a = 1;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j <= i; j++) {
#             cout << a << " ";
#             a++;
#         }
#         cout << endl;
#     }}


#pattern 14
# A
# AB
# ABC
def pattern14():
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+j),end="")
        print()
# pattern14()

#pattern 15
# ABCD
# ABC
# AB
# A
def pattern15():
    n=int(input())
    for i in range(n):
        for j in range(n-i):
            print(chr(ord('A')+j),end="")
        print()
# pattern15()

#pattern 16
# A
# BB
# CCC
def pattern16():
    n=int(input())
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+i),end="")
        print()
# pattern16()
#c++
#void pattern16() {
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j <= i; j++) {
#             cout << char('A' + i);}
#         cout << endl;}}


#pattern 17
#   A
#  ABA
# ABCBA
def pattern17():
    n=int(input())
    
    for i in range(n):
        for j in range(n-i-1):
            print("-",end="")
        a=ord("A")
        b=chr(a)
        
        for j in range(2*i+1):
            if j<i:
                print(b,end="")
                b=chr(ord(b)+1)
                
            else:
                print(b,end="")
                b=chr(ord(b)-1)
        for j in range(n-i-1):
            print("-",end="")
        print()
# pattern17()
# void pattern17() {
#     int n;
#     cin >> n;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j < n - i - 1; j++) {
#             cout << "-";}
#         char b = 'A';
#         for (int j = 0; j < 2 * i + 1; j++) {
#             if (j < i) {
#                 cout << b;
#                 b++;} 
#             else {
#                 cout << b;
#                 b--;}}
#         for (int j = 0; j < n - i - 1; j++) {
#             cout << "-";}
#         cout << endl;}} 


#pattern 18
#E
#DE
#CDE
#BCDE
#ABCDE
def pattern18():
    n=int(input())
    for i in range(n):
        a=ord("A")+n-i-1
        for j in range(i+1):
            print(chr(a),end="")
            a+=1
        print()
# pattern18()
# void pattern18() {
    # for (int i = 0; i < n; i++) {
    #     char a = 'A' + n - i - 1;
    #     for (int j = 0; j < i + 1; j++) {
    #         cout << a;
    #         a++;}

#pattern 19
