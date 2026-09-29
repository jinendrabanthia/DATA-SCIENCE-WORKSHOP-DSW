# to represent a group of values into a single entity where insertion order is preserved 
# duplicate values are allowed 
# heterogenous elements are allowed 
# elements are indexed using forward and backward indexing 
# tuple is immutable 
# tuple is not growable
# tuple is represented using parenthesis ()

t=(10,20,30,40)
print(t)
print(type(t))

k=(10,20,'jinendra',[10,20,30])
print(k)
print(type(k))

t=t*2
print(t)
#in tuple parenthesis is not mandatory
tup1=10,20,30
print(tup1)
print(type(tup1))

#syntax
t=tuple('iterable object')
print(t)
print(type(t))
#tuple cannot be empty

o=tuple(range(0,11,2))
print(o)
print(type(o))

