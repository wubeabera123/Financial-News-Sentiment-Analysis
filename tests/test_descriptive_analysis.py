# file: test_news_data_analysis.py

import unittest
import pandas as pd
from scripts.descriptive_analysis import NewsDataAnalysis

class TestNewsDataAnalysis(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Assuming the data is already loaded
        cls.df = pd.DataFrame({
            'date': pd.to_datetime(['2024-08-01 10:00:00', '2024-08-01 11:00:00', 
                                    '2024-08-02 09:00:00', '2024-08-03 12:00:00', 
                                    '2024-08-03 13:00:00']),
            'headline': ['First headline', 'Second headline', 'Third headline', 
                         'Fourth headline', 'Fifth headline'],
            'publisher': ['Publisher A', 'Publisher B', 'Publisher A', 
                          'Publisher C', 'Publisher B']
        })
        cls.analysis = NewsDataAnalysis(cls.df)
    
    def test_headline_length_statistics(self):
        stats = self.analysis.headline_length_statistics()
        self.assertEqual(stats['count'], 5)
        self.assertTrue('mean' in stats)
        self.assertTrue('std' in stats)
        self.assertTrue('min' in stats)
        self.assertTrue('max' in stats)
    
    def test_articles_per_publisher(self):
        counts = self.analysis.articles_per_publisher()
        self.assertEqual(counts['Publisher A'], 2)
        self.assertEqual(counts['Publisher B'], 2)
        self.assertEqual(counts['Publisher C'], 1)
    
    def test_articles_per_day(self):
        counts = self.analysis.articles_per_day()
        self.assertEqual(counts['2024-08-01'], 2)
        self.assertEqual(counts['2024-08-02'], 1)
        self.assertEqual(counts['2024-08-03'], 2)
    
    def test_plot_articles_over_time(self):
        # This test checks if plotting does not raise an error.
        try:
            self.analysis.plot_articles_over_time()
        except Exception as e:
            self.fail(f"Plotting failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
