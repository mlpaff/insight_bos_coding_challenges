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



def depth_helper(node, current_depth=0):
    if node is None:
        # Leaves have depth zero
        return(0)
    else:
        left_value = depth_helper(node.left, current_depth)
        right_value = depth_helper(node.right, current_depth)
        # This node is one step deeper than the deeper of its two children
        return 1 + max(left_value, right_value)

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
