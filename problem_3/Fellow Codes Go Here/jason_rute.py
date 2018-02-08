"""
Given a string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

def is_substring_helper (data):
    """
    Takes in a string data and tests if there is a proper substring ss such that 
    data = ss * n for some n.

    parameters
    ----------
        data: the string

    returns
    -------
        a bool indicating if data is a multiple of a proper substring
    """

    substring_candidate = data[0] # start with initial character (prevents div by zero issues)

    for i, c in enumerate(data):
        if c != substring_candidate[i % len(substring_candidate)]: #candidate is no longer valid
            substring_candidate = data[:i+1] # replace candidate with current substring 

    # check that candidate is not just the whole string
    # check that candidate evenly divides the length of the string
    if substring_candidate == data or len(data) % len(substring_candidate): 
        return False
    else:
        return True

#DON NOT CHANGE THIS FUNCTION
def is_substring (string_input):
    return is_substring_helper(string_input)


#test case
def main():
    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    print ("Testing your code with TEST_CASE1, the expected output is True, your output is {}".format(is_substring(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is False, your output is {}".format(is_substring(TEST_CASE2)))
    print ("Testing your code with TEST_CASE3, the expected output is True, your output is {}".format(is_substring(TEST_CASE3)))

if __name__ == "__main__":
    main()