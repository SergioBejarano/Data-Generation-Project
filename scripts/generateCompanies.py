import pandas as pd
from companyGenerator.dataGenerator import CompanyDataGenerator

def generate_excel_file(row_count=1000, filename="data/companies.xlsx"):
    """
    Generate company data and save it to an Excel file.

    Parameters:
        row_count (int): Number of rows to generate.
        filename (str): Path to save the Excel file.
    """
    # Generate data
    generator = CompanyDataGenerator(row_count=row_count)
    df = generator.generate_data()

    # Save to Excel
    df.to_excel(filename, index=False)
    print(f"Data generated and saved to '{filename}'.")

if __name__ == "__main__":
    generate_excel_file(row_count=1000, filename="data/companies.xlsx")