import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Create the CSV files based on the provided data

# Now read the data from the CSV files and generate the plot
swe_df = pd.read_csv('swe_mean.csv')
sales_df = pd.read_csv('wheat_yield_per_acre.csv')

# Merge the dataframes on the 'year' column
merged_df = pd.merge(swe_df, sales_df, on='year')

# Drop rows where sales data is missing
merged_df.dropna(subset=['per_acre'], inplace=True)

# Extract the relevant columns
years = merged_df['year']
swe_mean = merged_df['swe_mean']
acre = merged_df['per_acre']

# Calculate the linear regression
slope, intercept, r_value, p_value, std_err = linregress(swe_mean, acre)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(swe_mean, acre, color='blue', label='Data points')

# Plot the trend line
trend_line = slope * swe_mean + intercept
plt.plot(swe_mean, trend_line, color='red', label=f'Trend line (R²={r_value**2:.2f})')

# Add labels and title
plt.xlabel('SWE Mean')
plt.ylabel('Wheat yield per acre (LB)')
plt.title('Correlation between SWE Mean and wheat yield per acre')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
