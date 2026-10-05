data=[4,5,6,10,11,12,13,2]
target=9
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]+data[j]==target:
            print(data[i],data[j])
