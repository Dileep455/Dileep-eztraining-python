import random as r 
x=" i love sweets"

print (r. sample (x,2))

#everytime it gives different output 
a=[1,2,3,4,5,6]
r.shuffle(a)
print (a)
a={1,2,3,4,5,6}
print (r. choice (a))
b= "welcome back"
print (r. choice (b))
a=r.random()
print(a)





#to find out all the functions in a module 
z=dir(r)
print(z)

#display whole year calendar

import calendar
print("full calendar")
print(calendar.calendar(2022))
print("particular month")
print(calendar.month(2022,4))
print("set first day of the week")
calendar.setfirstweekday(calendar.MONDAY)
print(calendar.month(2022,12))


#date time moudle
import datetime
a=datetime.datetime.now()
print(a)
sv=a. strftime("%Y")  #upper case
sv=a.strftime("y")   #lower case
print("year short version")
print("year full version")


#functions
#classfcation
#for code reuseabailty inmuitlable we can write it once include that and can call the function
#types 
#1)functions with arrugment
# 2) 
 


def sample():
    print("collage days")
    print("real days")
sample()
print("today")
sample()
print("present days")
sample()
print("class room")

#without arugument,without return value
def multi():
    n1=int(input("number"))
    n2=int(input("number"))
    n3=int(input("number"))
    prod=n1*n2*n3
    print(prod)

multi()


#without arugument,with return value
def multi():
    n1=int(input("number"))
    n2=int(input("number"))
    n3=int(input("number"))
    prod=n1*n2*n3
    return prod
res=multi
print(res)

#with arugunment,without return value
# #static input


#with arugunment,with return value
# #static input
def multi(n1,n2,n3):
    prod=n1*n2*n3
    return prod
res=multi(3,4,5)
print(res)
# #user input
def multi(a,b,c):
    prod=a*b*c
    return(prod)
n1=int(input("enter 1:"))
n2=int(input("enter 2:"))
n3=int(input("enter 3:"))
res=multi(n1,n2,n3)
print(res)






def multi_table(n):
   for i in range (1,11): 
    print(i,"x",n,"=",i*n)
n=int(input("which table?:"))
multi_table


#factors of a given number( without arugument,with return value)
def factor(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i)
n=int(input("number?:"))
factor




# find out sum of digits of given in a number
# sum of digits of given number
# function with argument with return
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return(sum)
n=int(input("enter the number"))
res=digits
print(res)

#recusion method
# a fuction which calls itself is called recursive function 
# this concept is called "recusion"
def display():
    n=int(input("enter the number"))
    if n==2:
        display()
    else:
        print("over")
display()    


#recursive function
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1) 
result=fact(4)
print(result)


n=int(input("enter number:"))
a=0
b=1
sum=0
count=1

while(count<=n):
    print(sum,end="")
    count=+1
    a=b
    b=sum
    sum=a+b