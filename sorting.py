import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
def selection_sort(numbers):
    numbers = [:]
    for pozice_ukladani in range (len(numbers)):
        min_indx= pozice_ukladani
        for pozice_hledani in range(pozice_ukladani + 1, len(numbers)):
            if numbers[pozice_hledani] < numbers[min_indx]:
                min_indx= pozice_hledani
    numbers[pozice_ukladani], numbers[min_indx] = numbers[min_indx], numbers[pozice_ukladani]
    return numbers


def main(numbers)
numbers= [5, 1, 4, 2, 8]
print("Původní seznam:", numbers)
print("seřazený seznam:", selection_sort(numbers))

