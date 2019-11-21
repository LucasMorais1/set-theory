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

        p = binary_relation.relation(input_set)
        ReflexivityCases = 0
        for x, y in p:
            if x == y:
                ReflexivityCases += 1
        if ReflexivityCases == len(input_set):
            return True
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
        p = binary_relation.relation(input_set)
        SymmetryCases = 0
        for x, y in p:
            SymmetryCases += 1 if ((y, x) in p) else 0

        if SymmetryCases == len(p):
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
        p = sorted(binary_relation.relation(input_set))
        NumTransitivity = 1
        NumCasesRule1 = 1
        for x in range(len(p) - 1):
            if p[x][1] == p[x + 1][0]:
                NumCasesRule1 += 1
                NumTransitivity += 1 if ((p[x][0], p[x + 1][1]) in p) else 0
        if NumTransitivity == NumCasesRule1:
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
        p = binary_relation.relation(input_set)
        CasesAntiSymmetric = 1
        NumInverses = 1
        for x, y in p:
            if (y, x) in p:
                NumInverses += 1
                CasesAntiSymmetric += 1 if (x == y) else 0
        if CasesAntiSymmetric == NumInverses:
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
        p = binary_relation.relation(input_set)
        partitions = []
        possui_equivalencia = BinaryRelationUtils.verify_equivalency(binary_relation, input_set)
        if possui_equivalencia:
            for x in sorted(input_set):
                part = set()
                for y in input_set:
                    if (x, y) in p:
                        part.add(y)
                if part not in partitions:
                    partitions.append(part)
            return partitions
        else:
            return None
