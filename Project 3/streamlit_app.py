import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "raw_skills.csv")
data = pd.read_csv(file_path)

# Title
st.title("AI Career Recommendation System")
st.write("Enter your skills and get top career recommendations")

# User input
user_input = st.text_input("Enter your skills (Example: Python SQL Machine Learning)")

if st.button("Recommend"):
    all_skills = data["Skills"].tolist()
    all_skills.append(user_input)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_skills)

    similarity = cosine_similarity(
        tfidf_matrix[-1], tfidf_matrix[:-1]
    )

    scores = similarity.flatten()
    top_indices = scores.argsort()[::-1][:3]

    st.subheader("Top Recommended Roles:")

    for i in top_indices:
        st.write(data.iloc[i]["Role"])