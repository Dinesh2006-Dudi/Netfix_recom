import pandas as pd
import joblib

from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv(
    "data/movies.csv"
)

pivot = df.pivot_table(
    index="user_id",
    columns="movie",
    values="rating"
)

pivot = pivot.fillna(0)

similarity = cosine_similarity(
    pivot
)

joblib.dump(
    similarity,
    "models/recommendation.pkl"
)

print(
"Model Saved"
)