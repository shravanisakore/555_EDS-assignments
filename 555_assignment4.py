import numpy as np
import pandas as pd
import itertools

# Read the CSV file into a DataFrame
df = pd.read_csv("D:\\python\\grainsales.csv")

# Display the DataFrame
print(df)
# 1Group by month and calculate total sales
monthly_sales = df.groupby('Months')['Sales'].sum()

# 2Find the month with the highest sales
best_month = monthly_sales.idxmax()

# 3Calculate the earnings for the best month
earnings = monthly_sales.max()

# Print the result
print("The best month for sales was", best_month, "with earnings of", earnings)
# Group by grain and calculate total sales
grain_sales = df.groupby('GrainName')['Sales'].sum()

# Find the grain with the highest sales
best_selling_grain = grain_sales.idxmax()

# Print the result
print("The product that sold the most was", best_selling_grain)

# Group by city and calculate total number of products sold
city_sales = df.groupby('City').size()

# Find the city with the highest sales
best_selling_city = city_sales.idxmax()

# Print the result
print("The city that sold the most products was", best_selling_city)