#shallow copy require nested lists
#copy.copy reates 2 completely different objects 
import copy
x=[10,20,[30,40]]
y= copy.copy(x)
x[2]=999
print(x)
print(y)
print(id(x))
print(id(y))
#shallow copy means creating new object, but not copying the inner nested 
#object.