# Day 2 - Python Basics
# AI & ML Internship - Codomax Digital Solutions

# ---- Variables & data types ----
name = "Alice"          # string
age = 21                 # int
gpa = 8.75                # float
is_enrolled = True        # boolean

print(type(name), type(age), type(gpa), type(is_enrolled))

# ---- Operators ----
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

print(a > b, a == b, a != b)            # comparison
print(a > 5 and b < 5, a > 5 or b > 5)  # logical

# ---- Loops ----
# for loop
for i in range(1, 6):
    print("Iteration:", i)

# while loop
count = 0
while count < 5:
    print("Count is", count)
    count += 1

# ---- Functions ----
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

scores = [78, 85, 90, 62, 74]
print("Average score:", calculate_average(scores))

def predict_score_naive(hours):
    """A naive placeholder before we build the real ML model."""
    return min(100, hours * 9 + 5)

print(predict_score_naive(6))

# ---- Mini-program (ties into the project) ----
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

for s in scores:
    print(f"Score {s} -> Grade {grade(s)}")
