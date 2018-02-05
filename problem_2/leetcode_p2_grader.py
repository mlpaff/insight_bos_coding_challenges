import sys
import os
import importlib


# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 


# Compute the "find_max_depth" of a tree -- the number of nodes 
# along the longest path from the root node down to the 
# farthest leaf node
def _find_max_depth(node):
    if node is None:
        return 0 ; 
 
    else :
 
        # Compute the depth of each subtree
        lDepth = _find_max_depth(node.left)
        rDepth = _find_max_depth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

#test case helper functions
def test_case_helper(module, test_case):
    try:
        if module.find_max_depth(test_case) == _find_max_depth(test_case): return 1
    except:
        return 0


def main():
    data_dir = './leetcode_exercise/example_2/'
    input_files = os.listdir(data_dir)
    sys.path.append(data_dir)
    

    grad_file = open("leetcode_p2_grade_report.txt","w") 
    for filename in [f for f in input_files if f.endswith(".py")]:  
        modulename = filename.split(".")[0]   
        grad_file.write ('Leetcode P2 grade report: {}\n'.format(modulename))

        try:
            module = importlib.import_module(modulename, ".py")
            #TEST_CASE_1: empty tree
            root = None
            if test_case_helper(module, root) == 1:
                grad_file.write ('Testing your code with input of empty tree: PASS\n')
            else:
                grad_file.write ('Testing your code with input of empty tree: FAIL\n')

            #TEST_CASE 2
            root = Node(1)
            root.left = Node(2)
            root.right = Node(3)
            root.left.left = Node(4)
            root.left.right = Node(5)

            if test_case_helper(module, root) == 1:
                grad_file.write ('Testing your code with a Tree with Height of 3: PASS\n\n\n')
            else:
                grad_file.write ('Testing your code with a Tree with Height of 3: FAIL\n\n\n')

        except:
            grad_file.write ('unable to open {} file, please douable check your code.\n\n\n'.format(modulename))

    grad_file.close() 
    return 0

if __name__ == "__main__":
    main()