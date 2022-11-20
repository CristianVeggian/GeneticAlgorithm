def utilTupla(tupla, pos, item):
    my_list = list(tupla)
    my_list[pos] = item
    return tuple(my_list)