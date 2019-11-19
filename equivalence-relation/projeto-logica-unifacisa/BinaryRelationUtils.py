# coding: utf-8


class BinaryRelationUtils(object):
    """Class providing utilities to verify properties of a binary relation."""

    @staticmethod
    def verify_reflexivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is reflexive or not.
        Arguments:
        binary_relation - A subclass of the BinaryRelation class.
        input_set - A set closed under the binary relation.
        Return True if the binary relation in the given input set is reflexive
        or False if it is not.
        """
        # TODO: Replace line below with actual code.

        input_set_list = sorted(input_set)
        ho = binary_relation
        p = sorted(ho.relation(input_set))
        reflex = []
        for x, y in p:
            if x == y:
                reflex.append((x, y))

        if len(reflex) > 0:
            ultimo_valor = reflex[-1][0]
            if ultimo_valor == input_set_list[-1]:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def verify_symmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is symmetric or not.
        Arguments:
        binary_relation - A subclass of the BinaryRelation class.
        input_set - A set closed under the binary relation.
        Return True if the binary relation in the given input set is symmetric
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        cont = 0
        ho = binary_relation
        p = ho.relation(input_set)
        p = sorted(p)
        for x in p:
            par = (x[1], x[0])
            cont += 1 if (par in p) else 0

        if cont == len(p):
            return True
        else:
            return False

    @staticmethod
    def verify_transitivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is transitive or not.
        Arguments:
        binary_relation - A subclass of the BinaryRelation class.
        input_set - A set closed under the binary relation.
        Return True if the binary relation in the given input set is transitive
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        ho = binary_relation
        p = ho.relation(input_set)
        p = sorted(p)
        cont = 1
        cont2 = 1
        for x in range(len(p) - 1):
            if p[x][1] == p[x + 1][0]:
                cont2 += 1
                cont += 1 if ((p[x][0], p[x + 1][1]) in p) else 0
        if cont == cont2:
            return True
        else:
            return False

    @staticmethod
    def verify_antisymmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is antisymmetric or not.
        Arguments:
        binary_relation - A subclass of the BinaryRelation class.
        input_set - A set closed under the binary relation.
        Return True if the binary relation in the given input set is
        antisymmetric or False if it is not.
        """
        # TODO: Replace line below with actual code.
        ho = binary_relation
        p = ho.relation(input_set)
        p = sorted(p)
        cont = 1
        cont2 = 1

        for x in range(len(p) - 1):
            par = (p[x][1], p[x][0])
            if par in p:
                cont2 += 1
                cont += 1 if (p[x][0] == p[x][1]) else 0
        if cont == cont2:
            return True
        else:
            return False

    @staticmethod
    def verify_equivalency(binary_relation, input_set):
        """
        This method verifies if a given binary relation is an equivalence relation.
        Arguments:
        binary_relation - A subclass of the BinaryRelation class.
        input_set - A set closed under the binary relation.
        Return True if the binary relation in the given input set is
        an equivalence relation or False if it is not.
        """
        # TODO: Replace line below with actual code.

        relation = BinaryRelationUtils

        if relation.verify_reflexivity(binary_relation, input_set) and \
                relation.verify_symmetry(binary_relation, input_set) and \
                relation.verify_transitivity(binary_relation, input_set):
            return True
        else:
            return False

    @staticmethod
    def get_partitioning(binary_relation, input_set):
        """
        This method first verifies if binary relation is an equivalence relation and, if it is, generates a partitioning of the input set using the binary relation. If the binary relation is not an equivalence relation, it returns None.
        Note: The partitioning of the set should be a list of subsets.
        Arguments:
        binary_relation - A subclass of the BinaryRelation class.
        input_set - A set closed under the binary relation.
        Return None if the binary relation is not an equivalence relation or a partitioning of the input set (e.g.: [{1, 3, 5, ...}, {2, 4, 6, ...}]) if it is an equivalence relation.
        """
        # TODO: Replace line below with actual code.
        relation = BinaryRelationUtils
        ho = binary_relation
        tipo = str(ho)
        tipo = tipo[tipo.index('.')+1:tipo.index(' ')]
        p = ho.relation(input_set)
        p = sorted(p)

        if relation.verify_equivalency(binary_relation, input_set):
            if tipo == 'SameParityBinaryRelation':
                par = impar = set()
                partitioning = []
                for x, y in p:
                    if x % 2 == 0 and y % 2 == 0:
                        par.add((x, y))
                    elif x % 2 != 0 and y % 2 != 0:
                        impar.add((x, y))

                partitioning.append([par])
                partitioning.append([impar])

                return partitioning

            elif tipo == 'SameFirstLetterBinaryRelation':
                first_letter = sorted(input_set)[0][0]
                letters = {first_letter: set()}

                for x in sorted(input_set):
                    if x[0] != first_letter:
                        first_letter = x[0]
                        if first_letter not in letters.keys():
                            letters[first_letter] = set()

                for y in input_set:
                    if y[0] in letters.keys():
                        letters[y[0]].add(y)

                return letters.values()



        else:
            return None
