"""
Function to call the different function generators.
Edit the appropriate parameters and uncomment the appropriate call for execution.
"""
from marks_generators import uniform_generator, normal_generator, skewed_generator, \
    bimodal_generator

# values
number_of_marks = 100
seed = None
plot = True
# for uniform
lower_limit = 50
upper_limit = 90
# for normal
mean = 40
sd = 10
# for skewed
success_proportion = 0.75
failure_proportion = 1.75
# for bimodal
mean1 = 30
sd1 = 8
mean2 = 70
sd2 = 8

# function calls
# uniform_generator(n=number_of_marks, seed=seed, plot=plot)
# normal_generator(n=number_of_marks, mean=mean, sd=sd, seed=seed, plot=plot)
skewed_generator(n=number_of_marks, success_proportion=success_proportion, failure_proportion=failure_proportion, seed=seed, plot=plot)
# bimodal_generator(n=number_of_marks, mean1=mean1, sd1=sd1, mean2=mean2, sd2=sd2, seed=seed, plot=plot)