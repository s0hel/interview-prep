# Calculate maximum value using ‘+’ or ‘*’ sign between two numbers in a string
# https://www.geeksforgeeks.org/calculate-maximum-value-using-sign-two-numbers-string/

def calc_max_value(str):
    # Store first character as integer
    # in result
    res = ord(str[0]) - 48

    # Start traversing the string
    for i in range(1, len(str)):

        # Check if any of the two numbers
        # is 0 or 1, If yes then add current
        # element
        if (str[i] == '0' or
                str[i] == '1' or res < 2):
            res += ord(str[i]) - 48
        else:
            res *= ord(str[i]) - 48

    return res


print(calc_max_value("01891"))
print(calc_max_value("01231"))
print(calc_max_value("891"))
print(calc_max_value("00001000002"))
print(calc_max_value("00002000001"))
print(calc_max_value("200001000002"))
print(calc_max_value("231001000002"))


