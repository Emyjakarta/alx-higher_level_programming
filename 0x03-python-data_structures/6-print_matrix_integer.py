#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0] == []:
        print()
    for out in matrix:
        for index, element in enumerate(out):
            if index == len(out) - 1:
                print("{}".format(element))
            else:
                print("{} ".format(element), end="")
