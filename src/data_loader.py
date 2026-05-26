import pandas as pd

def load_data():

    data = pd.read_csv(
        "data/movies.csv"
    )

    return data


df = load_data()

print(df.head())
print(df.info())