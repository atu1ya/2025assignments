# Name: YOUR NAME
# Student Number: 23XXXXXX

class Genealogy:
    """The genealogy and succession order for Envoy of the Kiktil."""

    def __init__(self, originator_name):
        """Constructs an initial genealogy containing no individuals other than
        the Originator.

        Args:
            originator_name: The name of the Originator of the Kiktil species.
        """
        pass

    def add_child(self, parent_name, child_name):
        """Adds a new child belonging to a given parent.

        You may assume the parent has previously been added as the child of
        another individual, and that no individual named `child_name` exists.

        Target Complexity: O(1) expected.

        Args:
            parent_name: The name of the parent individual.
            child_name: The name of their new child.
        """
        pass

    def get_primogeniture_order(self):
        """Returns the primogeniture succession order for Envoy of the Kiktil.

        By primogeniture, succession flows from parent to eldest child, only
        moving to the next youngest sibling after all their elder sibling's
        descendants.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Returns:
            A list of the names of individuals in primogeniture succession order
            starting with the Originator.
        """
        pass

    def get_seniority_order(self):
        """Returns the seniority succession order for Envoy of the Kiktil.

        Seniority order prioritizes proximity to the Originator, only moving on
        to a younger generation after every individual in the previous
        generations. Within a generation, older siblings come before younger,
        and cousins are prioritized by oldest different ancestor.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Returns:
            A list of the names of individuals in seniority succession order
            starting with the Originator.
        """
        pass

    def get_cousin_dist(self, lhs_name, rhs_name):
        """Determine the degree and removal of two cousins.

        The order of an individual relative to an ancestor is the number of
        generations separating them. So a child is order 0, a grandchild is
        order 1, and so on. For consistency, an individual has order -1 to
        themself.
        Consider the orders of two individuals relative to their most recent
        shared ancestor.
        The degree of the cousin relation of these individuals is the lesser of
        their orders.
        The removal of the cousin relation is the difference in their orders.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Args:
            lhs_name: The name of one cousin.
            rhs_name: The name of the other cousin.

        Returns:
            A pair `(degree, removal)` of the degree and removal of the cousin
            relation between the specified individuals.
        """
        pass
