# 67. Add Binary
# Easy
# Topics
# Companies
# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        one = a[::-1]
        other = b[::-1]

        carry = 0
        result = ""

        i = 0
        while i < len(one) or i < len(other):

            b1 = int(one[i]) if i < len(one) else 0
            b2 = int(other[i]) if i < len(other) else 0

            res = b1 + b2 + carry

            result += str(res % 2)
            carry = res // 2

            i += 1

        if carry:
            result += str(carry)

        return result[::-1]

    def addBinary_v2(self, s1: str, s2: str) -> str:
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        result = ""

        # process both strings from right to left
        while i >= 0 and j >= 0:
            digit_sum = int(s1[i]) + int(s2[j]) + carry
            digit = digit_sum % 2
            carry = digit_sum // 2
            result += str(digit)
            i -= 1
            j -= 1

        # process remaining from s1
        while i >= 0:
            digit_sum = int(s1[i]) + carry
            digit = digit_sum % 2
            carry = digit_sum // 2
            result += str(digit)
            i -= 1

        # process remaining from s2
        while j >= 0:
            digit_sum = int(s2[j]) + carry
            digit = digit_sum % 2
            carry = digit_sum // 2
            result += str(digit)
            j -= 1

        # process final carry
        if carry:
            result += str(carry)

        # return the reversed string
        return result[::-1]


s = Solution()
print(s.addBinary("1010", "1011"))  # 10101
print(s.addBinary("11", "1"))  # 100
print(s.addBinary("10", "10"))  # 100
print(s.addBinary("100", "1000"))  # 1100
print(s.addBinary("1111", "1111"))  # 11110
