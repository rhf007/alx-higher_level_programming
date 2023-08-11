#!/usr/bin/python3
def no_c(my_string):
    copy = [i for i in my_string]
    for j in copy[:]:
        if j == 'c' or j == 'C':
            copy.remove(j)
    return ''.join(copy)
