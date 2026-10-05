data=[4,2,4,3,2,3,3,2,5,3,3]
fre={}
for x in data:
    if x in fre:
        fre[x]=fre[x]+1
    else:
        fre[x]=1
print(fre)
s_f=sorted(fre.items(),key=lambda x:x[1],reverse=True)
print("second most frequent elemnet is : ",s_f[1][0])