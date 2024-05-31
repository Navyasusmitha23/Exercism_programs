def append(list1, list2):
    return list1+list2

def concat(lists):
    r = []
    for list in lists:
        r += list
    return r
        


def filter(function, list):
    r = []
    for item in list:
        if function(item):
           r.append(item)
    return r
    


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    r = []
    for item in list:
        r.append(function(item))
    return r

def foldl(function, list, initial):
    for item in list:
        initial = function(initial,item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial,item)
    return initial


def reverse(list):
    return list[::-1]
