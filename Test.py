a = ("Hello World")
print(a)

#Tuple Data Type:
#Tuple is a immutable data type.
#We cannot modify data in tuple.
#To denote tuple data we use round brackets.
#Example:
tup = (10,20,30,"Python","Apple","Banana")
print(tup)
print(len(tup))
print(type(tup))
print(tup[0])
print(tup[2:4])
print(tup.count(10))
print(tup.index(10))

for i in tup:
    print(i)