import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load cleaned dataset
data = pd.read_csv("clean_student_scores.csv")

# Input feature and target
X = data[["Hours"]]
y = data["Scores"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Get study hours from the user
hours = float(input("Enter the number of study hours: "))

# Make prediction
prediction = model.predict(
    pd.DataFrame({"Hours": [hours]})
)

# Display result
print("\nStudy Hours:", hours)
print("Predicted Score:", round(prediction[0], 2))

print("\nDay 9 Score Prediction Completed Successfully!")