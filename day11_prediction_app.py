import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Load cleaned dataset
data = pd.read_csv("clean_student_scores.csv")

# Select input and output
X = data[["Hours"]]
y = data["Scores"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)


# Display application title
print("======================================")
print("    STUDENT SCORE PREDICTION APP")
print("======================================")


# Get study hours from user
try:
    hours = float(input("\nEnter the number of study hours: "))

    # Prepare input for prediction
    input_data = pd.DataFrame({"Hours": [hours]})

    # Generate prediction
    prediction = model.predict(input_data)

    # Display result
    print("\n--------------------------------------")
    print("Study Hours     :", hours)
    print("Predicted Score :", round(prediction[0], 2))
    print("--------------------------------------")

except ValueError:
    print("\nPlease enter a valid number.")


print("\nDay 12 Project Improvement Completed Successfully!")