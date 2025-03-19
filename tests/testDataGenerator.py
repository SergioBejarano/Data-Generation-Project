import unittest
import pandas as pd
from companyGenerator.dataGenerator import CompanyDataGenerator

class TestDataGenerator(unittest.TestCase):
    def test_generate_data_shape(self):
        """Test that the generated DataFrame has the correct shape (10 rows, 30 columns)."""
        generator = CompanyDataGenerator(row_count=10)
        df = generator.generate_data()
        self.assertEqual(df.shape, (10, 30))

    def test_unique_registration_ids(self):
        """Test that the 'Registration ID' column contains unique values."""
        generator = CompanyDataGenerator(row_count=10)
        df = generator.generate_data()
        self.assertTrue(df["Registration ID"].is_unique)

    def test_annual_revenue_range(self):
        """Test that the 'Annual Revenue (USD)' values are within a reasonable range."""
        generator = CompanyDataGenerator(row_count=10)
        df = generator.generate_data()
        self.assertTrue((df["Annual Revenue (USD)"] >= 0).all())
        self.assertTrue((df["Annual Revenue (USD)"] <= 1200000000).all())

    def test_employee_satisfaction_range(self):
        """Test that the 'Employee Satisfaction Index (1-10)' values are within the range 1 to 10."""
        generator = CompanyDataGenerator(row_count=10)
        df = generator.generate_data()
        self.assertTrue((df["Employee Satisfaction Index (1-10)"] >= 1).all())
        self.assertTrue((df["Employee Satisfaction Index (1-10)"] <= 10).all())
if __name__ == "__main__":
    unittest.main()