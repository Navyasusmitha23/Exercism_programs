def flatten(iterable):
    lst = []
    for x in iterable:
        if type(x)==int:
           lst.append(x)
        elif type(x)==list:
            lst += flatten(x)
    return lst