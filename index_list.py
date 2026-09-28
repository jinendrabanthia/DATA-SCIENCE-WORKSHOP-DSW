l=[10,20,30,40,10,20,30,10,10]
target=int(input("enter value to search"))
if target in l:
    print(l.index(target))
else:
    print("value not found")

    
