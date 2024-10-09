# You are given a string ‘letters’ made of N English letters.
# Count the number of different letters that appear in both uppercase
# and lowercase where all lowercase occurrences of the given letter appear before any uppercase occurrence.
#
# For example, for letters = “aaAbcCABBc” the answer is 2.
# The condition is met for letters ‘a’ and ‘b’, but not for ‘c’
#
# That, given string letters, return the number of different letters fulfilling the conditions above.
#
# Examples
# -----
# letters = “aaAbcCABBc”, the function should return 2
# letters = “xyzXYZabcABC”, the function should return 6
# letters = “ABCabcAefG”, the function should return 0
#
# Write an efficient algorithm for the following assumptions:
# - N is an integer between 1 and 100,000
# - String letters is made only of letters ‘a-z and/or A-Z

def solution(letters: str) -> int:
    lower_map = {} # track right-most index of lowercase letters
    upper_map = {} # track left-most index of uppercase letters
    result = 0

    for i in range(len(letters)):
        c = letters[i]
        if c.islower():
            lower_map[c] = i
        else:
            if c.upper() not in upper_map:
                upper_map[c.upper()] = i

    for c in lower_map:
        if c.upper() in upper_map:
            if lower_map[c] < upper_map[c.upper()]:
                result += 1

    return result


print(solution("aaAbcCABBc"))
print(solution("xyzXYZabcABC"))
print(solution("ABCabcAefG"))




