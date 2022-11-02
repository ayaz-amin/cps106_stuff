def selection_sort(unsorted_array):
    sorted_array = []
    for i in range(len(unsorted_array)):
        min_elem = unsorted_array[0]
        min_idx = 0
        for j, elem in enumerate(unsorted_array):
            if elem < min_elem:
                min_elem = elem
                min_idx = j
        sorted_array.append(min_elem)
        unsorted_array.pop(min_idx)
    return sorted_array

if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))