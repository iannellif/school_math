import streamlit as st
import subprocess

# Title
st.title("Math Exercise Portal")

# Sidebar
st.sidebar.header("Options")
exercise_type = st.sidebar.selectbox("Select Exercise Type", ["addition", "subtraction", "multiplication"])
difficulty_level = st.sidebar.selectbox("Select Difficulty Level", [1, 2, 3])
num_exercises = st.sidebar.number_input("Number of Exercises", min_value=1, value=20)

# Initialize session state variables
if "exercise_index" not in st.session_state:
    st.session_state.exercise_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = [""] * num_exercises

# Generate Exercises Button
if st.sidebar.button("Generate Exercises"):
    # Run the exercise.py script with the selected options
    cmd = f"python exercise.py --num-exercises {num_exercises} --exercise-type {exercise_type} --difficulty-level {difficulty_level}"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    exercises = result.stdout.splitlines()

    # Display exercises one at a time with a button to navigate to the next exercise
    if st.session_state.exercise_index < num_exercises:
        st.subheader(f"Exercise {st.session_state.exercise_index + 1}:")
        st.write(exercises[st.session_state.exercise_index])
        
        # User input for the answer
        user_answer = st.text_input(f"Your Answer (Exercise {st.session_state.exercise_index + 1}):")
        
        # Store the answer in the list
        st.session_state.answers[st.session_state.exercise_index] = user_answer

        # Button to proceed to the next exercise
        if st.button("Next Exercise") or (user_answer and st.session_state.enter_pressed):
            st.session_state.exercise_index += 1
            st.session_state.enter_pressed = False  # Reset the Enter flag
            st.empty()  # Clear the current question and input field

    # Clear any remaining input fields and questions
    st.empty()

# About
st.sidebar.markdown("### About")
st.sidebar.info("This is a simple math exercise portal powered by Streamlit.")
