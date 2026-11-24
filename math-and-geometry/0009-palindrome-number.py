class Solutions(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[:: -1]

if __name__ == "__main__":
    sol = Solutions()

   # Standard cases and edge cases
    assert sol.isPalindrome(121) is True, "Error on 121"
    assert sol.isPalindrome(-121) is False, "Error on -121"
    assert sol.isPalindrome(10) is False, "Error on 10"
    assert sol.isPalindrome(0) is True, "Error on 0"

    print("All tests passed successfully !")