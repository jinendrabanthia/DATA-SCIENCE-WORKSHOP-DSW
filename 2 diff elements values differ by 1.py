data=[8,3,12,20,7,15]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if abs(data[i]-data[j]==1):
            print(data[i],data[j])
            found=True
            break
        