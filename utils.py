# generate marks for our simulation
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def marks_generator(n, a, b):
    """
    Function to generate random integer marks within a limit
    and return them to a text file as an integer in each line (in string format).

    :param n: no. of marks to be generated
    :param a: lower limit
    :param b: upper limit
    :return: none
    """
    marks = []

    for i in range(n):
        marks.append(random.randint(a, b))

    with open("input.txt", "w") as file:
        for mark in marks:
            file.write(f"{mark}\n")

        file.close()

    # return marks

def marks_normalizer(mean, sd, percent):
    """
    Function to normalize the marks of the students into grades based on
    the mean and standard deviation of the sample.
    Rule followed by the University of Delhi.

    :param mean: sample mean (percentages)
    :param sd: sample sd (percentages)
    :param percent: numpy array of percentage of obtained marks
    :return grades: data frame containing normalized grades (number and letter)
    """

    grades = pd.DataFrame(columns = ["Grade Points", "Grade"])

    # Apply normaliztion logic
    for i, percentage in enumerate(percent):
        if percentage >= min(mean + 2.5 * sd, 90):
            grades.loc[i, "Grade Points"] = 10
            grades.loc[i, "Grade"] = "O"
        elif percentage >= min(mean + 2.0 * sd, 80):
            grades.loc[i, "Grade Points"] = 9
            grades.loc[i, "Grade"] = "A+"
        elif percentage >= min(mean + 1.5 * sd, 70):
            grades.loc[i, "Grade Points"] = 8
            grades.loc[i, "Grade"] = "A"
        elif percentage >= min(mean + 1.0 * sd, 60):
            grades.loc[i, "Grade Points"] = 7
            grades.loc[i, "Grade"] = "B+"
        elif percentage >= min(mean, 50):
            grades.loc[i, "Grade Points"] = 6
            grades.loc[i, "Grade"] = "B"
        elif percentage >= min(mean - 0.5 * sd, 40):
            grades.loc[i, "Grade Points"] = 5
            grades.loc[i, "Grade"] = "C"
        elif percentage >= min(mean - 1.0 * sd, 30):
            grades.loc[i, "Grade Points"] = 4
            grades.loc[i, "Grade"] = "D"
        else:
            grades.loc[i, "Grade Points"] = 0
            grades.loc[i, "Grade"] = "F"

    return grades

def visualizer(percent, grade_points):
    # Step 1: Preprocess grade points
    grade_points_clean = grade_points.copy()
    grade_points_clean = grade_points_clean.apply(lambda x: 3 if x < 4 else x)

    # Step 2: Grade point frequency smoothing
    possible_grades = np.arange(3, 11)
    grade_counts = grade_points_clean.value_counts().reindex(possible_grades, fill_value=0).sort_index()

    # Step 3: Plotting
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Smooth curve for percentage using KDE
    sns.kdeplot(percent, fill=True, ax=axes[0, 0], bw_adjust=1)
    axes[0, 0].set_title("Smoothed Percentage Distribution")
    axes[0, 0].set_xlabel("Percentage (%)")
    axes[0, 0].set_ylabel("Density")
    axes[0, 0].set_xlim(-5, 105)  # One interval before and after

    # Plot 2: Smoothed grade frequency using a line plot
    axes[1, 1].plot(possible_grades, grade_counts.values, marker='o', linestyle='-', color='orange')
    axes[1, 1].set_title("Grade Points Distribution (Smoothed Line)")
    axes[1, 1].set_xlabel("Grade Points")
    axes[1, 1].set_ylabel("Number of Students")
    axes[1, 1].set_xticks(possible_grades)
    axes[1, 1].set_xlim(2, 11)

    # Plot 3: Smooth density curve for grade frequency using KDE
    sns.kdeplot(grade_points_clean, fill=True, ax=axes[1, 0], bw_adjust=0.5, clip=(2, 11))
    axes[1, 0].set_title("Smoothed Grade Points Distribution")
    axes[1, 0].set_xlabel("Grade Points")
    axes[1, 0].set_ylabel("Density")
    axes[1, 0].set_xlim(2, 11)

    plt.tight_layout()
    plt.show()