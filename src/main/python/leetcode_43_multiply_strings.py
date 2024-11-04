# https://leetcode.com/problems/multiply-strings/description/
# 43. Multiply Strings
# Medium
# Topics
# Companies
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        if num1 == "1":
            return num2

        if num2 == "1":
            return num1

        result = [0] * len(num1 + num2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                result[i + j] += digit

                res = result[i+j] % 10
                carry = result[i+j] // 10

                result[i + j] = res
                result[i + j + 1] += carry

        result = result[::-1]
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        result = [str(c) for c in result[start:]]
        return "".join(result)

s = Solution()
print(s.multiply("2", "3"))
print(s.multiply("123", "456"))
print(s.multiply("45", "123"))
