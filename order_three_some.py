import itertools
import json

import numpy as np

import vertex_neighbors as vn
from Vertex import Vertex


def isAllTriosCanSwap(vertex):
    """
    :param: vertex, it has 2 bases we want to check. each base is dictionary
    :return: if every trio in base_a can be swap in any order with any trio in base_b
    """
    baseA = vertex.base_a.copy()
    baseB = vertex.base_b.copy()
    list_of_four_somes = itertools.combinations(baseA.keys(), 4)
    lst_of_legal_order_per_quartet = [] # list of tuples: (sub group of 4 vectors, how many legal orders of swap)
    for quartet in list_of_four_somes:
        lst_of_legal_order_per_quartet.append((quartet, isQuartetCanBeSwap(baseA, baseB, quartet)))
    return lst_of_legal_order_per_quartet


def isQuartetCanBeSwap(baseA, baseB, quartet):
    """
    :param: baseA is the base we want to check every order of the trio, in any order.
    :param: baseB is the base we want to swap the trio with.
    :param: quartet is tuple with 4 values (vector1, vector2, vector3, vector4).
            the vectors are subgroup from base_a that we want to try and swap
    :return: True if the qurtet has legal swap order with base_b, else False.
    """
    list_of_all_orders = itertools.permutations(quartet)
    num_of_legal_orders = 0
    for perm in list_of_all_orders:
        if isQuartetCanBeSwapHelper(baseA.copy(), baseB.copy(), perm, 0):
            num_of_legal_orders += 1
    return num_of_legal_orders


def isQuartetCanBeSwapHelper(baseA, baseB, perm, perm_index):
    dim = len(baseA)
    if perm_index == len(perm):
        return True
    for vecB in baseB.keys():
        if baseB[vecB]:
            continue
        tmpBaseA, tmpBaseB = vn.swapVec(baseA, baseB, perm[perm_index], vecB)
        if vn.isBase(baseA.keys(), dim) and vn.isBase(baseB.keys(), dim):
            if isQuartetCanBeSwapHelper(tmpBaseA, tmpBaseB, perm, perm_index + 1):
                return True
    return False


def main():
    baseI = {"10000": False, "01000": False, "00100": False, "00010": False, "00001": False}
    # baseB = {"01010": False, "01111": False, "10000": False, "10111": False, "11110": False}
    f = open('bases_5.json')
    res = open('result.txt', 'w')
    data = json.load(f)
    min_all_orders_for_sub_group_len_4 = np.inf
    min_sub_group_len_4 = None
    for base in data:
        lst = isAllTriosCanSwap(Vertex(base, baseI, 5))
        lst.sort(key=lambda x: x[1])
        min_order_for_vertex = lst[0][1]
        min_sub_group_for_vertex = lst[0][0]
        line = str(min_order_for_vertex) + ", " + str(min_sub_group_for_vertex) + '\n'
        res.write(line)
        if min_order_for_vertex < min_all_orders_for_sub_group_len_4:
            min_all_orders_for_sub_group_len_4 = min_order_for_vertex
            min_sub_group_len_4 = min_sub_group_for_vertex
    print(min_sub_group_len_4, min_all_orders_for_sub_group_len_4)


main()

