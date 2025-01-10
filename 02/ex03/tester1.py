import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
from projection_life import data_collect, convert_income


class TestDataCollect(unittest.TestCase):
    def setUp(self):
        # Prepare valid data for life expectancy and income
        self.valid_life_expectancy_data = pd.DataFrame({
            "country": ["France", "Germany", "USA"],
            "1900": [45, 50, 47]
        })

        self.valid_income_data = pd.DataFrame({
            "country": ["France", "Germany", "USA"],
            "1900": ["1K", "2K", "3K"]
        })

        # Data with errors (missing columns, invalid values)
        self.missing_country_column = pd.DataFrame({
            "1900": [45, 50, 47]
        })

        self.invalid_income_data = pd.DataFrame({
            "country": ["France", "Germany", "USA"],
            "1900": ["1K", "haha", "3K"]
        })

        self.empty_data = pd.DataFrame()

    @patch('projection_life.load')
    def test_valid_data(self, mock_load):
        """
        Test with valid life expectancy and income data
        """
        mock_load.side_effect = [self.valid_life_expectancy_data, self.valid_income_data]

        result = data_collect("life_expectancy_years.csv", 
                              "income_per_person_gdppercapita_ppp_inflation_adjusted.csv", 
                              "1900")
        
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)  # All three rows should match
        self.assertIn("Life Expectancy", result.columns)
        self.assertIn("Income", result.columns)

    @patch('projection_life.load')
    def test_missing_country_column(self, mock_load):
        """
        Test when one file is missing the 'country' column
        """
        mock_load.side_effect = [self.missing_country_column, self.valid_income_data]

        result = data_collect("missing_country_life.csv", 
                              "income_per_person_gdppercapita_ppp_inflation_adjusted.csv", 
                              "1900")
        
        self.assertIsNone(result)

    @patch('projection_life.load')
    def test_empty_data(self, mock_load):
        """
        Test with empty data files
        """
        mock_load.side_effect = [self.empty_data, self.valid_income_data]

        result = data_collect("empty_life_expectancy.csv", 
                              "income_per_person_gdppercapita_ppp_inflation_adjusted.csv", 
                              "1900")
        
        self.assertIsNone(result)

    @patch('projection_life.load')
    def test_invalid_income_values(self, mock_load):
        """
        Test with invalid income values
        """
        mock_load.side_effect = [self.valid_life_expectancy_data, self.invalid_income_data]

        result = data_collect("life_expectancy_years.csv", 
                              "income_per_person_gdppercapita_ppp_inflation_adjusted_data_error.csv", 
                              "1900")

        self.assertIsNotNone(result)
        # One invalid row (haha) should be removed
        self.assertEqual(len(result), 2)

    def test_convert_income(self):
        """
        Test the convert_income function with valid and invalid inputs
        """
        self.assertEqual(convert_income("1K"), 1000.0)
        self.assertEqual(convert_income("2M"), 2_000_000.0)
        self.assertEqual(convert_income("3B"), 3_000_000_000.0)
        self.assertIsNone(convert_income("invalid"))
        self.assertIsNone(convert_income(None))


if __name__ == '__main__':
    unittest.main()
