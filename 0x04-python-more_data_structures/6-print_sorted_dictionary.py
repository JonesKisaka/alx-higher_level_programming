#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, v in sorted(a_dictionary.items()):
        print("{0}: {1}".format(i, v))
