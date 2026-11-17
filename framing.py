import pandas as pd
d=pd.DataFrame({'Name':['Salman','Aishswarya','Shahid','Kareena'],
                'Height':[1.63,1.63,1.71,1.65],
                'Weight':[78,55,72,53]})
print(d)
d[d['Height']==max(d['Height'])]['Name']
e=lambda x:x**2
x=d['Height'].map(e)
y=d['Weight']
d['BMI']=y/x
print(d)