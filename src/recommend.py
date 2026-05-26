import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


df = pd.read_csv(
    "data/movie_metadata.csv"
)


vectorizer = (
    TfidfVectorizer()
)

vectors = vectorizer.fit_transform(
    df["genre"]
)

similarity = cosine_similarity(
    vectors
)


def recommend(movie):

    movie = movie.lower()

    movies = (
        df["movie"]
        .str.lower()
        .tolist()
    )

    if movie not in movies:

        return [
            "Popular Action",
            "Popular Drama",
            "Popular Sci-Fi"
        ]

    idx = movies.index(movie)

    scores = (
        similarity[idx]
    )

    indices = (
        scores.argsort()[-6:-1]
    )

    rec = (
        df.iloc[
            indices
        ]["movie"]
        .tolist()
    )

    return rec[::-1]