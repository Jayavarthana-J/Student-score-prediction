import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load cleaned dataset
data = pd.read_csv("clean_student_scores.csv")

# Input feature and target
X = data[["Hours"]]
y = data["Scores"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Display model details
print("Linear Regression Model Trained Successfully!")

print("\nCoefficient:")
print(model.coef_[0])

print("\nIntercept:")
print(model.intercept_)

# Predict test data
y_pred = model.predict(X_test)

print("\nActual Scores:")
print(y_test.values)

print("\nPredicted Scores:")
print(y_pred)

print("\nDay 8 Linear Regression Completed Successfully!")