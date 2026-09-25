# ==========================================
# DAY 3 - NUMPY BASICS
# AI & ML INTERNSHIP
# Student Score Prediction Project
# ==========================================

import numpy as np

# 1. Create a NumPy array
study_hours = np.array([1, 2, 3, 4, 5])

print("Study Hours:")
print(study_hours)


# 2. Create a scores array
scores = np.array([35, 45, 55, 65, 75])

print("\nStudent Scores:")
print(scores)


# 3. Array indexing
print("\n--- Array Indexing ---")

print("First study hour:", study_hours[0])
print("Third study hour:", study_hours[2])


# 4. Array slicing
print("\n--- Array Slicing ---")

print("First three values:", study_hours[0:3])


# 5. Mathematical operations
print("\n--- Mathematical Operations ---")

print("Scores + 5:")
print(scores + 5)

print("\nScores - 5:")
print(scores - 5)

print("\nScores * 2:")
print(scores * 2)

print("\nScores / 2:")
print(scores / 2)


# 6. Statistical operations
print("\n--- Statistical Operations ---")

print("Mean:", np.mean(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))
print("Standard Deviation:", np.std(scores))


# 7. Array information
print("\n--- Array Information ---")

print("Shape:", scores.shape)
print("Size:", scores.size)
print("Data Type:", scores.dtype)


# 8. Create an array of zeros
zeros = np.zeros(5)

print("\nArray of Zeros:")
print(zeros)


# 9. Create a sequence
sequence = np.arange(1, 11)

print("\nSequence from 1 to 10:")
print(sequence)


print("\n==========================================")
print("DAY 3 NUMPY TASK COMPLETED SUCCESSFULLY!")
print("==========================================")