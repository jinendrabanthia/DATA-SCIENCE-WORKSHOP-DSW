import copy
#deep copy
x=[10,20,30,40]
y=copy.deepcopy(x)
x[2]=999
print(x)
print(y)
print(id(x))
print(id(y))