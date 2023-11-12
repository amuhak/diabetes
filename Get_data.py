import tkinter as tk
from tkinter import *
from tkinter import simpledialog


def get_user_input():
    import numpy as np

    all_the_answers = []

    def categorize_age(age):
        category = 0
        if 18 <= age <= 24:
            category = 1
        elif 25 <= age <= 29:
            category = 2
        elif 30 <= age <= 34:
            category = 3
        elif 35 <= age <= 39:
            category = 4
        elif 40 <= age <= 44:
            category = 5
        elif 45 <= age <= 49:
            category = 6
        elif 50 <= age <= 54:
            category = 7
        elif 55 <= age <= 59:
            category = 8
        elif 60 <= age <= 64:
            category = 9
        elif 65 <= age <= 69:
            category = 10
        elif 70 <= age <= 74:
            category = 11
        elif 75 <= age <= 79:
            category = 12
        elif age >= 80:
            category = 12
        return category

    questions = {
        "HighBP": "Do you have high blood pressure?",
        "HighChol": "Do you have high cholesterol?",
        "CholCheck": "Have you had your cholesterol checked in the past 5 years?",
        "BMI": "What is your Body Mass Index?",
        "Smoker": "Have you smoked at least 100 cigarettes in your entire life?",
        "Stroke": "Have you ever had a stroke?",
        "HeartDiseaseorAttack": "Have you ever been told by a doctor that you have coronary heart disease (CHD) or "
        "myocardial infarction (MI)?",
        "PhysActivity": "During the past month, other than your regular job, did you participate in any physical "
        "activities or exercises?",
        "Fruits": "Do you consume fruit 1 or more times per day?",
        "Veggies": "Do you consume vegetables 1 or more times per day?",
        "HvyAlcoholConsump": "Are you a heavy drinker (adult men having more than 14 drinks per week and adult women "
        "having more than 7 drinks per week)",
        "AnyHealthcare": "Do you have any kind of health care coverage?",
        "NoDocbcCost": "Was there a time in the past 12 months when you needed to see a doctor but could not because of "
        "cost?",
        "GenHlth": "Would you say that in general your health is: scale 1-5; 1 = excellent 2 = very good 3 = good 4 = "
        "fair 5 = poor",
        "MentHlth": "Now thinking about your mental health, which includes stress, depression, and problems with "
        "emotions, for how many days during the past 30 days was your mental health not good? scale 1-30 days",
        "PhysHlth": "Now thinking about your physical health, which includes physical illness and injury, for how many "
        "days during the past 30 days was your physical health not good? scale 1-30 days",
        "DiffWalk": "Do you have serious difficulty walking or climbing stairs?",
        "Sex": "female or male",
        "Age": "Age in years (this will be generalized into 13 age groups [AGEG5YR])",
        "Education": "Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = "
        "Grades 1 through 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED ("
        "High school graduate) 5 = College 1 year to 3 years (Some college or technical school) 6 = College "
        "4 years or more (College graduate)",
        "Income": "[INCOME2] scale 1-8; 1 = Less than $10,000 2 = $10,000 to less than $15,000 3 = $15,"
        "000 to less than $20,000 4 = $20,000 to less than $25,000 5 = $25,000 to less than $35,000 6 = $35,"
        "000 to less than $50,000 7 = $50,000 to less than $75,000 8 = $75,000 or more",
    }

    for i in questions:
        if i == "BMI":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(intUserInput)
            continue
        if i == "GenHlth":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(intUserInput)
            continue
        if i == "MentHlth":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(intUserInput)
            continue
        if i == "PhysHlth":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(intUserInput)
            continue
        if i == "Sex":

            def check_answer():
                answer = var.get()
                all_the_answers.append(answer)
                root.destroy()

            # Create the main window
            root = tk.Tk()
            root.title(i)

            # Create a variable to store the user's choice (True or False)
            var = tk.BooleanVar()

            # Create a label to display the question
            question_label = tk.Label(root, text=questions[i])
            question_label.pack(pady=10)
            root.geometry("500x500")
            # Create radio buttons for True and False
            true_radio = tk.Radiobutton(root, text="Male", variable=var, value=True)
            true_radio.pack()
            false_radio = tk.Radiobutton(root, text="Female", variable=var, value=False)
            false_radio.pack()
            # Create a button to submit the answer
            submit_button = tk.Button(root, text="Submit", command=check_answer)
            submit_button.pack(pady=10)

            # Start the main loop
            root.mainloop()
            continue
        if i == "Age":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(categorize_age(int(intUserInput)))
            continue
        if i == "Education":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(intUserInput)
            continue
        if i == "Income":
            root = Tk()
            root.withdraw()
            intUserInput = simpledialog.askinteger(title=i, prompt=questions[i])
            root.destroy()
            all_the_answers.append(intUserInput)
            continue

        def check_answer():
            answer = var.get()
            all_the_answers.append(answer)
            root.destroy()

        # Create the main window
        root = tk.Tk()
        root.title(i)

        # Create a variable to store the user's choice (True or False)
        var = tk.BooleanVar()

        # Create a label to display the question
        question_label = tk.Label(root, text=questions[i])
        question_label.pack(pady=10)
        root.geometry("500x500")
        # Create radio buttons for True and False
        true_radio = tk.Radiobutton(root, text="True", variable=var, value=True)
        true_radio.pack()

        false_radio = tk.Radiobutton(root, text="False", variable=var, value=False)
        false_radio.pack()

        # Create a button to submit the answer
        submit_button = tk.Button(root, text="Submit", command=check_answer)
        submit_button.pack(pady=10)

        # Start the main loop
        root.mainloop()
    return np.array(all_the_answers)
