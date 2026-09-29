#frozen set is immutable
s={10,20,30,40}
fs=frozenset(s)
print(fs)
print(type(fs))

#frozen set can be used as keys in dictionary
#frozen set cannot be used as values in dictionary
#frozen set can be used as elements in set
#frozen set cannot be used as elements in list
#frozen set can be used as elements in tuple
