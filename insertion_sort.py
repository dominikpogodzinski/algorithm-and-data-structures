def insertion_sort(list):
    for i in range(1, len(list) - 1):
        j = i
        while list[j] > list[j + 1] and j > -1:
            list[j], list[j + 1] = list[j + 1], list[j]
            j -= 1
        print(list)

    return list


if __name__ == "__main__":
    li = [1, 9, 8, 5, 7, 3]

    print("List before sorting: {}".format(li))
    result = insertion_sort(li)

    print("List after sorting: {}".format(result))
