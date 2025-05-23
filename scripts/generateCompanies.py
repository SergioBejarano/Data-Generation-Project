import argparse
from companyGenerator.dataGenerator import CompanyDataGenerator

import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description='Generate company data')
    parser.add_argument('--row_count', type=int, default=1000,
                        help='Number of rows to generate (default: 1000)')
    args = parser.parse_args()

    generator = CompanyDataGenerator(row_count=args.row_count)
    df = generator.generate_data()

    df.to_csv("data/companies.csv", index=False, encoding="utf-8")
    print(f"Data generated and saved to 'data/companies.csv' with {args.row_count} rows.")

    generate_additional_plots(df)

def generate_additional_plots(df):
    """Generate the requested additional plots"""
    plt.figure(figsize=(12, 6))
    cloud_data = df['Number of Cloud Servers'].value_counts()
    total = cloud_data.sum()
    percentages = [f'{(count/total)*100:.3f}%' for count in cloud_data]
    colors = ['#FF6B6B','#4ECDC4','#45B7D1','#FFA07A','#98D8C8','#F7CAC9']
    wedges, texts, autotexts = plt.pie(cloud_data,
                                       colors=colors,
                                       startangle=90,
                                       autopct='',
                                       pctdistance=0.85,
                                       textprops={'fontsize': 10})
    legend_labels = [f"{label} - {count} ({pct})"
                     for label, count, pct in zip(cloud_data.index, cloud_data, percentages)]
    plt.legend(wedges, legend_labels,
               title="N° de Servidores:",
               loc="center left",
               bbox_to_anchor=(1, 0.5),
               fontsize=10,
               frameon=False)
    plt.title('Distribución de Servidores en la Nube\n', fontsize=14, pad=20)
    plt.savefig('plots/servidores_torta.png', bbox_inches='tight', dpi=120)
    plt.close()
    generate_additional_exp_norm(df)
    generate_year_founded_distribution(df)
    generate_employees_vs_revenue(df)


def generate_additional_exp_norm(df):
    """Generate the requested additional plots"""
    df_sorted = df.sort_values('Number of Offices')
    plt.figure(figsize=(10, 6))
    plt.plot(df_sorted['Number of Offices'],
             df_sorted['Number of Employees'],
             'bo', markersize=1)
    plt.title('Relación Creciente: Empleados vs Oficinas', fontsize=14)
    plt.xlabel('Número de Oficinas', fontsize=12)
    plt.ylabel('Número de Empleados', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('plots/empleados_vs_oficinas.png', dpi=300)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.hist(df['Annual Revenue (USD)'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribución de Ingresos Anuales')
    plt.xlabel('Ingresos (USD)')
    plt.ylabel('Frecuencia')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.savefig('plots/distribucion_ingresos.png')
    plt.close()


def generate_year_founded_distribution(df):
    """Generate a plot for Year Founded vs Number of Companies"""
    plt.figure(figsize=(10, 6))
    year_counts = df['Year Founded'].value_counts().sort_index()
    plt.bar(year_counts.index, year_counts.values, color='lightblue', edgecolor='black')
    plt.title('Distribución del Año de Fundación de Empresas', fontsize=14)
    plt.xlabel('Año de Fundación', fontsize=12)
    plt.ylabel('Cantidad de Empresas', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.savefig('plots/year_founded_distribution.png', dpi=300)
    plt.close()


def generate_employees_vs_revenue(df):
    """Generate a plot for Number of Employees vs Annual Revenue"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Number of Employees'], df['Annual Revenue (USD)'],
                alpha=0.5, color='green', edgecolor='black', s=20)
    plt.title('Relación entre Empleados y Revenue Anual', fontsize=14)
    plt.xlabel('Número de Empleados', fontsize=12)
    plt.ylabel('Revenue Anual (USD)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('plots/employees_vs_revenue.png', dpi=300)
    plt.close()



if __name__ == "__main__":
    main()