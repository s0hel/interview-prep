MAX_CHAR = 26
offset = ord('A')
offset_num = ord('0')

def sort_string(s: str) -> str:
    char_arr = [0] * MAX_CHAR
    num_arr = [0] * 10

    for i in range(len(s)):
        c = s[i]

        if 'A' <= c <= 'Z':
            char_arr[ord(c) - offset] += 1

        if '0' <= c <= '9':
            num_arr[ord(c) - offset_num] += 1

    result = ""
    for i in range(len(char_arr)):
        if char_arr[i]:
            for _ in range(char_arr[i]):
                result += chr(offset + i)

    for i in range(len(num_arr)):
        if num_arr[i]:
            for _ in range(num_arr[i]):
                result += chr(offset_num + i)

    return result


print(sort_string("AC2BEW3")) # ABCEW23
print(sort_string("JD72MCDB23")) # ABCEW23
