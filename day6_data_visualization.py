import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("clean_student_scores.csv")

# Display dataset
print("Student Score Dataset:")
print(data)

# Display basic information
print("\nDataset Shape:")
print(data.shape)

print("\nDataset Columns:")
print(data.columns)

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(data["Hours"], data["Scores"])
plt.xlabel("Study Hours")
plt.ylabel("Student Score")
plt.title("Study Hours vs Student Scores")
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(data["Hours"], data["Scores"])
plt.xlabel("Study Hours")
plt.ylabel("Student Score")
plt.title("Study Hours and Student Scores")
plt.show()

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(data["Hours"], data["Scores"], marker="o")
plt.xlabel("Study Hours")
plt.ylabel("Student Score")
plt.title("Study Hours vs Student Scores")
plt.grid(True)
plt.show()

# Histogram of Scores
plt.figure(figsize=(8, 5))
plt.hist(data["Scores"], bins=8)
plt.xlabel("Student Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Scores")
plt.show()

print("\nDay 6 Data Visualization Completed Successfully!")