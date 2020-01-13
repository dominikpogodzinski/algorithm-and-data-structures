from collections import defaultdict


def swap_keys_with_elements(my_dict):
    keys = my_dict.keys()
    values = my_dict.values()

    l = list(zip(values, keys))

    d = defaultdict(list)
    for x, y in l:
        d[x].append(y)

    return dict(d)


print(swap_keys_with_elements({'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}))
