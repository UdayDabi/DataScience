import pandas as pd

a = pd.Series(['Java', 'C', 'C++', 'Python'])
print(a)

#Add
# Naya element add karte hain index 4 pe
a[4] = 'JavaScript'
print(a)

#Update
# Index 2 pe element update karte hain
a[2] = 'Ruby'
print(a)


#delete
# Index 1 pe element delete karte hain
a = a.drop(1)
print(a)

#Get
# Index 3 ka element get karte hain
print(a.iloc[3])