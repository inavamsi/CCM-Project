'''
This file can be used to figure out a correct varaiance value to generate data with constarints on expectation on numbe rof pure sequences and nosiy sequences.
'''

from scipy.stats import norm
import numpy as np
import random

len_l=5
var=0.66


c1 = norm.cdf(1, loc=0, scale=var)
c_1=norm.cdf(-1, loc=0, scale=var)


print("Probability of noise for a given element of sequence : ",1 - c1+c_1)
print("Expected number of sequences of length ",len_l," with no error : ",pow(c1-c_1,len_l))
