import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import argparse

# Load dataset
def load_data(file_path):
    movies = pd.read_csv(file_path)
    movies = movies[['Movie Names', 'Rating', 'Year', 'Genere', 'Description']].dropna()
    movies = movies.drop_duplicates(subset=['Movie Names'])
    movies['Genere'] = movies['Genere'].str.replace(',Back to top', '', regex=False)
    movies['combined_features'] = (
        movies['Genere'] + ' ' + movies['Year'].astype(str) + ' ' + 
        movies['Rating'].astype(str) + ' ' + movies['Description']
    ).str.lower()
    return movies

# Compute TF-IDF matrix
def compute_tfidf_matrix(movies):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(movies['combined_features'])
    return vectorizer, tfidf_matrix

# Recommend movies
def recommend_movies(query, movies_df, tfidf_matrix, vectorizer, top_n=5):
    query_vector = vectorizer.transform([query.lower()])
    cosine_sim = cosine_similarity(query_vector, tfidf_matrix).flatten()
    if not cosine_sim.any():
        print("No relevant movies found. Try refining your query.")
        return
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    recommendations = movies_df.iloc[top_indices].copy()
    recommendations['similarity_score'] = cosine_sim[top_indices]
    print("\nTop Movie Recommendations:")
    print(recommendations[['Movie Names', 'Genere', 'Year', 'Rating', 'Description', 'similarity_score']])

# Main execution function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Enter your movie preference")
    parser.add_argument("--file", type=str, default="Dataset/Indian_movies.csv", help="Path to movie dataset")
    args = parser.parse_args()
    
    movies = load_data(args.file)
    vectorizer, tfidf_matrix = compute_tfidf_matrix(movies)
    recommend_movies(args.query, movies, tfidf_matrix, vectorizer)

if __name__ == "__main__":
    main()
