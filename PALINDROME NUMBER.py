class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        revnum=0
        temp=x
        while temp!= 0:
            digit = temp%10
            revnum=revnum*10 + digit
            temp//=10
        return revnum == x
