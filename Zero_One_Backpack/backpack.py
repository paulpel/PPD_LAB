from random import randint
import sys

#zwraca listę z objętością
def volume_items(quantity):
    return [randint(1,100) for value in range(quantity)]

#zwraca listę z wartością
def value_items(quantity):
    return [randint(50,300) for value in range(quantity)]

#sprawdzenie ograniczenia 1, czy suma objetosci rzeczy  jest wieksza od objetosci plecaka
def constraint_1(capacity, item_vol):
    if sum(item_vol) > capacity:
        return True
    else:
        return False

#sprawdzenie ograniczenia 2, czy kazdy element ma z osobna mniejsza objetosc od pojemnosci
def constraint_2(capacity, item_vol):
    passed = True
    for elem in item_vol:
        if elem < capacity:
            passed = True
        else:
            passed = False
            return passed
    return passed

#zwraca największą wartość możliwą do uzyskania bez powtarzania elementów
def knapSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]

#zwraca największą wartość możliwą do uzyskania z powtarzaniem elementów
def unboundedKnapsack(W, val, wt):
    n = len(val)
    table = [0 for i in range(W + 1)]

    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                table[i] = max(table[i], table[i - wt[j]] + val[j])

    return table[W]


capacity_backpack = 100
number_of_items = 10
volume_of_i_elem = volume_items(number_of_items)
value_of_i_elem = value_items(number_of_items)
