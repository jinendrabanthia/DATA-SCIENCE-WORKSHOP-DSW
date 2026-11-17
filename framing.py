
import pandas as pd

d = pd.DataFrame({
    'Name': ['Salman', 'Aishswarya', 'Shahid', 'Kareena'],
    'Height': [1.63, 1.63, 1.71, 1.65],
    'Weight': [78, 55, 72, 53]
})

print("Original DataFrame:")
print(d)

print("\nPerson with maximum height:")
print(d[d['Height'] == d['Height'].max()]['Name'])

e = lambda x: x**2

x = d['Height'].map(e)

y = d['Weight']

d['BMI'] = y / x

print("\nFinal DataFrame with BMI:")
print(d)
