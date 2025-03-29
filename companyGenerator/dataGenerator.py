import pandas as pd
import numpy as np
from faker import Faker

class CompanyDataGenerator:
    def __init__(self, row_count=1000):
        self.row_count = row_count
        self.fake = Faker()

    def generate_data(self):
        # Qualitative data (lists of at least 10 values)
        company_names = [self.fake.company() for _ in range(self.row_count)]
        company_types = ["S.A.", "S.R.L.", "Startup", "Cooperative", "Corporation", "LLC", "Partnership", "Non-Profit", "Public Company", "Private Company"]
        industries = ["Technology", "Finance", "Healthcare", "Manufacturing", "Retail", "Education", "Energy", "Telecommunications", "Transportation", "Real Estate"]
        countries = [self.fake.country() for _ in range(self.row_count)]
        cities = [self.fake.city() for _ in range(self.row_count)]
        product_lines = ["Software", "Electronics", "Healthcare Devices", "Financial Services", "Consumer Goods", "Automobiles", "Energy Solutions", "Telecom Services", "Education Tools", "Real Estate Services"]
        benefit_policies = ["Health Insurance", "Remote Work", "Stock Options", "Retirement Plans", "Tuition Reimbursement", "Parental Leave", "Wellness Programs", "Flexible Hours", "Bonuses", "Professional Development"]
        num_offices = list(range(2, 2 * self.row_count + 1, 2))

        # Generate data
        data = {
            "Registration ID": [self.fake.uuid4() for _ in range(self.row_count)],  # Unique key
            "Company Name": np.random.choice(company_names, self.row_count),
            "Company Type": np.random.choice(company_types, self.row_count),
            "Industry/Sector": np.random.choice(industries, self.row_count),
            "Country of Origin": np.random.choice(countries, self.row_count),
            "Main Operating City": np.random.choice(cities, self.row_count),
            "Year Founded": np.random.randint(1900, 2023, self.row_count),
            "Number of Offices": num_offices,
            "Annual Revenue (USD)": np.random.normal(500000, 200000, self.row_count).astype(int),
            "Net Profit (USD)": np.random.normal(50000, 10000, self.row_count).astype(int),

            # Exponential relationship with Number of Offices
            "Number of Employees": self._generate_exponential_employees(num_offices),

            "Average Monthly Salary (USD)": np.random.normal(3500, 1000, self.row_count).astype(int),
            "Market Cap (USD)": np.random.choice(["100M", "2B", "500M"], self.row_count),
            "Number of Investors": np.random.randint(1, 20, self.row_count),
            "Total Investment Received (USD)": np.random.normal(5000000, 1000000, self.row_count).astype(int),
            "Main Product Line": np.random.choice(product_lines, self.row_count),
            "Number of Products/Services Offered": np.random.randint(5, 200, self.row_count),
            "Average Product Price (USD)": np.random.normal(500, 100, self.row_count).astype(int),
            "Number of Active Customers": np.random.randint(1000, 10000000, self.row_count),
            "Customer Retention Rate (%)": np.random.uniform(60, 95, self.row_count).round(2),
            "Percentage of Revenue from Recurring Customers": np.random.uniform(40, 95, self.row_count).round(2),

            # Modified to use pie chart distribution (45%, 35%, 25%, 15%, 10%, 5%)
            "Number of Cloud Servers": self._generate_pie_distribution(self.row_count),

            "Number of Physical Offices": np.random.randint(1, 300, self.row_count),
            "Automation Level (%)": np.random.uniform(10, 95, self.row_count).round(2),
            "Employee Satisfaction Index (1-10)": np.random.uniform(6, 9, self.row_count).round(1),
            "Employee Turnover Rate (%)": np.random.uniform(5, 40, self.row_count).round(2),
            "Percentage of Remote Employees": np.random.uniform(10, 80, self.row_count).round(2),
            "Average Years of Experience": np.random.randint(3, 15, self.row_count),
            "Number of Countries Operated In": np.random.randint(1, 50, self.row_count),
            "Key Benefits Policy": np.random.choice(benefit_policies, self.row_count),
        }
        return pd.DataFrame(data)

    def _generate_pie_distribution(self, size):
        """Generate data with an automatic mathematical distribution for pie chart"""
        num_values = 20
        base = 10
        ratio = 2
        values = np.array([base * (ratio ** i) for i in range(num_values)])
        decay_factor = 0.7
        probabilities = np.exp(-decay_factor * np.arange(num_values))
        probabilities /= probabilities.sum()
        return np.random.choice(values, size=size, p=probabilities)

    def _generate_exponential_employees(self, offices):
        """Generate employees count with exponential growth based on offices"""
        employees = []
        for i in range(len(offices)):
            employees.append(offices[i]**2)
        return employees
