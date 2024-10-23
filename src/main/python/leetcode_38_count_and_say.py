# https://leetcode.com/problems/count-and-say/description/
# 38. Count and Say
# Medium
# Topics
# Companies
# Hint
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
#
# Given a positive integer n, return the nth element of the count-and-say sequence.
#
#
#
# Example 1:
#
# Input: n = 4
#
# Output: "1211"
#
# Explanation:
#
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:
#
# Input: n = 1
#
# Output: "1"
#
# Explanation:
#
# This is the base case.

class Solution:
    cache = {1: "1"}

    def countAndSay(self, n: int) -> str:

        def run_length_encoding(n: int):
            if n == 1:
                return "1"

            if n in self.cache:
                return self.cache[n]

            prev_rle = run_length_encoding(n - 1)

            result = process(prev_rle)

            self.cache[n] = result
            return self.cache[n]

        def process(rle_num: str):
            result = ""
            counter = 0

            prev_c = rle_num[0]
            for i in range(len(rle_num)):
                c = rle_num[i]
                if c == prev_c:
                    counter += 1
                else:
                    result += f"{counter}{prev_c}"
                    counter = 1
                prev_c = c

            result += f"{counter}{prev_c}"

            return result

        return run_length_encoding(n)


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))
