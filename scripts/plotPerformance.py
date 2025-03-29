import time
import numpy as np
import matplotlib.pyplot as plt
from companyGenerator.dataGenerator import CompanyDataGenerator
import argparse

def measure_execution_time(row_count):
    """Measure the time it takes to generate data for a given row_count."""
    generator = CompanyDataGenerator(row_count=row_count)
    start_time = time.time()
    generator.generate_data()
    end_time = time.time()
    return end_time - start_time

def plot_performance():
    """Plot the execution time for different row counts with a linear trendline."""
    parser = argparse.ArgumentParser(description='Performance measurement for data generation')
    parser.add_argument('--base', type=int, default=1000,
                        help='Base value for row counts (default: 1000)')
    args = parser.parse_args()

    row_counts = [args.base * i for i in range(1, 21)]
    execution_times = []

    for count in row_counts:
        print(f"Generating data for {count} rows...")
        execution_time = measure_execution_time(count)
        execution_times.append(execution_time)
        print(f"Time taken: {execution_time:.4f} seconds")

    row_counts_np = np.array(row_counts)
    execution_times_np = np.array(execution_times)

    slope, intercept = np.polyfit(row_counts_np, execution_times_np, 1)
    trendline = slope * row_counts_np + intercept

    plt.figure(figsize=(10, 6))
    plt.plot(row_counts, execution_times, marker="o", linestyle="-", color="b", label="Execution Time")
    plt.plot(row_counts, trendline, linestyle="--", color="r", label="Linear Trendline")
    plt.title("Execution Time vs. Number of Rows")
    plt.xlabel("Number of Rows")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.legend()

    plt.savefig("plots/performance_plot_with_trendline.png")
    print("Plot saved to 'plots/performance_plot_with_trendline.png'")

if __name__ == "__main__":
    plot_performance()