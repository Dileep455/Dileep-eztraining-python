# d={n:n*n for n in range(1,5)}
# print(d)

# #product price fo 5 units
# old={"onion":60,"tomato":120,"apple":300}
# new={product:price*5 for (product,price) in old.items()}
# print(new)


# #with checks
# real={"pavan":60,"ravi":180,"sathish":60}
# now={name:age for(name,age) in real.items() if age<=60 }
# print(now)


# crate a list with 8 custmers names display a dict. which has along with discount for them from particular shop
# import random
# cust=["sam","srinu","akhil","nikhil","ram","pavan","ravi","sathish"]
# cust_dict={names:random.randint(1,100) for names in cust}
# print(cust_dict)


# n1=['a','b','c']
# n2=[1,2,3]
# d={a:b for (a,b) in zip(n1,n2)}
# print(d)



#creat a list of student and their marks display the name and percentage
# name=['ram','dileep','ravi','pavan','satish']
# marks=[560,565,564,574,466]
# dict_percentage={names:marks for (names, marks) in zip(name,marks) }
# print(dict_percentage)      

# method2
# import random
# student_names=list(map(str,input("enter names").split()))
# marks=[]
# for i in range(len(student_names)):
#     a=(random.randint(300,500)/500)*100
#     marks.append(a)
# my_dict={x:y for (x,y) in zip(student_names,marks)}
# print(my_dict)
   

#strings
# n="hi i'am "dileep"//invalid syntax
# print(n)

# n="hi i'am"
# print(n)//vaild syntax

# nm='hi i'am'
# print(nm)//invaild syntax

# n='hi i\'am'
# print(n)//vaild syntax


#s.upper()
# s.lower() or s.casefold()
# s.capitalize()
# s.replace('h','a')
# s.strip()
# s.split()s.split(',')s.split('.')s.split('a')
# s.center(31,'*') s.center(width,fillchar)
# s.count()
# s.count('a',5,len(s))
# s.endswith('a',o,len(s))
# s.find('a',o,len(s))
# a.index('a',7,len(s))
#s.islower()/s.isupper()/s.istitle()
# caps/max(s)
# min(s)
# s.starswith('hello',o,len(s))
# s.rfind('a',o,len(s))


# s="     dileep,kumar"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.replace('d','b'))
# print(s.strip())
# print(s.split())
# print(s.split(','))
# print(s.split('e'))
# print(s.center(40,'e'))




# mutable vs immutable 
# mutable-can be changed after creation  (list,set,dictionary) 
# immutable- cannot change after creation  (int,float,str,bool,tuple)



#get on string as input along with no.find out and display weather it is present in string or no
# string=input("enter your string:")
# i=input ('enter the data:')
# if i in string:
#     print("present")
# else:
#     print("not present")


#check weather the string is palandron or not



#after get a string as input check your string as space or not  it if true print no. of spaces in string






#crate a list with vowels get one string as a input count vowels in string




#math  module
import math 
print("cell 12.5:",math.ceil(12.5))
print("floor 12.5:",math.floor(12.5))
print("sqrt 345:",math.sqrt(345))
print("factorial 3:",math.factorial(3))
print("power 2,3:",math.pow(2,3))
print("remainder 10,3:",math.fmod(10,3))
a,b=divmod(10,3)
print(a,b) 










