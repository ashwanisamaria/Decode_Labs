import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("raw_skills.csv")

# User input
user_input = input("Enter your skills: ")

# Combine data
all_skills = data["Skills"].tolist()
all_skills.append(user_input)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_skills)

# Similarity calculation
similarity = cosine_similarity(
    tfidf_matrix[-1], tfidf_matrix[:-1]
)

# Get top 3 recommendations
scores = similarity.flatten()
top_indices = scores.argsort()[::-1][:3]

# Show results
print("\nTop Recommended Career Roles:")

for i in top_indices:
    print(data.iloc[i]["Role"])
