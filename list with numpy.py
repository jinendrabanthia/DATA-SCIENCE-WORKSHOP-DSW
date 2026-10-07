import numpy as np

Name = np.array(['Satyanistha', 'Nisith', 'Chandran', 'Swayam', 'Nisith'])
Roll = np.array([100, 13, 39, 41, 43])
Marks = np.array([95, 97, 96, 91, 94])

result = Marks[(Name == 'Nisith') & (Roll == 13)]

print("Marks secured by Nisith:", result[0])