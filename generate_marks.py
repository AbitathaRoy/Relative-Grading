"""
Function to call the different function generators.
Edit the appropriate parameters and uncomment the appropriate call for execution.
"""
from marks_generators import uniform_generator, normal_generator, skewed_generator, \
    bimodal_generator

# values
number_of_marks = 1000
seed = None
plot = True
# for uniform
lower_limit = 90
upper_limit = 150
# for normal
mean = 90
sd = 15
# for skewed
success_proportion = 1.2
failure_proportion = 1.8
# for bimodal
mean1 = 32
sd1 = 8
mean2 = 140
sd2 = 8

# function calls
# uniform_generator(n=number_of_marks, lower_limit=lower_limit, upper_limit=upper_limit, seed=seed, plot=plot)
# normal_generator(n=number_of_marks, mean=mean, sd=sd, seed=seed, plot=plot)
# skewed_generator(n=number_of_marks, success_proportion=success_proportion, failure_proportion=failure_proportion, seed=seed, plot=plot)
bimodal_generator(n=number_of_marks, mean1=mean1, sd1=sd1, mean2=mean2, sd2=sd2, seed=seed, plot=plot)