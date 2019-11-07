def quick_sort(list):
    mniejsze = []
    rowne = []
    wieksze = []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x > pivot:
                wieksze.append(x)
            elif x == pivot:
                rowne.append(x)
            else:
                mniejsze.append(x)
        return quick_sort(mniejsze) + rowne + quick_sort(wieksze)
    else:
        return list


if __name__ == "__main__":
    li = [1, 9, 8, 5, 7, 3, 3, 2, 4]

    print("Lista przed sortowaniem: {}".format(li))
    result = quick_sort(li)
    print("Lista po sortowaniu: {}".format(result))

    assert result == [1, 2, 3, 3, 4, 5, 7, 8, 9], "Lista nie jest posortowana!"
