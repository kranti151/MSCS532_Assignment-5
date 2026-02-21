"""
Assignment 5 - Quicksort Implementation
Komalben Suthar

"""

import random
import time


# ======================================================
# Deterministic Quicksort (First Element as Pivot)
# ======================================================

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def deterministic_quicksort(arr, low, high):
    while low < high:
        pivot_index = partition(arr, low, high)

        # Recurse on smaller side first
        if pivot_index - low < high - pivot_index:
            deterministic_quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            deterministic_quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1

# ======================================================
# Randomized Quicksort
# ======================================================

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[low], arr[random_index] = arr[random_index], arr[low]
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


# ======================================================
# Benchmarking
# ======================================================

def benchmark(sort_func, arr):
    start = time.time()
    sort_func(arr, 0, len(arr) - 1)
    return time.time() - start


if __name__ == "__main__":
    sizes = [1000, 5000, 10000]

    for n in sizes:
        random_arr = [random.randint(1, n) for _ in range(n)]
        sorted_arr = list(range(n))
        reverse_arr = list(range(n, 0, -1))

        print(f"\nArray Size: {n}")

        print("Deterministic (Random):",
              benchmark(deterministic_quicksort, random_arr.copy()))
        print("Randomized (Random):",
              benchmark(randomized_quicksort, random_arr.copy()))

        print("Deterministic (Sorted):",
              benchmark(deterministic_quicksort, sorted_arr.copy()))
        print("Randomized (Sorted):",
              benchmark(randomized_quicksort, sorted_arr.copy()))

        print("Deterministic (Reverse):",
              benchmark(deterministic_quicksort, reverse_arr.copy()))
        print("Randomized (Reverse):",
              benchmark(randomized_quicksort, reverse_arr.copy()))