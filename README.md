# 📺 Netflix Data Analysis
![Python](https://img.shields.io/badge/python-3.13-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A data-driven exploration of Netflix's global content catalog to uncover trends, content strategy, and viewing preferences using Python.

## Repository Structure

```
netflix-data-analysis/
├── data/                  # Raw dataset (netflix_titles.csv)
├── visuals/               # All generated charts (.png)
├── notebook/              # Analysis script (analysis.py)
└── README.md              # Project documentation (this file)
```

## Project Overview

This project analyzes the Netflix dataset to extract meaningful insights about its content library over time. It includes data cleaning, transformation, exploratory analysis, and visualization. The project is designed to demonstrate practical data analysis skills using a real-world entertainment dataset.

## Dataset Description

- **Source:** [Kaggle - Netflix Titles Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Total Records:** ~8,800 titles
- **Features:** Title, Type (Movie/TV Show), Country, Date Added, Duration, Genre, Cast, Rating, etc.

## Project Objectives

- Understand the distribution between Movies and TV Shows.
- Identify countries contributing most to Netflix’s content library.
- Explore how content additions have evolved over the years.
- Discover the most popular genres globally.
- Analyze movie durations and identify consumption patterns.
- Compare yearly trends of Movies vs TV Shows.

## Tools & Libraries Used

- Python 3
- Pandas – Data manipulation
- Matplotlib – Data visualization
- Counter – Frequency analysis
- VS Code – Development environment

## Data Cleaning & Processing

Key cleaning steps included:

- Dropped rows with missing `date_added`.
- Filled missing `country` with `"Unknown"` and `rating` with `"Not Rated"`.
- Converted `date_added` to datetime and extracted `year_added`.
- Parsed `duration` field to separate numeric duration for movies and seasons for TV Shows.
- Cleaned `listed_in` column to analyze genres.

## Key Insights

1. **Movies Dominate Netflix's Library**

Netflix hosts **6,131 Movies** compared to **2,666 TV Shows**, showing a strategic preference for feature-length content appealing to global audiences.

2. **Top Content-Producing Countries**
- The **USA** leads by a large margin, followed by **India** and **the UK**.
- A significant number of entries have missing country data, reflecting the importance of thorough data collection.

3. **Content Growth Over the Years**
- Netflix steadily expanded content from 2014 onwards.
- A peak was reached in **2019** with **1,999 titles** added.
- **2020** remained strong (1,878 titles) despite the pandemic.
- **2021** saw a slight drop (1,498 titles), likely due to COVID-related production delays.

4. **Most Popular Genres**

Top genres by frequency:
- International Movies – 2,752
- Dramas – 2,427
- Comedies – 1,674

This suggests Netflix's focus on global, emotionally engaging, and accessible content.

5. **Movie Duration Distribution**
- **Average movie runtime:** ~99.6 minutes
- **Most common range:** 87–114 minutes
- **Shortest movie:** 3 minutes
- **Longest movie:** 312 minutes

This shows a strong focus on feature-length movies optimized for single-sitting viewing.

 6. **Yearly Trends: Movies vs TV Shows**
- Between 2008 and 2012, Netflix added very few titles, mostly movies.
- From 2013 onward, the number of TV Shows steadily increased alongside movies.
- The platform experienced rapid growth between 2018 and 2020:
  - **2019:** 1,424 movies and 575 shows
  - **2020:** 1,284 movies and 594 shows
- In **2021**, there was a slight drop in new content, likely due to pandemic-related production delays.

Netflix scaled rapidly to compete globally by increasing original content.

## Visualizations
Visualizations are saved as `.png` files in the `visuals/` folder.

## Conclusion
Between 2016 and 2020, Netflix dramatically expanded its library, peaking at nearly 2,000 new titles in 2019. 
The platform’s global strategy is evident in its mix of feature-length dramas and comedies from top markets such as the U.S., India, and the U.K.  

## Contact
**Elizabeth Ayeku**  
Email: temiloluwaayeku@gmail.com
 GitHub: https://github.com/thepludenhystrophile
