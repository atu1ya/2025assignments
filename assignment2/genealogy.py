# Name: ATULYA CHATURVEDI
# Student Number: 24225113

class _Individual:
    """Represents an individual in the genealogy."""
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []  # Store children in order of addition (eldest first)

class Genealogy:
    """Manages the genealogy and succession order for Envoy of the Kiktil."""

    def __init__(self, originator_name):
        """
        Initializes the genealogy with the Originator as the root.

        Args:
            originator_name (str): The name of the Originator of the Kiktil species.
        """
        self.originator = _Individual(originator_name)
        self.individuals = {originator_name: self.originator}

    def add_child(self, parent_name, child_name):
        """
        Adds a new child to the genealogy under the specified parent.

        Args:
            parent_name (str): The name of the parent individual.
            child_name (str): The name of the new child.
        """
        parent_node = self.individuals[parent_name]
        child_node = _Individual(child_name, parent=parent_node)
        parent_node.children.append(child_node)
        self.individuals[child_name] = child_node

    def get_primogeniture_order(self):
        """
        Returns the primogeniture succession order.

        Primogeniture succession flows from parent to eldest child, moving to
        the next youngest sibling only after all elder siblings' descendants.

        Returns:
            list: Names of individuals in primogeniture succession order.
        """
        order = []
        stack = [self.originator]  # Use a stack for depth-first traversal

        while stack:
            current = stack.pop()
            order.append(current.name)
            # Add children in reverse order so eldest is processed first
            stack.extend(reversed(current.children))
        return order

    def get_seniority_order(self):
        """
        Returns the seniority succession order.

        Seniority prioritizes proximity to the Originator, processing all
        individuals in one generation before moving to the next. Within a
        generation, older siblings come before younger ones.

        Returns:
            list: Names of individuals in seniority succession order.
        """
        order = []
        queue = [self.originator]  # Use a queue for breadth-first traversal

        while queue:
            current = queue.pop(0)  # Remove the first element
            order.append(current.name)
            # Add children in order (eldest first)
            queue.extend(current.children)
        return order

    def _get_path_to_originator(self, name):
        """
        Helper method to get the path from the Originator to the specified individual.

        Args:
            name (str): The name of the individual.

        Returns:
            list: A list of _Individual objects representing the path.
        """
        if name not in self.individuals:
            return None  # Should not happen based on assumptions

        path = []
        current = self.individuals[name]
        while current:
            path.append(current)
            current = current.parent
        return path[::-1]  # Reverse to get path from Originator

    def get_cousin_dist(self, lhs_name, rhs_name):
        """
        Determines the degree and removal of two cousins.

        The degree is the lesser of the orders of the two individuals relative
        to their most recent common ancestor (MRCA). The removal is the
        difference in their orders.

        Args:
            lhs_name (str): The name of one individual.
            rhs_name (str): The name of the other individual.

        Returns:
            tuple: A pair (degree, removal) representing the cousin relationship.
        """
        path_lhs = self._get_path_to_originator(lhs_name)
        path_rhs = self._get_path_to_originator(rhs_name)

        if not path_lhs or not path_rhs:
            return None  # Should not happen given problem constraints

        # Find the Most Recent Common Ancestor (MRCA)
        mrca_index = -1
        for i in range(min(len(path_lhs), len(path_rhs))):
            if path_lhs[i] == path_rhs[i]:
                mrca_index = i
            else:
                break

        # Calculate orders relative to the MRCA
        order_lhs = len(path_lhs) - mrca_index - 1
        order_rhs = len(path_rhs) - mrca_index - 1

        # Adjust the order calculation to account for the MRCA being at the same depth
        order_lhs = len(path_lhs) - mrca_index - 2
        order_rhs = len(path_rhs) - mrca_index - 2

        degree = min(order_lhs, order_rhs)
        removal = abs(order_lhs - order_rhs)

        return (degree, removal)
