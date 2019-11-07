# -*- coding: utf-8 -*-
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1


def print_list(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()


if __name__ == "__main__":
    lista = [1, 9, 8, 5, 7, 3, 3, 2, 4]
    print("Lista przed sortowaniem:", lista)
    merge_sort(lista)
    print("Lista po sortowaniu:", lista)
