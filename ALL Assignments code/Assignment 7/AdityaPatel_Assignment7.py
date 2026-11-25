# Assignment 7: Data visualization using Matplotlib and Seaborn
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset using Pandas
csv_path = Path(__file__).with_name("student_performance.csv")
df = pd.read_csv(csv_path)

# Inspect the dataset
print("First 5 rows:")
print(df.head())
print("\nDataset Info:")
df.info()
print("\nSummary Statistics:")
print(df.describe())

# 1. Line Plot: Internal Marks vs Final Marks across Students
plt.figure(figsize=(8, 5))
plt.plot(df["Student"], df["Final_Marks"], marker="o", label="Final Marks")
plt.plot(df["Student"], df["Internal_Marks"], marker="s", label="Internal Marks")
plt.title("Student Marks Comparison (Line Plot)")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Plot: Average Final Marks by Subject
subject_avg = df.groupby("Subject")["Final_Marks"].mean()
plt.figure(figsize=(7, 5))
plt.bar(subject_avg.index, subject_avg.values, color="steelblue")
plt.title("Average Final Marks by Subject (Bar Plot)")
plt.xlabel("Subject")
plt.ylabel("Average Final Marks")
plt.tight_layout()
plt.show()

# 3. Scatter Plot: Study Hours vs Final Marks
plt.figure(figsize=(7, 5))
plt.scatter(df["Study_Hours"], df["Final_Marks"], color="darkorange")
plt.title("Study Hours vs Final Marks (Scatter Plot)")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.show()

# 4. Heatmap: Correlation Matrix of Numerical Attributes using Seaborn
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Student Performance")
plt.tight_layout()
plt.show()
