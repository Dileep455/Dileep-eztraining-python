#Day 3
#contant
#list 
l=[12,445,34.34,'rose']
print(type(l))
print(l[3])
print(l[:2])
print(l[-1:])
print(l[:-1])

#append():-add an element in the list                                    ex:-l.append()
#extend():-add an group of values of list to another list               ex:-l.extend()
#insert():-insert an element                                             ex:-l.insert()
#remove()                                                                   l.remove()
#pop()                                                                       l.pop()
#clear()                                                                      l.clear()
#index()                                                                     l.index()
#count():-count the int                                                        l.count()
#sort():-keep the number in ascendind order                                   l.sort()
#reverse():-reverse the list                                                  l.reverse()
#copy()

#l=[1,2,1,3,2,15,'flag']
#l.append("hosted")
#print(l)
#l.extend([12])
#print(l)
#l.insert(2,'frog')
#print(l)
#l.remove(1)
#print(l)
#l.pop(2)
#print(l)
#l.clear()
#print(l)

#create a listof 10 element print element of one by one
#method 1
#l=[1,2,3,4,5,6,7,8,9,10]
#for i in range(len(l)):
#    print(l[i])

#method 2
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(i)

#create a list 5 float numbers find out than find the sum and average of element
# l=[12.2,23.2,22.3,34.3,23.32]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)    
# average=0
# for j in l:
#     average=(sum+i)/len(l)
# print(average)  



#after creating  list 6 element extract only even numbers 
# size=int(input("size:"))
# l=[]
# for i in range(size):
#     ele=int(input("element:"))
#     l.append(ele)
# print(l)
# for j in l:
#     if(j%2==0):
#         print(j)    


# get list numbers as input ,return their product if the product than 750 else ruturn the sum

# n=list(map(int,input("enter").split()))
# print(n)
# x=1
# y=0
# for i in n:
#     x=x*i
#     y=y+i
# if x<=750:
#     print("prod",x)
# else:
#     print("sum",y)
         
#list comprasion
# number=[elements for elements in "great people"]
# print(number)

# n=[2,3,6,8,6,]
# sum=0
# l=[ele for ele in n]
# for i in l:
#     sum=i+sum
#     if(sum<10):
#         print(l)
# print(sum)

#set
# s.add(element)
# s.update([20,24])
# s.discard(element)
# s.remove(element)
# s1={1,2,3}
# S2={4,5,6,1,2}
# S1|S2  Union  than  s1.union(s2)    ans={1,2,3,4,5,6}
# s1&s2  intersect   than  s1.intersection(s2)    ans={1,2}
# s1-s2
# s1^s2 (or) print(s1.symmtric _differce(s2))



# s={2,4,6,9}
# s.add(10)
# print(s)
# s.update([354,34,4,3])
# print(s)
# s.discard(4)
# print(s)

#........tuple()
# tuple   cannot do change in list
# t=(3,4,6,5.6,"ice",6)
# print(t.count(6))
# print(t)

# d={1:"dileep",2:"kumar"}
# # print(d.keys())
# # print(d)
# # print(d.values())
# # print(d)
# print(d.items())
# print(d)

