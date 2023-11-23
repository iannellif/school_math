import random
import argparse

# Function to generate addition exercises of varying difficulty levels
def generate_addition_exercise(difficulty_level):
    if difficulty_level == 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
    elif difficulty_level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(1, 9)
    elif difficulty_level == 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    else:
        raise ValueError("Invalid difficulty level for addition.")
    
    question = f"{num1} + {num2} = ?"
    answer = num1 + num2
    return question, answer

# Function to generate subtraction exercises of varying difficulty levels
def generate_subtraction_exercise(difficulty_level):
    if difficulty_level == 1:
        num1 = random.randint(1, 99)
        num2 = random.randint(1, num1)
    elif difficulty_level == 2:
        num1 = random.randint(10, 99)
        ones_digit = num1 % 10
        if ones_digit == 9:    
            num2 = 10
        else:    
            num2 = random.randint(ones_digit + 1, 9)
            while num2 <= ones_digit:  # Ensure num2 is not smaller than the ones in num1
                num2 = random.randint(ones_digit + 1, 9)
    elif difficulty_level == 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, num1)
    else:
        raise ValueError("Invalid difficulty level for subtraction.")
    
    question = f"{num1} - {num2} = ?"
    answer = num1 - num2
    return question, answer

# Function to generate multiplication exercises of varying difficulty levels
def generate_multiplication_exercise(difficulty_level):
    if difficulty_level == 1:
        num1 = random.randint(2, 9)  # Exclude 1 and 10
        num2 = random.randint(2, 9)
    elif difficulty_level == 2:
        num1 = random.randint(11, 20)
        num2 = random.randint(2, 9)
    elif difficulty_level == 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(2, 9)
    else:
        raise ValueError("Invalid difficulty level for multiplication.")
    
    question = f"{num1} x {num2} = ?"
    answer = num1 * num2
    return question, answer

# Main function to generate exercises of a specific type and difficulty level
def generate_exercises_by_type_and_difficulty(num_exercises, exercise_type, difficulty_level):
    exercises = []
    if exercise_type == "addition":
        generate_func = generate_addition_exercise
    elif exercise_type == "subtraction":
        generate_func = generate_subtraction_exercise
    elif exercise_type == "multiplication":
        generate_func = generate_multiplication_exercise
    else:
        print("Invalid exercise type.")
        return exercises

    for _ in range(num_exercises):
        question, answer = generate_func(difficulty_level)
        exercises.append((question, answer))
    return exercises

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-exercises", type=int, default=20, help="Number of exercises to generate")
    parser.add_argument("--exercise-type", choices=["addition", "subtraction", "multiplication"], help="Type of exercises to generate")
    parser.add_argument("--difficulty-level", type=int, choices=[1, 2, 3], default=1, help="Difficulty level (1, 2, or 3)")
    args = parser.parse_args()
    
    num_exercises = args.num_exercises
    exercise_type = args.exercise_type
    difficulty_level = args.difficulty_level
    
    exercises = generate_exercises_by_type_and_difficulty(num_exercises, exercise_type, difficulty_level)
    
    if exercises:
        for i, (question, answer) in enumerate(exercises, 1):
            print(f"Exercise {i}: {question}")
    else:
        print("No exercises generated.")
