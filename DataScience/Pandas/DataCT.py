import pandas as pd
data = range(10, 60, 10)
df =pd.DataFrame(data)
#print(df.groupby(0).sum())
#print(df.replace(10, 100))
#print(df.astype(float))
#print(df.round(2))
print(df.eval('0+ 1'))
