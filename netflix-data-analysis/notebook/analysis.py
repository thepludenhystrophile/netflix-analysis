# Netflix Data Analysis Project
# Author: Ayeku Elizabeth
# Description: Exploratory Data Analysis

import pandas as pd

# Load and Preview Dataset
df = pd.read_csv("netflix_titles.csv")

print("Preview of dataset")
print(df.head())

print("\nColumns in the dataset:")
print(df.columns.tolist())

print("\Dataset information:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

#Data Cleaning

#Fill missing values
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

#Drop rows with missing 'date_added'
df = df.dropna(subset=['date_added'])
print("\nMissing data cleaned")

import matplotlib.pyplot as plt

#Content Type Distribution
type_counts = df['type'].value_counts()

#Plot
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['red', 'skyblue'])
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Type')
plt.ylabel('Number of Titles')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\nNumber of Movies and TV Shows:")
print(type_counts)

#Top Countries with most Titles
top_countries = df['country'].value_counts().head(10)

#Plot
plt.figure(figsize=(8,5))
top_countries.plot(kind='bar', color='darkcyan')
plt.title('Top 10 countries with Most Netflix Content')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Yearly Trend of Content Added
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
yearly_counts = df['year_added'].value_counts().sort_index()

#Plot 
plt.figure(figsize=(10,5))
plt.plot(yearly_counts.index, yearly_counts.values, marker='o', color='green')
plt.title('Netflix Content Added by Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nNumber of Netflix titles added each year:")
print(yearly_counts)

#Top Genres
from collections import Counter

#Create a flat list of all genres
all_genres = []
for genres in df['listed_in']:
    split_genres = [genre.strip() for genre in genres.split(',')]
    all_genres.extend(split_genres)

#Count the frequency of each genre
genre_counts = Counter(all_genres)
top_10_genres = genre_counts.most_common(10)

#Plot
genres, counts = zip(*top_10_genres)
plt.figure(figsize=(10,6))
plt.bar(genres,counts, color='coral')
plt.title('Top 10 Most Common Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nTop 10 genres on Netflix:")
for i, (genre, count) in enumerate(top_10_genres, start=1):
    print(f"{i}. {genre}: {counts}")

#Movie Duration Analysis
movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration_clean'] = movies_df['duration'].str.extract('(\d+)').astype(float)
                                                                
#Plot
plt.figure(figsize=(10,5))
plt.hist(movies_df['duration_clean'], bins=30, color='mediumslateblue', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.show()

print("\nMovie Duration Stats:")
print(movies_df['duration_clean'].describe())

#Movies vs TV Shows Added per Year
count_by_year_type = df.groupby(['year_added', 'type'])['show_id'].count().unstack(fill_value=0)

#Plot
plt.figure(figsize=(12,6))
count_by_year_type.plot(kind='bar', stacked=True, legend=True, ax=plt.gca())
plt.title('Movies vs TV Shows Added per Year')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()                              

print("\nMovies vs TV Shows per Year:")
print(count_by_year_type)