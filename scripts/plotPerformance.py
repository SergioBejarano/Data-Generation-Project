import time
import matplotlib.pyplot as plt
from companyGenerator.dataGenerator import CompanyDataGenerator

def measure_execution_time(row_count):
    """Measure the time it takes to generate data for a given row_count."""
    generator = CompanyDataGenerator(row_count=row_count)
    start_time = time.time()
    generator.generate_data()
    end_time = time.time()
    return end_time - start_time

def plot_performance():
    """Plot the execution time for different row counts."""
    row_counts = [100 * i for i in range(1, 21)]
    execution_times = []

    for count in row_counts:
        print(f"Generating data for {count} rows...")
        execution_time = measure_execution_time(count)
        execution_times.append(execution_time)
        print(f"Time taken: {execution_time:.4f} seconds")

    plt.figure(figsize=(10, 6))
    plt.plot(row_counts, execution_times, marker="o", linestyle="-", color="b")
    plt.title("Execution Time vs. Number of Rows")
    plt.xlabel("Number of Rows")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)

    plt.savefig("plots/performance_plot.png")
    print("Plot saved to 'plots/performance_plot.png'")

if __name__ == "__main__":
    plot_performance()