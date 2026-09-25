# ==========================================
# DAY 5 - DATA CLEANING
# AI & ML INTERNSHIP
# Student Score Prediction Project
# ==========================================

import pandas as pd


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("student_scores.csv")

print("==========================================")
print("          ORIGINAL DATASET")
print("==========================================")

print(df)


# ==========================================
# 2. Check Missing Values
# ==========================================

print("\n==========================================")
print("          MISSING VALUES")
print("==========================================")

missing_values = df.isnull().sum()

print(missing_values)


# ==========================================
# 3. Check Duplicate Rows
# ==========================================

print("\n==========================================")
print("          DUPLICATE ROWS")
print("==========================================")

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)


# ==========================================
# 4. Remove Duplicate Rows
# ==========================================

df = df.drop_duplicates()

print("\n==========================================")
print("       AFTER REMOVING DUPLICATES")
print("==========================================")

print(df)


# ==========================================
# 5. Check Missing Values Again
# ==========================================

print("\n==========================================")
print("     CHECKING MISSING VALUES AGAIN")
print("==========================================")

print(df.isnull().sum())


# ==========================================
# 6. Remove Missing Values
# ==========================================

df = df.dropna()

print("\n==========================================")
print("        AFTER DATA CLEANING")
print("==========================================")

print(df)


# ==========================================
# 7. Dataset Statistics
# ==========================================

print("\n==========================================")
print("        DATASET STATISTICS")
print("==========================================")

print(df.describe())


# ==========================================
# 8. Dataset Information
# ==========================================

print("\n==========================================")
print("        DATASET INFORMATION")
print("==========================================")

df.info()


# ==========================================
# 9. Final Dataset Shape
# ==========================================

print("\n==========================================")
print("          FINAL DATASET SIZE")
print("==========================================")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==========================================
# 10. Save Clean Dataset
# ==========================================

df.to_csv(
    "clean_student_scores.csv",
    index=False
)

print("\n==========================================")
print("Clean dataset saved successfully!")
print("File: clean_student_scores.csv")
print("==========================================")


print("\n==========================================")
print("    DAY 5 TASK COMPLETED SUCCESSFULLY!")
print("==========================================")