from numpy import inf as inf_value


class Vertex:

    def __init__(self, base_a, base_b, dim, v_id='NA'):
        self.base_a = self.init_base_from_input(base_a, dim)
        self.base_b = self.init_base_from_input(base_b, dim)
        self.dv = inf_value
        self.v_id = v_id
        self.near_lst = []  # neighbours list

    def init_base_from_input(self, base, dim):
        if isinstance(base, dict):
            return base
        if isinstance(base, str):
            num_of_vectors = (len(base)+dim-1)//dim
            step = dim
            base = [base[i: i+step] for i in range(0, num_of_vectors*step, step)]
        if isinstance(base, list):
            return {vector: False for vector in base}

    def equals(self, other_vertex):
        base_a_vectors = self.base_a.keys()
        base_b_vectors = self.base_b.keys()
        other_base_a_vectors = other_vertex.base_a.keys()
        other_base_b_vectors = other_vertex.base_b.keys()
        # print(f'base_a_vectors = {set(base_a_vectors)}, other_base_a_vectors = {set(other_base_a_vectors)}')
        # print(f'base_b_vectors = {set(base_b_vectors)}, other_base_b_vectors = {set(other_base_b_vectors)}')
        return base_a_vectors == other_base_a_vectors and base_b_vectors == other_base_b_vectors

    def add_neighbour(self, new_neighbour):
        self.near_lst.append(new_neighbour)

    def get_dv(self):
        return self.dv

    def set_dv(self, d):
        self.dv = d

    def get_base_to_print(self, a_or_b):
        base = self.base_a if a_or_b == 'a' else self.base_b
        return '\n'.join(base.keys())

    def __str__(self):
        return f"Vertex with id {self.v_id}, neighbours = {[neighbour.v_id for neighbour in self.near_lst]}\n" \
               f"baseA = \n{self.get_base_to_print('a')}\n" \
               f"baseB = \n{self.get_base_to_print('b')}\n"

    def __repr__(self):
        return self.__str__()


"""
Vertex example:
    vertex.base_a = {vector0: switched(True/False),  vector1: switched(True/False) ... }
    vertex.base_b = {vector0: switched(True/False),  vector1: switched(True/False) ... }
    vertex.id = running index from 0 that increasing every Vertex creation
    vertex.dv = infinity_value  # prepare for BFS
    vertex.near_lst = [vertex1, vertex2, vertex3..]  # neighbour list
"""