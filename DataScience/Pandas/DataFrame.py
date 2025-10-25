import pandas as pd

data = {'Name': ['Uday', 'Anshul', 'Kanak'], 'Age': [25, 30, 35], 'City': ['Indore', 'Dewas', 'Bhopal']}
df =pd.DataFrame(data)
print(df)
print(df['Name'])
print(df.iloc[1])
print(df[df['Age'] > 28])
