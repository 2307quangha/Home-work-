# bài 1
for i in range(1,100):
    print(i)
# bài 2
for i in range(1,100):
    if i%3==0 :
        print(i) 
# bài 3
a=int(input())
for i in range(1,11) :
    print(f"{a} x {i} = {a*i} ")
# bài 4


# bài 5

n=int(input())
a=0
for i in range (1,n+1):
    a+=i
print(i)
    
# bài 6

a=int(input())
for i in (1,a):
    if a%i==0 :
        print(i) 

# bài 7

a=int(input())
b=0
for i in (1,a):
    if a%i==0 :
        b+=1 
print(b)
        

# bài 8

a,b=map(int,input().split())
for i in range (1,a) :
    if a%i==0 and b%i==0 :
        print(i)
# bài 9

a=int(input())
b=a**(1/2)
if int(str(b).split(".")[1])==0 :
    print("Yes")
else :
    print("No")

    
# bài 10

a=int(input())
b=0 
for i in range(1,a) :
    if a%i==0 :
        b+=i 
if a==b :
    print("Yes")
else :
    print("No")
    
# bài 11

a=int(input("a="))
while a<0 :
    a=int(input("Nhập lại a= "))
print("bạn đã nhập đúng quy tắc")
# bài 12

n=int(input())
b=1
while sum(range(1,b+1))<n :
    b+=1
print(b-1)



# bài 13

a=int(input())
ds=[1]
b=1
while sum(ds)<=a :
    ds.append(1/(b+1)) 
    b+=1
    
print(b)


# bài 13 cách 2

a=int(input())
c=1
b=1
while c<=a :
    c+=1/(b+1)
    b+=1
    
print(b)
# bài 14

a=int(input())
max=a
min=a
while a!=-1 :
    a=int(input())
    if a>max :
        max=a
    if min>a :
        min=a    
print(max)
print(min)
# bài 15

n=int(input())
b=0
while n!=0 :
    n=n//10
    b+=1
print(b)    





# bài 16

n=int(input())
b=0 
c=0
while n!=0 :
    if (n%10)%2==0 :
        b+=1
    else :
        c+=1
    n=n//10        
print(b)
print(c)    
# bài 17
n=int(input())
b=0 
while n!=0 :
    b+=(n%10)
    n=n//10
print(b)    
# bài 18
import math 
n=int(input())
b=math.log(n, 3)
if int(str(b).split(".")[1])==0 :
    print("yes")
else :
    print("no")    
# bài 19
n0=1
n1=1
a=int(input())
while n1<a :
    n0=n1
    n1+=n1

print(n0)    
    

# bài 20
n=int(input())
b=0
while n!=0 :
    match n%10 :
        case 2|3|5|7 :
            b+=1
    n=n//10        
print(b)            