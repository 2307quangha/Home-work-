b1 

a,b=map(float,input("Nhập 2 cạnh vủa hình chữ nhật : ").split())
print("p=",(a+b)*2)
print("S=",(a*b))

b2

a=float(input("Nhập r :"))
print("s=",3.14*a**2)
print("p=",2*3.14*a)

b3

a,b,c=map(float,input("Nhập ba số a,b,c").split("/"))
nn=min(a,b,c)
if a+b>c and b+c>a and c+a>b :
    if a==b and b==c :
        print("Tam giac deu")
    elif a==b or b==c or a==c :
        print("Tam giac can")
    else :
        print("Tam giac thuong")
else :
    print("Khong phai tam giac") 

b4 

a,b=map(float,input("Nhập lần lượt 2 số a,b của pt ax+b=0 :").split())
print("x=",(-b)/a)

b5 

a,b,c=map(float,input("Nhập lần lượt 3 số a,b,c của pt ax^2+bx+c=0 :").split())
d= b**2-4*a*c
if d <0 :
    print("pt vô nghiệm")
elif d==0 :
    print("pt có nghiệm kép x=",(-b)/(2*a))
else :
    print("pt có 2 nghiệm phân biệt x1=",(-b-d**0.5)/(2*a),"x2=",(-b+d**0.5)/(2*a))    

b6 

a,b,c,d = map(float,input("Nhập lần lượt 4 số a,b,c,d" ).split())
print("Max=",max(a,b,c,d))

b7

a,b,c,d = map(float,input("Nhập lần lượt 4 số a,b,c,d" ).split())
print("Max=",min(a,b,c,d))

b8

b9 

a=int(input("Nhập số giây "))
h=a/3600
m=a/60
print(f"{h}:{m}:{a}")

b10 

a,b=map(float,input("Nhập lần lượt tọa độ x,y tâm đường tròn ").split())
c=float(input("R="))
e,f=map(float,input("Nhập tọa độ x,y của điểm A").split())
d=(a-e)**2 + (b-f)**2 
if d==c:
    print("điểm a thuộc đường tròn ") 
else :
    print("điêm A không thuộc đường tròn ")

b11 

a,b=map(float,input("Nhập X , y ").split())
print(a**b)


                          


