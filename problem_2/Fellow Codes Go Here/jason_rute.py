"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

"""
# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def depth_helper(node):
    """
    This function find the max depth of a binary tree.  A tree with only a 
    root node has depth 1, a tree with a root node and one or two leaf nodes,
    has depth 2, etc.

    parameters
    ----------
        node: the root node of the tree

    returns
    -------
        the depth of the tree
    """

    # find max depth on the left (recursively)
    if node.left is None:
        max_left_depth = 0
    else:
        max_left_depth = depth_helper(node.left)

    # find max depth on the right (recursively)
    if node.right is None:
        max_right_depth = 0
    else:
        max_right_depth = depth_helper(node.right)        

    # add one for the current node
    return 1 + max(max_left_depth, max_right_depth)


#PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
	depth = depth_helper(tree)
	return depth



#test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print ("Depth of tree is %d, and the expected result is 3" %(find_max_depth(root),))

if __name__ == "__main__":
    main()
