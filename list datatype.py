x=[10,20,30,40]
y=x
x[2]=999
print(x)
print(y)
#only one object creted and both reference variable refer to same object 
#changes in the location will cause changes in both reference variable.
#slicing use krne se dusre wale ko affect nhi krega 
k=[10,20,30,40]
j=k[:]
k[2]=999
print(k)
print(j)
print(id(k))
print(id(j))
