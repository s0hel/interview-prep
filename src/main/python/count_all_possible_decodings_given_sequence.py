# https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
# Count Possible Decodings of a given Digit Sequence
# Last Updated : 15 Apr, 2023
# Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.
#
# Examples:
#
# Input:  digits[] = "121"
# Output: 3
# // The possible decodings are "ABA", "AU", "LA"
#
# Input: digits[] = "1234"
# Output: 3
# // The possible decodings are "ABCD", "LCD", "AWD"
from typing import List


def count_possible_decodings(s: str) -> List[str]:
    result = []

    def convert_number_to_character(n: int) -> chr:
        return chr(n + ord('A') - 1)

    def helper(s1, output):
        if not s1:
            result.append(output)
            return

        # parse first digit, convert it to ascii character,
        # append to existing output, and recursively run it for the rest of the string
        num = int(s1[0])
        o1 = output + convert_number_to_character(num)
        helper(s1[1:], o1)

        # parse two digits, if it is between 10 and 26, then convert that to ascii character,
        # append to existing output, and recursively run it for the rest of the string
        num = int(s1[0:2])
        if 10 <= num <= 26:
            o2 = output + convert_number_to_character(num)
            helper(s1[2:], o2)

    helper(s, "")

    return result


print(count_possible_decodings('121'))  # The possible decodings are "ABA", "AU", "LA"
print(count_possible_decodings('1234'))  # The possible decodings are "ABCD", "LCD", "AWD"
