# simulate relative grading
import utils
import pandas as pd, numpy as np

from utils import marks_normalizer, visualizer


def parse_integers_from_file(filepath):
    """
    Parses integers from a text file where each integer is
    in a new line as a String concatenated with a newline operator.

    :param filepath: The path to the text file
    :return: A list of integers
    """

    marks_list = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                # Remove the leading/trailing whitespace including the newline
                cleaned_line = line.strip()
                if cleaned_line:  # Ensure that the line is not empty after stripping
                    try:
                        marks_list.append(int(cleaned_line))
                    except ValueError:
                        print(f"Warning: Could not convert '{cleaned_line}' to an integer. Skipping.")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return marks_list

marks_list = parse_integers_from_file("input.txt")
# print(marks)
marks = np.array(marks_list)
percent = marks / 160 * 100

df = pd.DataFrame(columns = ["Percentage", "Deviation", "Grade Points", "Grade"])
df["Percentage"] = percent

mean = np.mean(percent)
sd = np.std(percent)

df["Deviation"] = percent - mean

# Normalize the score
grades = marks_normalizer(mean, sd, percent)

# Assign values to our main dataframe
df[["Grade Points", "Grade"]] = grades[["Grade Points", "Grade"]]

print(f"Sample Mean = {mean}, Sample SD = {sd}")
print(df)

# Visualisation
visualizer(percent, df["Grade Points"])