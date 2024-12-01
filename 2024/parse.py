'''
attribution: https://twitter.com/clemkeirua
https://blog.keiruaprod.fr/2021/11/23/getting-ready-for-adventofcode-in-python.html
'''

from typing import List

def input_as_string(filename:str) -> str:
    '''returns the content of the input file as a string'''
    with open(filename) as f:
        return f.read().rstrip('\n')

def input_as_lines(filename:str) -> List[str]:
    '''Return a list where each line in the input file is an element of the list'''
    return input_as_string(filename).split('\n')

def input_as_ints(filename:str) -> List[int]:
    '''Return a list where each line in the input file is an element of the list, converted into an integer'''
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def partition(arr, l, h, cmp_fn):
    piv = arr[h]
    ii = l - 1

    for jj in range(l, h):
        if cmp_fn(arr[jj], piv):
            ii += 1
            (arr[ii], arr[jj]) = (arr[jj], arr[ii])
    (arr[ii + 1], arr[h]) = (arr[h], arr[ii + 1])

    return ii + 1

def quicksort(arr, cmp_fn, l=0, h=None):
    if h is None:
        h = len(arr) - 1
    if l < h:
        piv = partition(arr, l, h, cmp_fn)
        quicksort(arr, cmp_fn, l, piv - 1)
        quicksort(arr, cmp_fn, piv + 1, h)
