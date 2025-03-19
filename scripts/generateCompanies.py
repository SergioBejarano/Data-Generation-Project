from companyGenerator.dataGenerator import CompanyDataGenerator
import pandas as pd

if __name__ == "__main__":
    generator = CompanyDataGenerator(row_count=1000)
    df = generator.generate_data()
    df.to_csv("data/companies.csv", index=False, encoding="utf-8")
    print("Data generated and saved to 'data/companies.csv'.")