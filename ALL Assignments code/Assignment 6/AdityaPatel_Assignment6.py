# Assignment 6: Data preprocessing on a .csv/.xls file using Pandas
from pathlib import Path
import pandas as pd

# Load dataset from CSV file
csv_path = Path(__file__).with_name("students_data.csv")
df = pd.read_csv(csv_path)

print("Original Dataset:")
print(df)

print("\nFirst 5 rows (head):")
print(df.head())

print("\nDataset Info:")
df.info()

print("\nStatistical Summary (describe):")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())

# Demonstrate dropna() without modifying the main DataFrame
print("\nRows without any missing values (dropna):")
print(df.dropna())

# Handle missing values using fillna() with mean, median, and mode
df_cleaned = df.copy()
df_cleaned["Marks"] = df_cleaned["Marks"].fillna(df_cleaned["Marks"].mean())
df_cleaned["Age"] = df_cleaned["Age"].fillna(df_cleaned["Age"].median())
df_cleaned["City"] = df_cleaned["City"].fillna(df_cleaned["City"].mode()[0])

print("\nDataset after filling missing values (fillna with mean/median/mode):")
print(df_cleaned)

# Identify and remove duplicate records
print("\nDuplicate rows mask (duplicated):")
print(df_cleaned.duplicated())

df_cleaned = df_cleaned.drop_duplicates().reset_index(drop=True)
print("\nDataset after removing duplicates (drop_duplicates):")
print(df_cleaned)

# Filter and select data using loc[]
high_scorers = df_cleaned.loc[df_cleaned["Marks"] >= 85, ["Name", "Marks", "City"]]
print("\nFiltered students with Marks >= 85 using loc[]:")
print(high_scorers)
