# 12. Integer to Roman
# Medium
# Topics
# Companies
# Seven different symbols represent Roman numerals with the following values:
#
# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
# Converting a decimal place value into a Roman numeral has the following rules:
#
# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
# append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
# for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms
# are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot
# append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
#
# Given an integer, convert it to a Roman numeral.
#
#
#
# Example 1:
#
# Input: num = 3749
#
# Output: "MMMDCCXLIX"
#
# Explanation:
#
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Example 2:
#
# Input: num = 58
#
# Output: "LVIII"
#
# Explanation:
#
# 50 = L
#  8 = VIII
# Example 3:
#
# Input: num = 1994
#
# Output: "MCMXCIV"
#
# Explanation:
#
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
#

class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""

        roman_map = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        def convertToRoman(n: int):
            if n in roman_map:
                return roman_map[n]
            elif f"{n}".startswith("9"):
                if n < 10:
                    return "IX"
                elif n < 100:
                    return "XC"
                elif n < 1000:
                    return "CM"
            elif f"{n}".startswith("4"):
                if n < 5:
                    return "IV"
                elif n < 50:
                    return "XL"
                elif n < 500:
                    return "CD"
            elif f"{n}".startswith("1") or f"{n}".startswith("2") or f"{n}".startswith("3"):
                if n < 5:
                    return "I" * n
                elif n < 50:
                    return "X" * int(n / 10)
                elif n < 500:
                    return "C" * int(n / 100)
                elif n < 4000:
                    return "M" * int(n / 1000)
            elif f"{n}".startswith("6") or f"{n}".startswith("7") or f"{n}".startswith("8"):
                if n < 10:
                    return "V" + ("I" * (n - 5))
                elif n < 100:
                    return "L" + ("X" * int(((n - 50) / 10)))
                elif n < 1000:
                    return "D" + ("C" * int(((n - 500) / 100)))

        num_str = f"{num}"
        i = len(num_str) - 1
        while i >= 0:
            div = pow(10, i)
            n = int(num / div) * div
            if n > 0:
                s = f"{s}{convertToRoman(n)}"
            num -= n
            i -= 1
        return s


    def intToRoman_better(self, num: int) -> str:
        roman_int_list = [["M", 1000],
                          ["CM", 900],
                          ["D", 500],
                          ["CD", 400],
                          ["C", 100],
                          ["XC", 90],
                          ["L", 50],
                          ["XL", 40],
                          ["X", 10],
                          ["IX", 9],
                          ["V", 5],
                          ["IV", 4],
                          ["I", 1]]

        result = ""
        for roman, n in roman_int_list:
            count = num // n
            if count > 0:
                result += roman * count
                num = num % n

        return result

s = Solution()
print(s.intToRoman_better(60))
print(s.intToRoman_better(3749))
print(s.intToRoman(1))
print(s.intToRoman(2))
print(s.intToRoman(3))
print(s.intToRoman(4))
print(s.intToRoman(5))
print(s.intToRoman(6))
print(s.intToRoman(7))
print(s.intToRoman(8))
print(s.intToRoman(9))
print(s.intToRoman(10))
print(s.intToRoman(11))
print(s.intToRoman(12))
print(s.intToRoman(13))
print(s.intToRoman(14))
print(s.intToRoman(15))
print(s.intToRoman(16))
print(s.intToRoman(17))
print(s.intToRoman(18))
print(s.intToRoman(19))
print(s.intToRoman(20))
