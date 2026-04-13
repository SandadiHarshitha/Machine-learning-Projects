# 🎬 Movie Recommendation System

## 📌 Overview

This project is a simple Movie & TV Show Recommendation System. It suggests similar movies or shows based on the title entered by the user. The system uses content-based filtering by comparing features like director, cast, genre, and description.

## ⚙️ How It Works

The dataset (netflix_titles.csv) is first cleaned by filling missing values. Important features such as director, cast, listed_in (genre), and description are selected and processed. These features are combined into a single text called a "soup".

This text is then converted into numbers using TF-IDF (Term Frequency–Inverse Document Frequency). After that, cosine similarity is used to measure how similar each movie is to others.

When a user enters a movie name, the system finds and returns the top 10 most similar movies.

## 🧠 Techniques Used

* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Filtering

## ▶️ How to Use

1. Install required libraries: pandas, numpy, scikit-learn
2. Run the notebook
3. Call the function:
   get_enhanced_recommendations("Movie Name")

## 📊 Example

Input: Blood & Water
Output: List of similar shows like The Gift, Jinn, Into the Night, etc.

## 🛠️ Tools

Python, Pandas, NumPy, Scikit-learn

## ⚠️ Limitations

* Works only with available dataset
* No user personalization

## ✅ Conclusion

This project demonstrates how machine learning can be used to recommend movies based on content similarity in a simple and effective way.

