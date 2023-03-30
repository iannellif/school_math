import random

# function to generate a random math problem with specified difficulty level
def generate_problem(operation, difficulty):
    if operation == "addition":
        a = random.randint(10**(difficulty-1), 10**difficulty-1)
        b = random.randint(10**(difficulty-1), 10**difficulty-1)
        problem = f"{a} + {b} = ?"
        answer = str(a + b)
    elif operation == "subtraction":
        a = random.randint(10**(difficulty-1), 10**difficulty-1)
        b = random.randint(10**(difficulty-2), a-1)
        problem = f"{a} - {b} = ?"
        answer = str(a - b)
    elif operation == "multiplication":
        a = random.randint(10**(difficulty-1), 10**difficulty-1)
        b = random.randint(10**(difficulty-2), 10**(difficulty-1)-1)
        problem = f"{a} x {b} = ?"
        answer = str(a * b)
    elif operation == "division":
        b = random.randint(10**(difficulty-2), 10**(difficulty-1)-1)
        a = b * random.randint(10**(difficulty-1), 10**difficulty-1)
        problem = f"{a} / {b} = ?"
        answer = str(a // b)
    elif operation == "fractions":
        a = random.randint(1, 10)
        b = random.randint(10**(difficulty-1), 10**difficulty-1)
        problem = f"What is {a}/{b} as a decimal?"
        answer = "{:.{diff}f}".format(a / b, diff=difficulty+2)
    elif operation == "proportions":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        x = c * b // a
        problem = f"If {a}:{b} = {c}:{x}, what is x?"
        answer = str(x)
    elif operation == "decimals":
        a = round(random.uniform(10**(difficulty-1), 10**difficulty-1), difficulty)
        b = round(random.uniform(10**(difficulty-1), 10**difficulty-1), difficulty)
        problem = f"What is {a} + {b}?"
        answer = "{:.{diff}f}".format(a + b, diff=difficulty)
    return (problem, answer)

# function to generate a set of math exercises
def generate_exercises(num_problems, operations, difficulty):
    exercises = []
    for i in range(num_problems):
        operation = random.choice(operations)
        problem, answer = generate_problem(operation, difficulty)
        exercises.append((problem, answer))
    return exercises

# input parameters
num_problems = int(input("Enter the number of math exercises: "))
operations = input("Enter the types of math operations (separated by commas): ").split(",")
difficulty = int(input("Enter the difficulty level (1-10): "))

# generate math exercises
exercises = generate_exercises(num_problems, operations, difficulty)

# write exercises to file
with open("math_exercises.txt", "w") as f:
    for i, (problem, answer) in enumerate(exercises):
        f.write(f"{i+1}. {problem}\n")

# print confirmation message
print(f"Successfully generated {num_problems} math exercises of the following types: {', '.join(operations)}
