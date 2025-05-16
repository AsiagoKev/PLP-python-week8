import pandas as pd

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Explore structure
print("Columns:\n", df.columns)
print("\nPreview:\n", df.head())

# Check missing values
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values[missing_values > 0])

# Select countries of interest
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Handle missing values
df[['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']] = (
    df[['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']]
    .fillna(0)
)

import matplotlib.pyplot as plt
import seaborn as sns

# Plot total cases over time
plt.figure(figsize=(10, 6))
for country in countries:
    df_country = df[df['location'] == country]
    plt.plot(df_country['date'], df_country['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid()
plt.show()

# Death Rate Calculation
df['death_rate'] = df['total_deaths'] / df['total_cases']

# Cumulative vaccinations
plt.figure(figsize=(10, 6))
for country in countries:
    df_country = df[df['location'] == country]
    plt.plot(df_country['date'], df_country['total_vaccinations'], label=country)
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid()
plt.show()
