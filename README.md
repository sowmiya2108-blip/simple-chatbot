# simple-chatbot
**Overview**:
This is a basic recommendation system that suggests movies to users based on their preferences. It uses content-based filtering to recommend similar movies by analyzing genres or descriptive features of each movie. The system calculates similarities between items using vectorized features and returns the most relevant suggestions.
**Features**:
*Recommends movies based on user-selected input.

*Uses genre-based similarity to find similar movies.

*Implements content-based filtering using TF-IDF and cosine similarity.

*Lightweight and beginner-friendly codebase.

*Can be easily extended for books, products, or songs.
Workflow:
1. User selects a movie
2. Extract genre and text features from all movies
3. Convert genres to vectors using TF-IDF
4. Calculate cosine similarity between selected and other movies
5. Recommend top similar movies to the user
**Installation**:
Install required Python packages:
pip install pandas scikit-learn
