import pandas as pd
df = pd.read_csv("./gapminder.tsv",sep="\t")
#print(df)
#print(df.shape)
#print(type(df))
#print(df.columns)
#print(df.dtypes)
#print(df.info())
print(df.head())