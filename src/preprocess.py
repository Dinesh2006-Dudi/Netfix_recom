import pandas as pd


df = pd.read_csv(
    "data/movies.csv"
)

df = df.drop_duplicates()

df = df.fillna(0)

print(df.head())
print(df.info())