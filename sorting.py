import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
def selection_sort(numbers):
    numbers = numbers[:]
    for pozice_ukladani in range (len(numbers)):
        min_indx= pozice_ukladani
        for pozice_hledani in range(pozice_ukladani + 1, len(numbers)):
            if numbers[pozice_hledani] < numbers[min_indx]:
                min_indx= pozice_hledani
    numbers[pozice_ukladani], numbers[min_indx] = numbers[min_indx], numbers[pozice_ukladani]
    return numbers


def main(numbers):
    numbers= [5, 1, 4, 2, 8]
    print("Původní seznam:", numbers)
    print("seřazený seznam:", selection_sort(numbers))

def bubble_sort(numbers):
    numbers= numbers[:]
    num= len(numbers)
    plt.ion()
    plt.show()
    for i in range(num):
        for j in range(0, num - i - 1):
            if nums[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
        index_highlight1 = j
        index_highlight2 = j + 1
        colors = ["steelblue"] * len(values)
        colors[index_highlight1] = "tomato"
        colors[index_highlight2] = "tomato"
        plt.clf()
        plt.bar(range(len(values)), values, color=colors)
        plt.title("Bubble Sort")
        plt.pause(0.1)
    plt.ion()
    plt.show()