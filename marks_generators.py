import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def uniform_generator(n=100, lower_limit=0, upper_limit=160, seed=None, plot=False):
    """
    Function to generate random integer marks within a limit
    and return them to a text file as an integer in each line (in string format).

    :param n: no. of marks to be generated
    :param lower_limit: lower limit
    :param upper_limit: upper limit
    :param seed: random seed for reproducibility
    :param plot: whether to show KDE plot of the generated data
    :return: none
    """
    marks = []

    if seed is not None:
        np.random.seed(seed)

    for i in range(n):
        marks.append(random.randint(lower_limit, upper_limit))

    with open("input.txt", "w") as file:
        for mark in marks:
            file.write(f"{mark}\n")

        file.close()

        # Optional plot section
        if plot:
            sns.kdeplot(marks, fill=True)
            plt.title(f"Uniform Distribution of Marks (a={lower_limit}, b={upper_limit})")
            plt.xlabel("Marks")
            plt.ylabel("Density")
            plt.xlim(0, 160)
            plt.grid(True)
            plt.show()

def normal_generator(n=100, mean=70, sd=10, seed=None, plot=False):
    """
    Function to generate random integer marks from a normal distribution
    and return them to a text file as an integer in each line (in string format).

    :param n: no. of marks to be generated
    :param mean: mean of the normal distribution
    :param sd: standard deviation of the normal distribution
    :param lower_limit: lower limit
    :param upper_limit: upper limit
    :param seed: random seed for reproducibility
    :param plot: whether to show KDE plot of the generated data
    :return: none
    """
    if seed is not None:
        np.random.seed(seed)

    # Generate and clip to the integer range 0–100 (optional safeguard)
    marks = np.random.normal(loc=mean, scale=sd, size=n)
    marks = np.clip(marks, a_min=0, a_max=160).astype(int)  # Convert to integer marks

    # Write to input.txt
    with open("input.txt", "w") as file:
        for mark in marks:
            file.write(f"{mark}\n")

        file.close()

    # Plot the distribution
    if plot:
        sns.kdeplot(marks, fill=True)
        plt.title(f"Normal Distribution of Marks (mean={mean}, sd={sd})")
        plt.xlabel("Marks")
        plt.ylabel("Density")
        plt.xlim(0, 160)
        plt.grid(True)
        plt.show()

def skewed_generator(n=100, success_proportion=5, failure_proportion=2, seed=None, plot=False):
    """
    Function to generate skewed integer marks within a limit
    and return them to a text file as an integer in each line (in string format).

    :param n: no. of marks to be generated
    :param lower_limit: lower limit
    :param upper_limit: upper limit
    :param success_proportion: proportion of successes in the result set
    :param failure_proportion: proportion of failures in the result set
    :param seed: random seed for reproducibility
    :param plot: whether to show KDE plot of the generated data
    :return: none
    """
    if seed is not None:
        np.random.seed(seed)

    # Generate left-skewed values using beta distribution
    # Beta(5, 2) → skewed to the left (more high values)
    beta_values = np.random.beta(a=success_proportion, b=failure_proportion, size=n)
    marks = (beta_values * (160 - 0) + 0).astype(int)

    # Write to file
    with open("input.txt", "w") as file:
        for mark in marks:
            file.write(f"{mark}\n")

    # Optional plot section
    if plot:
        sns.kdeplot(marks, fill=True)
        plt.title("Skewed Distribution of Marks")
        plt.xlabel("Marks")
        plt.ylabel("Density")
        plt.xlim(0, 160)
        plt.grid(True)
        plt.show()

def bimodal_generator(n=100, mean1= 30, sd1=8, mean2=70, sd2=8, seed=None, plot=False):
    """
    Function to generate bimodal integer marks within a limit
    and return them to a text file as an integer in each line (in string format).

    :param n: no. of marks to be generated
    :param lower_limit: lower limit
    :param upper_limit: upper limit
    :param mean1: mode of the first bell
    :param sd1: standard deviation of the first bell
    :param mean2: mode of the second bell
    :param sd2: standard deviation of the second bell
    :param seed: random seed for reproducibility
    :param plot: whether to show KDE plot of the generated data
    :return: none
    """
    if seed is not None:
        np.random.seed(seed)

    # Half the samples around first mode (~30), half around second mode (~70)
    n1, n2 = n // 2, n - (n // 2)

    group1 = np.random.normal(loc=mean1, scale=sd1, size=n1)
    group2 = np.random.normal(loc=mean2, scale=sd2, size=n2)

    # Combine, clip to [a, b], and convert to int
    marks = np.concatenate([group1, group2])
    marks = np.clip(marks, 0, 160).astype(int)

    # Write to file
    with open("input.txt", "w") as file:
        for mark in marks:
            file.write(f"{mark}\n")

    # Optional plot section
    if plot:
        sns.kdeplot(marks, fill=True)
        plt.title("Bimodal Distribution of Marks")
        plt.xlabel("Marks")
        plt.ylabel("Density")
        plt.xlim(0, 160)
        plt.grid(True)
        plt.show()
