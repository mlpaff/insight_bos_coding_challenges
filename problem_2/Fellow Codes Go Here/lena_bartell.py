"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node

"""
# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def depth_helper(node):
    depths = tree_depth(node, 1)    
    return depths


def tree_depth(tree, depth):
    """
    Input:
        tree (root)
        depth (current node depth)

    Output:
        maximum depth via current node
    """

    # the max depth is at least as big as the current depth
    max_depth = depth


    # If there is a left split, see how deep it is
    if tree.left:
        depthL = tree_depth(tree.left, depth + 1)

        # If left depth is deeper than current max, set it as the new max depth
        if depthL > max_depth:
            max_depth = depthL

    # If there is a right split, see how deep it is
    if tree.right:
        depthR = tree_depth(tree.right, depth + 1)

        # If left depth is deeper than current max, set it as the new max depth
        if depthR > max_depth:
            max_depth = depthR

    return max_depth


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
