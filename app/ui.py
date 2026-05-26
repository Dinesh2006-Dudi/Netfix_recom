import streamlit as st
import sys

sys.path.append(".")

from src.recommend import recommend


st.title(
"🎬 Movie Recommendation"
)

movie = st.text_input(
"Enter any movie"
)

if st.button(
"Recommend"
):

    if movie:

        movies = recommend(
            movie
        )

        st.success(
            "Recommendations"
        )

        for m in movies:

            st.write(
                "⭐",
                m
            )