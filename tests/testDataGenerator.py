import pytest
from companyGenerator.dataGenerator import CompanyDataGenerator

def test_generate_data():
    generator = CompanyDataGenerator(row_count=10)
    df = generator.generate_data()
    assert df.shape == (10, 30)  # Check the number of rows and columns
    assert df["Registration ID"].is_unique, "Unique keys are not unique."