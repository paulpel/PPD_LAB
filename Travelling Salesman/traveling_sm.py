import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import random

# create  list of costs between each city
def create_data(n_of_cities):
    cost_between_cities = []  # array of costs between each city
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if i != j and j > i:
                cost_between_cities.append((i, j, round(random.uniform(1, 10), 4)))

    return  cost_between_cities

def display_stages():
    cost = 0
    for k in range(len(best_order) - 1):
        if best_order[k + 1] > best_order[k]:
            temp = [best_order[k], best_order[k + 1]]
        else:
            temp = [best_order[k + 1], best_order[k]]

        for elem in cost_between_cities:
            if elem[0] == temp[0] and elem[1] == temp[1]:
                print(f"Cost between {elem[0]} and {elem[1]} is {elem[2]}")
                cost += elem[2]

    if best_order[0] < best_order[-1]:
        temp = [best_order[0], best_order[-1]]

    else:
        temp = [best_order[-1], best_order[0]]

    for elem in cost_between_cities:
        if elem[0] == temp[0] and elem[1] == temp[1]:
            print(f"Cost between {elem[0]} and {elem[1]} is {elem[2]}")
            cost += elem[2]
    print(f"Total cost is {cost}")

number_of_cities = 8                #set number of different cities
cost_between_cities = create_data(number_of_cities)
print("INPUT DATA:")
print(cost_between_cities)

for elem in cost_between_cities:
    print(f"Cost between city {elem[0]} and {elem[1]} is {elem[2]}")

#creating an object
fitness_dists = mlrose.TravellingSales(distances = cost_between_cities)

#length - how many cities, maximize - determines if we want to max or min function
problem_fit = mlrose.TSPOpt(length = 8, fitness_fn = fitness_dists,maximize=False)

best_order, cheapest_cost = mlrose.genetic_alg(problem_fit, random_state = 2)

print("\nRESULT:")
print('The best order to visit cities is: ', best_order)

print('The minimum cost is : ', cheapest_cost)

display_stages()





