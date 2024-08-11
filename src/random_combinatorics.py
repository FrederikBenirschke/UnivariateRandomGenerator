import bisect
import random
import math
from functools import lru_cache
from random_variables import *

def random_permutation(n):
    """
    Generates a random permutation of the integers from 0 to n-1.

    Parameters:
    -----------
    n : int
        The size of the permutation.

    Returns:
    --------
    tuple of int
        A tuple representing the randomly generated permutation.
    """
    perm = list(range(n))
    for i in range(n):
        j = uniform_int(i, n - 1)
        perm[i], perm[j] = perm[j], perm[i]
    return tuple(perm)

def random_subset(n, k):
    """
    Generates a random subset of size k from the set {0, 1, ..., n-1}.

    Parameters:
    -----------
    n : int
        The size of the full set.
    k : int
        The size of the subset.

    Returns:
    --------
    tuple of int
        A tuple representing the randomly generated subset.
    """
    perm = list(range(n))
    # Perform the Fisher-Yates shuffle, but only for the first k elements
    for i in range(k):
        j = uniform_int(i, n - 1)
        perm[i], perm[j] = perm[j], perm[i]
    return tuple(perm[:k])

def random_partition_with_parts(n, k):
    """
    Generates a random partition of the integer n into k parts.

    Parameters:
    -----------
    n : int
        The integer to partition.
    k : int
        The number of parts in the partition.

    Returns:
    --------
    tuple of int
        A tuple representing the randomly generated partition with k parts.
    """
    if k == 1:
        return (n,)

    # Generate k-1 numbers in the range [0, n-k] and sort them
    cuts = sorted([uniform_int(0, n-k) for _ in range(k-1)])
    
    # Calculate the partition by taking differences of cuts
    parts = [cuts[0] + 1] + [cuts[i] - cuts[i-1] + 1 for i in range(1, k - 1)] + [n - k - cuts[-1] + 1]

    return tuple(parts)

def sample(lst, weights=None):
    """
    Samples an element from a list with given probabilities.

    Parameters:
    -----------
    lst : list or int
        The list from which to sample. If an int is provided, the list will be generated as range(lst).
    weights : list of float, optional
        A list of probabilities corresponding to the elements of lst.

    Returns:
    --------
    element from lst
        A randomly sampled element from the list based on the provided weights.
    """
    if isinstance(lst, int):
        lst = list(range(lst))
    if weights is None:
        weights = [1 / len(lst) for _ in range(len(lst))]
    
    # Compute cumulative probabilities
    cum_sum = 0
    probabilities = []
    for prob in weights:
        cum_sum += prob
        probabilities.append(cum_sum)
    
    assert abs(cum_sum - 1) < 1e-6, "Probabilities must sum to 1"
    
    # Sample an element
    index = bisect.bisect_left(probabilities, uniform(0, 1))
    return lst[index]

@lru_cache(maxsize=None)
def number_partitions(n, max_part=None):
    """
    Calculates the number of partitions of `n` with the largest part at most `max_part`.
    Dynamic programming algorithm with memoization, runtime is O(n * max_part).

    Parameters:
    -----------
    n : int
        The positive integer to partition.
    max_part : int, optional
        The maximum allowed value for any part of the partition. Defaults to `n`.

    Returns:
    --------
    int
        The number of possible partitions of `n` with parts not exceeding `max_part`.
    """
    if n == 0:
        return 1  # Base case: only one way to partition 0.
    if n < 0 or max_part == 0:
        return 0  # No valid partitions if `n` is negative or `max_part` is zero.
    if max_part is None:
        max_part = n  # Default max part to `n` if not specified.

    # Recursively calculate the number of partitions. 
    return number_partitions(n, max_part - 1) + number_partitions(n - max_part, max_part)

def random_partition(n, max_part=None):
    """
    Generates a random partition of the integer `n`.

    A partition is a way of writing `n` as a sum of positive integers. The order of summands does not matter.
    
    Preprocessing step: `number_partitions(n, max_part)` is used to calculate the number of partitions and has runtime O(n * max_part).
    The results are cached and subsequent calls have O(n) runtime.

    Parameters:
    -----------
    n : int
        The positive integer to partition.
    max_part : int, optional
        The maximum allowed value for any part of the partition. Defaults to `n`.

    Returns:
    --------
    tuple of int
        A tuple representing a randomly generated partition of `n`.
    """
    if n == 0 or max_part == 0:
        return ()  # Base case: no partition possible.

    if max_part is None or max_part > n:
        max_part = n  # Default max part to `n` if not specified or exceeds `n`.

    # Calculate the weights for sampling based on the number of partitions.
    weights = [number_partitions(n - i, i) for i in range(1, max_part + 1)]
    total_weight = sum(weights)
    weights = [weight / total_weight for weight in weights]

    # Randomly select the first part of the partition using the calculated weights.
    first_part = sample(range(1, max_part + 1), weights)

    # Recursively generate the remaining partition and return the result as a tuple.
    return (first_part,) + random_partition(n - first_part, first_part)

def random_ordered_partition(n):
    """
    Generates a random ordered partition of a positive integer `n`.

    An ordered partition of `n` is a way of writing `n` as a sum of positive integers, where the order of the summands matters.
    
    For example, for n = 5, some possible ordered partitions are (5), (4, 1), (3, 2), (2, 1, 2), etc.

    Parameters:
    -----------
    n : int
        The positive integer to partition.

    Returns:
    --------
    tuple of int
        A tuple representing a randomly generated ordered partition of `n`.
    """
    
    # Base case: when n is 0, return an empty tuple (no partition).
    if n == 0:
        return ()
    
    # Base case: when n is 1, the only partition is (1).
    if n == 1:
        return (1,)
    
    # Generate n-1 random positions (0 or 1) to determine where to split the partitions.
    positions = [uniform_int(0, 1) for _ in range(n - 1)]
    
    partition = []  # List to store the parts of the partition.
    part = 1  # Start with the first part.
    
    # Iterate over the random positions to form the partition.
    for pos in positions:
        if pos == 0:
            # Continue adding to the current part.
            part += 1
        else:
            # End the current part and start a new one.
            partition.append(part)
            part = 1
    
    # Append the last part to the partition.
    partition.append(part)
    
    # Return the partition as a tuple.
    return tuple(partition)

def young_tableau(partition, sort=False):
    """
    Converts a partition into a Young tableau.

    A Young tableau is a visual representation of a partition, where each part is represented by a row of squares.

    Parameters:
    -----------
    partition : tuple of int
        The partition to convert into a Young tableau.
    sort : bool, optional
        Whether to sort the partition in descending order before generating the tableau. Defaults to False.

    Returns:
    --------
    str
        A string representation of the Young tableau.
    """
    if sort:
        partition = tuple(sorted(partition, reverse=True))
    
    tableau = []
    
    for part in partition:
        row = '■ ' * part
        tableau.append(row)
    
    return '\n'.join(tableau)

def random_young_tableau(n):
    """
    Generates a random Young tableau corresponding to a random partition of n.

    Parameters:
    -----------
    n : int
        The positive integer to partition.

    Returns:
    --------
    str
        A string representation of the randomly generated Young tableau.
    """
    return young_tableau(random_partition(n))

@lru_cache(maxsize=None)
def number_dyck_words(n):
    """
    Calculates the number of Dyck words of length 2n.

    A Dyck word is a balanced string of X's and Y's such that in any prefix of the word, the number of X's is at least the number of Y's.

    Parameters:
    -----------
    n : int
        The number of pairs of X's and Y's.

    Returns:
    --------
    int
        The number of Dyck words of length 2n.
    """
    return math.comb(2*n, n) // (n+1)

def random_dyck_word(n):
    """
    Generates a random Dyck word of length 2n.

    A Dyck word is a balanced string of X's and Y's such that in any prefix of the word, the number of X's is at least the number of Y's.

    Parameters:
    -----------
    n : int
        The number of pairs of X's and Y's.

    Returns:
    --------
    str
        A randomly generated Dyck word of length 2n.
    """
    if n == 0:
        return ""

    # Calculate the weights for the possible positions of the first "X" matching its "Y"
    weights = [number_dyck_words(i-1) * number_dyck_words(n-i) for i in range(1, n+1)]
    total_weight = sum(weights)
    weights = [weight / total_weight for weight in weights]

    # Randomly select the position k
    k = sample(range(1, n+1), weights=weights)

    return "X" + random_dyck_word(k-1) + "Y" + random_dyck_word(n-k)

class TreeNode:
    """
    A class representing a node in a binary tree.

    Attributes:
    -----------
    value : any
        The value stored in the node.
    left : TreeNode, optional
        The left child of the node.
    right : TreeNode, optional
        The right child of the node.
    """
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def __repr__(self, level=0, prefix="Root: "):
        """
        Generates a string representation of the binary tree for easy visualization.
        """
        ret = "\t" * level + prefix + repr(self.value) + "\n"
        if self.left:
            ret += self.left.__repr__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__repr__(level + 1, "R--- ")
        return ret

    def __eq__(self, other):
        """
        Checks if two binary trees are structurally and value-wise equivalent.
        """
        if isinstance(other, TreeNode):
            return (self.value == other.value and
                    self.left == other.left and
                    self.right == other.right)
        return False

    def __hash__(self):
        """
        Generates a hash value for the binary tree based on its structure and values.
        """
        return hash((self.value, self.left, self.right))

def dyck_word_to_tree(word):
    """
    Converts a Dyck word into a binary tree.

    Parameters:
    -----------
    word : str
        The Dyck word to convert into a binary tree.

    Returns:
    --------
    TreeNode
        The root of the binary tree corresponding to the Dyck word.
    """
    if len(word) == 0:
        return None 
    
    first, second = '', ''
    balanced = 0 
    
    # Find the first balanced prefix
    for i, char in enumerate(word):
        if char != "Y":
            balanced += 1
        else:
            balanced -= 1
            if balanced == 0:
                first = word[1:i]
                second = word[i+1:]
                break

    root = TreeNode("X")
    root.left = dyck_word_to_tree(first)
    root.right = dyck_word_to_tree(second)

    return root

def random_binary_tree(n):
    """
    Generates a random binary tree with `n` nodes.

    The tree is generated by first creating a random Dyck word of length 2n and then converting it into a binary tree.

    Parameters:
    -----------
    n : int
        The number of nodes in the binary tree.

    Returns:
    --------
    TreeNode
        The root of the randomly generated binary tree.
    """
    return dyck_word_to_tree(random_dyck_word(n))
