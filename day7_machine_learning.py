import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned dataset
data = pd.read_csv("clean_student_scores.csv")

print("Student Score Dataset:")
print(data)

# Select input and output
X = data[["Hours"]]
y = data["Scores"]

print("\nInput (X):")
print(X)

print("\nOutput (y):")
print(y)

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Display training data
print("\nTraining Input:")
print(X_train)

print("\nTraining Output:")
print(y_train)

# Display testing data
print("\nTesting Input:")
print(X_test)

print("\nTesting Output:")
print(y_test)

# Display sizes
print("\nDataset Size:", len(data))
print("Training Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))

print("\nDay 7 Machine Learning Basics Completed Successfully!")