# file: news_data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

class NewsDataAnalysis:
    def __init__(self, data):
        """
        Initialize the class with a DataFrame.
        
        Parameters:
        data (pd.DataFrame): The raw data containing news articles.
        """
        self.data = data
        
        # Ensure 'headline_length' column is created
        if 'headline_length' not in self.data.columns:
            self.data['headline_length'] = self.data['headline'].apply(len)

        # Convert 'date' column to datetime if not already done
        self.data['date'] = pd.to_datetime(self.data['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

    def headline_length_statistics(self):
        """
        Compute and return descriptive statistics for headline lengths.
        
        Returns:
        pd.Series: Descriptive statistics for headline lengths.
        """
        headline_stats = self.data['headline_length'].describe()
        return headline_stats

    def articles_per_publisher(self):
        """
        Count and return the number of articles per publisher.
        
        Returns:
        pd.Series: Count of articles per publisher.
        """
        publisher_counts = self.data['publisher'].value_counts()
        return publisher_counts

    def articles_per_day(self):
        """
        Count and return the number of articles published per day.
        
        Returns:
        pd.Series: Number of articles published per day.
        """
        articles_per_day = self.data['date'].value_counts().sort_index()
        return articles_per_day

    def plot_articles_over_time(self):
        """
        Plot the number of articles published over time.
        """
        articles_per_day = self.articles_per_day()
        plt.figure(figsize=(10, 6))
        articles_per_day.plot(kind='line', marker='o')
        plt.title("Number of Articles Published Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
