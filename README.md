# Student Score Prediction Using Machine Learning

## AI & Machine Learning Internship Project

A practical Machine Learning project developed as part of the **AI & Machine Learning Internship at Codomax Digital Solutions**.

The project focuses on predicting a student's examination score based on the number of hours they study using **Python, Pandas, NumPy, Matplotlib and Scikit-learn**.

---

## 📌 Project Overview

The **Student Score Prediction System** uses a Machine Learning model to predict examination scores based on study hours.

The project follows a complete Machine Learning workflow:

```text
Data Collection
      ↓
Data Exploration
      ↓
Data Cleaning
      ↓
Data Visualization
      ↓
Train-Test Split
      ↓
Linear Regression
      ↓
Model Training
      ↓
Prediction
      ↓
Model Evaluation
      ↓
Prediction Application
      ↓
GitHub Deployment

The internship task sheet describes the project as a Student Score Prediction System that predicts examination scores based on study hours and focuses on data preprocessing, visualization, model training, prediction and evaluation.

🎯 Objectives

The main objectives of this project are:

Learn Python programming fundamentals
Understand NumPy for numerical operations
Learn Pandas for data handling
Perform data cleaning and preprocessing
Visualize relationships within the dataset
Understand basic Machine Learning concepts
Implement Linear Regression
Train a Machine Learning model
Predict student scores
Evaluate model performance
Build a simple prediction application
Organize and publish the project using Git and GitHub
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
NumPy	Numerical computing
Pandas	Data manipulation and analysis
Matplotlib	Data visualization
Scikit-learn	Machine Learning
Jupyter Notebook	Data analysis and experimentation
Git	Version control
GitHub	Project repository
📊 Dataset

The project uses a student score dataset containing two main attributes:

Column	Description
Hours	Number of hours studied
Scores	Student examination score
Example
Hours	Scores
2.5	21
5.1	47
3.2	27
8.5	75
3.5	30

The dataset is used to understand the relationship between study hours and examination scores.

🧠 Machine Learning Approach

The project uses Supervised Learning.

The input feature is:

Study Hours

The target variable is:

Student Score

The relationship is represented as:

Study Hours
     ↓
Machine Learning Model
     ↓
Predicted Score
📈 Algorithm Used
Linear Regression

Linear Regression is used to model the relationship between study hours and student examination scores.

The basic relationship can be represented as:

y = mx + c

Where:

y = predicted score
x = study hours
m = coefficient
c = intercept

The model learns the relationship from the training data and uses it to predict scores for new study-hour values.

📅 Internship Task Progress
Day 1 — Environment Setup
Tasks Completed
Installed Python
Installed VS Code
Installed Jupyter Notebook
Installed Git
Learned basic concepts of:
Artificial Intelligence
Machine Learning
Data Science
Created GitHub repository
Executed first Python program
Expected Outcome

Development environment successfully prepared.

Day 2 — Python Basics
Tasks Completed
Variables
Data types
Operators
Conditional statements
For loops
While loops
Lists
Functions
Basic Python programs
Expected Outcome

Basic Python programming skills developed.

Day 3 — NumPy
Tasks Completed
Created NumPy arrays
Array indexing
Array slicing
Mathematical operations
Mean
Maximum
Minimum
Standard deviation
Array shape and size
Numerical sequences
Expected Outcome

NumPy fundamentals completed.

Day 4 — Pandas
Tasks Completed
Imported Pandas
Created DataFrames
Loaded student score data
Explored rows and columns
Checked dataset shape
Checked column names
Checked data types
Used statistical functions
Saved dataset as CSV
Expected Outcome

Student score dataset successfully loaded and explored.

Day 5 — Data Cleaning
Tasks Completed
Checked missing values
Checked duplicate records
Removed duplicate records
Handled missing values
Generated dataset statistics
Prepared clean dataset
Expected Outcome

Clean dataset prepared for Machine Learning.

Day 6 — Data Visualization
Tasks Completed

Created:

Scatter plot
Bar chart
Line chart

The visualizations help understand the relationship between study hours and student scores.

Expected Outcome

Basic data visualizations created.

Day 7 — Machine Learning Basics
Topics Covered
Supervised Learning
Training data
Testing data
Train-test split
Linear Regression

The dataset was divided into training and testing portions before model development.

Expected Outcome

Basic Machine Learning concepts understood.

Day 8 — Model Building
Tasks Completed
Imported Scikit-learn
Created Linear Regression model
Prepared input and target variables
Split the dataset
Trained the model
Generated predictions
Expected Outcome

Linear Regression model successfully trained.

Day 9 — Prediction

The trained model was used to predict examination scores based on study hours.

Example workflow:

Study Hours: 7
       ↓
Linear Regression Model
       ↓
Predicted Score
Expected Outcome

Student score predictions generated.

Day 10 — Model Evaluation

The trained model was evaluated using:

Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

R² Score

Measures how well the model explains the variation in the target values.

The actual values generated by the trained model are recorded in the project results.

Expected Outcome

Model performance measured.

Day 11 — Prediction Application

A Python-based prediction application was created.

The application allows the user to enter study hours.

Example:

Enter your study hours: 7

Study Hours     : 7.00
Predicted Score : [Model Output]
Expected Outcome

Working Student Score Prediction application.

Day 12 — Project Improvement
Improvements
Organized project files
Added comments
Improved Python code structure
Organized dataset files
Organized screenshots
Created requirements file
Prepared project README
Expected Outcome

Professional project structure.

Day 13 — GitHub

The project was prepared for GitHub with:

Python source files
Dataset
Clean dataset
Jupyter Notebook
Screenshots
README
Requirements file
.gitignore

Git commands used:

git init
git add .
git commit -m "Complete Student Score Prediction project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
Expected Outcome

Project published on GitHub.

Day 14 — Final Submission

Final project submission includes:

GitHub repository
Jupyter Notebook
Dataset
Screenshots
README
Demo video
Internship submission form
Expected Outcome

Student Score Prediction project completed successfully.

📂 Project Structure
student-score-prediction/
│
├── .gitignore
│
├── README.md
│
├── hello.py
│
├── day2_python_basics.py
│
├── day3_numpy.py
│
├── day4_pandas.py
│
├── day5_data_cleaning.py
│
├── day6_visualization.py
│
├── day7_ml_basics.py
│
├── day8_train_model.py
│
├── day9_prediction.py
│
├── day10_evaluate_model.py
│
├── day11_prediction_app.py
│
├── student_scores.csv
│
├── clean_student_scores.csv
│
├── requirements.txt
│
├── notebook/
│   └── Student_Score_Prediction.ipynb
│
└── screenshots/
    ├── scatter_plot.png
    ├── bar_chart.png
    ├── line_chart.png
    ├── evaluation.png
    └── prediction_app.png
⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project
cd student-score-prediction
3. Install required libraries
pip install -r requirements.txt

Or install them individually:

pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install jupyter
▶️ Running the Project
Run Python Basics
python day2_python_basics.py
Run NumPy
python day3_numpy.py
Run Pandas
python day4_pandas.py
Run Data Cleaning
python day5_data_cleaning.py
Run Visualization
python day6_visualization.py
Run Machine Learning Basics
python day7_ml_basics.py
Train the Model
python day8_train_model.py
Generate Predictions
python day9_prediction.py
Evaluate the Model
python day10_evaluate_model.py
Run Prediction Application
python day11_prediction_app.py
📓 Jupyter Notebook

The complete Machine Learning workflow can also be performed using Jupyter Notebook.

Start Jupyter:

jupyter notebook

Open:

notebook/Student_Score_Prediction.ipynb

The notebook contains:

Project Introduction
Import Libraries
Dataset Loading
Data Exploration
Data Cleaning
Data Visualization
Train-Test Split
Linear Regression
Model Training
Prediction
Model Evaluation
Conclusion
📊 Project Workflow in Detail
                 STUDENT DATASET
                       │
                       ▼
                DATA EXPLORATION
                       │
                       ▼
                 DATA CLEANING
                       │
                       ▼
               DATA VISUALIZATION
                       │
                       ▼
                 TRAIN-TEST SPLIT
                       │
                       ▼
                LINEAR REGRESSION
                       │
                       ▼
                  MODEL TRAINING
                       │
                       ▼
                    PREDICTION
                       │
                       ▼
               MODEL EVALUATION
                  /      |      \
                MAE     MSE      R²
                       │
                       ▼
                PREDICTION APP
                       │
                       ▼
                    GITHUB
📸 Screenshots

The project includes screenshots demonstrating:

Python program execution
NumPy operations
Pandas dataset exploration
Data cleaning
Scatter plot
Bar chart
Line chart
Machine Learning model results
Model evaluation
Prediction application
📋 Model Evaluation

The model is evaluated using:

MAE - Mean Absolute Error
MSE - Mean Squared Error
R²  - R² Score

The actual evaluation values should be taken directly from the model execution rather than manually entered.

Example format:

MAE Score : [Actual Output]
MSE Score : [Actual Output]
R² Score  : [Actual Output]
💻 Prediction Application

The prediction application accepts study hours from the user.

Example:

========================================
      STUDENT SCORE PREDICTION
========================================

Enter your study hours: 7

========================================
              RESULT
========================================

Study Hours     : 7.00
Predicted Score : [Model Output]

========================================
🔍 Key Learning Outcomes

Through this project, I gained practical experience in:

Python programming
Numerical computing
Data manipulation
Data cleaning
Data visualization
Supervised Machine Learning
Linear Regression
Model training
Prediction
Model evaluation
Git and GitHub
Project organization
🚀 Future Improvements

Possible future improvements include:

Developing a web-based interface
Adding more student-related features
Using additional Machine Learning algorithms
Comparing multiple models
Adding interactive visualizations
Deploying the application online
Adding a database
Improving prediction and evaluation capabilities
👩‍💻 Author

Jayavarthana J

B.E. Computer Science and Engineering – Cybersecurity Honors
Suguna College of Engineering, Coimbatore

🏢 Internship

AI & Machine Learning Internship
Codomax Digital Solutions

The internship focuses on practical experience in data analysis, Machine Learning and predictive modeling using Python and industry-standard libraries.

📜 Project Status
Day 1   ✅ Environment Setup
Day 2   ✅ Python Basics
Day 3   ✅ NumPy
Day 4   ✅ Pandas
Day 5   ✅ Data Cleaning
Day 6   ⬜ Data Visualization
Day 7   ⬜ Machine Learning Basics
Day 8   ⬜ Model Building
Day 9   ⬜ Prediction
Day 10  ⬜ Model Evaluation
Day 11  ⬜ Prediction Application
Day 12  ⬜ Project Improvement
Day 13  ⬜ GitHub
Day 14  ⬜ Final Submission
