x=[10,20,30,40]
y=x.copy()
x[2]=999
print(x)
print(y)
print(id(x))
print(id(y))