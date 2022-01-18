import numpy as np
import Global_funcs_Trees
from Vertex import Vertex
from binmatrix import BinMatrix


def isBase(list_of_strings, dim):
    """
    :param list_of_strings: represents list of vectors which given in strings.
    the func convert the vectors to int.
    :return: true if the list represent a linear space base.
    """

    if len(list_of_strings) != dim: # case: 2 same vectors (keys) in base so dictionary size will be dim-1 (same keys)
        return False
    int_base = []
    for string in list_of_strings:
        row = [int(x) for x in string]
        int_base.append(row)
    matrix_base = BinMatrix(int_base)
    return matrix_base.is_base()


def swapVec(baseA, baseB, vecA, vecB):
    newBaseA = {}
    newBaseB = {}
    for vec in baseA:
        if vec != vecA:
            newBaseA[vec] = baseA[vec]
        else:
            newBaseA[vecB] = True
    for vec in baseB:
        if vec != vecB:
            newBaseB[vec] = baseB[vec]
        else:
            newBaseB[vecA] = True
    return newBaseA, newBaseB


def get_neighbours(vertex, sourceVertex=None):
    # Assumption - base given in list of strings
    neighbours = []
    baseA = vertex.base_a.copy()
    baseB = vertex.base_b.copy()
    foundSwappedVertex = False
    dim = len(baseB.keys())
    for a_vec, a_switched in baseA.items():
        if a_switched:
            continue
        for b_vec, b_switched in baseB.items():
            if b_switched:
                continue
            tmpbaseA, tmpbaseB = swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(tmpbaseA.keys(), dim) and isBase(tmpbaseB.keys(), dim):
                neighbours.append(Vertex(tmpbaseA, tmpbaseB, dim))
                if sourceVertex is not None:
                    if sourceVertex.base_a == tmpbaseB and sourceVertex.base_b == tmpbaseA:
                        foundSwappedVertex = True
                        break
        if foundSwappedVertex:
            break
    return neighbours if sourceVertex is None else (neighbours, foundSwappedVertex)


def is2BasesCanSwap(vertex):
    baseA = vertex.base_a
    baseB = vertex.base_b
    layer = 1
    dim = len(vertex)
    foundSwappedVertex = False
    currentLayerNeighbours, foundSwappedVertex = get_neighbours(vertex)
    while layer < dim:
        currentLayerNeighbours, foundSwappedVertex = get_neighbours(vertex, foundSwappedVertex)
        if foundSwappedVertex:
            return layer
        layer += 1
    return layer


def nextLayersNeighbours(array_of_layer):
    neighbours = []
    for vertex in array_of_layer:
        neighbours += get_neighbours(vertex)
    return neighbours
