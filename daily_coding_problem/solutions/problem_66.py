# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

# Write a function to simulate an unbiased coin toss.

from random import random

def toss_biased():
    rand = random()
    if rand < 0.7:
        coin_toss = 0
    else:
        coin_toss = 1
    return coin_toss

num_of_experiments = 100000

results_biased = {  0: 0, 
                    1: 0
                }
results_unbiased = {    0: 0, 
                        1: 0
                    }

for i in range(num_of_experiments):
    flip = toss_biased()
    results_biased[flip] += 1

#print(results_biased)
for key in results_biased:
    results_biased[key] /= num_of_experiments
    results_biased[key] = round(results_biased[key], 2)

print(results_biased)

assert results_biased[0] == 0.7
assert results_biased[1] == 0.3