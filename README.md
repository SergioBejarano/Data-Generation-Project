# Data Generation Project

Overview
This project focuses on generating pseudorandom company data that closely resembles real-world data. The goal is to create a dataset with 30 columns containing both qualitative and numerical data, ensuring that the generated data is realistic, unique, and adheres to specific constraints.

✅ How Data Generation Works?

**1. Qualitative Data**
Qualitative data (e.g., company names, industries, cities) is generated using predefined lists with at least 10 values for each field. This ensures variety and avoids repetition. For example:

Company Names: Generated using the Faker library, which provides realistic company names.

Industries: A predefined list of industries (e.g., Technology, Finance, Healthcare) is used.

Cities and Countries: Realistic city and country names are selected from predefined lists.

**2. Numerical Data**
Numerical data (e.g., revenue, number of employees, salaries) is generated using statistical distributions to ensure realism. For example:

Annual Revenue: Generated using a normal distribution with a mean of 500,000 and a standard deviation of 200,000.

Employee Satisfaction Index: Generated using a uniform distribution between 1 and 10.

Number of Employees: Generated using a random integer within a realistic range (e.g., 15 to 25,000).

**3. Unique Keys**
Each row in the dataset has a unique identifier (Registration ID) generated using UUID (Universally Unique Identifier). This ensures that no two rows have the same ID.

**4. Realistic Constraints**
The generated data adheres to realistic constraints:

Revenue and Profit: Non-negative values within reasonable ranges.

Employee Satisfaction: Values between 1 and 10.

Customer Retention Rate: Values between 60% and 95%.

🔑 **Key Features**

1. Realistic Data
Qualitative Data: Uses predefined lists and Faker to generate realistic names, industries, and locations.

Numerical Data: Uses statistical distributions (normal, uniform) to ensure realistic values.

2. Unique Identifiers
Each row has a unique Registration ID generated using UUID.

3. Customizable Data Generation
The number of rows can be adjusted by passing the row_count parameter to the CompanyDataGenerator class.

4. Validation
The generated data is validated to ensure it meets specific constraints (e.g., unique IDs, valid ranges).

## Requirements

- Python 3.8+
- Dependencies: `pandas`, `numpy`, `Faker`, `unitest`

## ✅ Run tests with coverage

```sh
coverage run -m unittest discover -s tests
```

## 📊 Generate coverage report:
```sh
coverage report -m
```


![image](https://github.com/user-attachments/assets/31fd0180-960f-4c98-9d1a-2f0236f536a1)



##  Generating data
```sh
python -m scripts.generateCompanies --row_count

```

##  Generating graphic
```sh
python -m scripts.plotPerformance --base

```
![image](https://github.com/user-attachments/assets/da806cf4-e577-4766-9bd0-9103916e23cd)

![image](https://github.com/user-attachments/assets/f7fa9404-6d8e-40d5-92b9-743548430886)


## Algorithm Complexity

### Total Complexity

1. **Initialization of qualitative lists**: \( O(1) \).
2. **Data generation for each column**: \( O(n) \) for each column.
   - Since there are 30 columns, the total complexity is \( O(30n) = O(n) \).
3. **Creation of the DataFrame**: \( O(n \cdot m) = O(30n) = O(n) \).

Thus, the **total complexity of the algorithm** is:

\[
O(1) + O(n) + O(n) = O(n)
\]

---

### Conclusion

- The algorithm complexity is **linear** (\( O(n) \)) concerning the number of rows (`row_count`).
- This means that execution time **increases proportionally** with the input size (`row_count`).
- The algorithm is **efficient** for generating large volumes of data since it **does not** include quadratic or exponential operations.



