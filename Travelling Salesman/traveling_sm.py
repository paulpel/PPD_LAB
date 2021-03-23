import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import random

cost_between_cities = []              #array of costs between each city
number_of_cities = 8                #set number of different cities

for i in range(number_of_cities):
    for j in range(number_of_cities):
        if i != j and j>i:
            cost_between_cities.append((i,j,round(random.uniform(1,10),4)))


for elem in cost_between_cities:
    print(elem)



