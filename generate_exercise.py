import random

class MathExerciseGenerator:
    def __init__(self, num_problems, operation, difficulty):
        self.num_problems = num_problems
        self.operation = operation
        self.difficulty = difficulty
        self.exercises_list = ["addition", "subtraction", "multiplication", "division", "fractions", "proportions", "decimals"]
        self.exercises = []
        self.filename = ""

    def generate_problem(self, operation, difficulty):
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

    def generate_exercises(self):
        if self.operation not in self.exercises_list:
            print(f"Invalid math operation. Please choose from {', '.join(self.exercises_list)}")
            return
        for i in range(self.num_problems):
            problem, answer = self.generate_problem(self.operation, self.difficulty)
            self.exercises.append((problem, answer))

    def write_exercises_to_file(self):
        if not self.filename:
            self.filename = f"{self.operation}_exercises_{self.num_problems}_{self.difficulty}"

        with open(f"exercises/{self.filename}_problems.txt", "w") as f:
            f.write(f"{self.operation.capitalize()} Exercises ({self.num_problems} problems, Difficulty: {self.difficulty}/10)\n\n")
            for i, (problem, answer) in enumerate(self.exercises, start=1):
                f.write(f"Problem {i}: {problem}\n\n")
        print(f"Successfully generated {self.num_problems} {self.operation} problems with difficulty {self.difficulty}/10 and saved to {self.filename}_problems.txt")
        
        with open(f"exercises/{self.filename}_solutions.txt", "w") as f:
            f.write(f"{self.operation.capitalize()} Exercises Solutions ({self.num_problems} problems, Difficulty: {self.difficulty}/10)\n\n")
            for i, (problem, answer) in enumerate(self.exercises, start=1):
                f.write(f"Problem {i}: {problem}\n")
                f.write(f"Answer: {answer}\n\n")
        print(f"Successfully generated {self.num_problems} {self.operation} exercises with difficulty {self.difficulty}/10 and saved to {self.filename}_solutions.txt")

            
if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Generate math exercises')
    parser.add_argument('operation', type=str, choices=['addition', 'subtraction', 'multiplication', 'division'], default='addition', help='The type of operation to generate exercises for')
    parser.add_argument('difficulty', type=int, choices=range(1, 11), default=5, help='The difficulty level of the exercises (1-10)')
    parser.add_argument('num_problems', type=int, default=20, help='The number of exercises to generate')
 
    args = parser.parse_args()


#     operation = input("Choose an operation (+, -, *, /, frac, prop): ")
#     num_problems = int(input("How many problems would you like to generate? "))
#     difficulty = int(input("What is the difficulty level (1-10)? "))

    # create instance of MathExerciseGenerator class
    generator = MathExerciseGenerator(operation=args.operation, num_problems=args.num_problems, difficulty=args.difficulty)

    # generate exercises
    generator.generate_exercises()

    # write exercises to files
    generator.write_exercises_to_file()
