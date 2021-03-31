from random import randint
import sys

class Backpack:
    '''Klasa do opisania problemu plecakowego'''

    def __init__(self):
        '''Inicjalizacja zmiennych'''
        self.settings = Settings()
        self.capacity = self.settings.capacity_of_backpack
        self.number_of_items = self.settings.number_of_items
        self.list_of_values = self.settings.list_of_values
        self.list_of_volumes = self.settings.list_of_volumes

    # zwraca największą wartość możliwą do uzyskania bez powtarzania elementów
    def knapSack(self):
        n = len(self.list_of_values)
        table = [[0 for x in range(self.capacity + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for j in range(self.capacity + 1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif self.list_of_volumes[i - 1] <= j:
                    table[i][j] = max(self.list_of_values[i - 1] + table[i - 1][j - self.list_of_volumes[i - 1]], table[i - 1][j])
                else:
                    table[i][j] = table[i - 1][j]

        return table[n][self.capacity]

    # zwraca największą wartość możliwą do uzyskania z powtarzaniem elementów
    def unboundedKnapsack(self):
        n = len(self.list_of_values)
        table = [0 for i in range(self.capacity + 1)]

        for i in range(self.capacity + 1):
            for j in range(n):
                if (self.list_of_volumes[j] <= i):
                    table[i] = max(table[i], table[i - self.list_of_volumes[j]] + self.list_of_values[j])

        return table[self.capacity]

    # sprawdzenie ograniczenia 1, czy suma objetosci rzeczy  jest wieksza od objetosci plecaka
    def constraint_1(self):
        if sum(self.list_of_volumes) > self.capacity:
            return True
        else:
            return False

    # sprawdzenie ograniczenia 2, czy kazdy element ma z osobna mniejsza objetosc od pojemnosci
    def constraint_2(self):
        passed = True
        for elem in self.list_of_volumes:
            if elem < self.capacity:
                passed = True
            else:
                passed = False
                return passed
        return passed

    def run_problem(self):
        #informacje o danych
        self.settings.print_info()
        #problem ograniczony
        if self.settings.limited_items == True:
            #sprawdzenie ograniczeń
            if self.constraint_1() == True and self.constraint_2() == True:
                print('\nOgraniczenia spełnione.')
                print(f'Maksymalna wartość jaką zmieścimy w plecaku przy problemie z ograniczoną ilościa rzeczy to: {self.knapSack()}')
            else:
                print('\nOgraniczenia nie spełnione.')
                sys.exit()
        elif self.settings.limited_items == False:
            if self.constraint_2() == True:
                print('\nOgraniczenia spełnione.')
                print(f'Maksymalna wartość jaką zmieścimy w plecaku przy problemie z nieograniczoną ilościa rzeczy to: {self.unboundedKnapsack()}')
            else:
                print('\nOgraniczenia nie spełnione.')
                sys.exit()
        else:
            print('\nNiesprecyzowano czy problem ma być ograniczony czy nieograniczony')





class Settings:
    '''Klasa zawierająca ustawienia'''

    def __init__(self):
        self.number_of_items = 10
        self.capacity_of_backpack = 100
        self.volume_range = (1,99)
        self.value_range = (50,300)
        self.limited_items = False
        self.list_of_volumes = self.volume_items()
        self.list_of_values = self.value_items()

    # zwraca listę z objętością
    def volume_items(self):
        return [randint(self.volume_range[0], self.volume_range[1]) for value in range(self.number_of_items)]

    # zwraca listę z wartością
    def value_items(self):
        return [randint(self.value_range[0], self.value_range[1]) for value in range(self.number_of_items)]

    def print_info(self):
        print('Informacje o danych wejściowych.')
        print("Tabela wartości: " + str(self.list_of_values))
        print('Tabela objętości: ' + str(self.list_of_volumes))
        print('Pojemność plecaka: ' + str(self.capacity_of_backpack))

if __name__ == '__main__':
    #Utworzenie egzemplarza i uruchomienie
    bp = Backpack()
    bp.run_problem()