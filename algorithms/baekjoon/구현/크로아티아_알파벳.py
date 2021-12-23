chars = input()
temp_char = []
count = 0

suspected_char_list = ["d","l","n", "c", "s", "z"]
not_char_list = ["=", "-"]
special_alphabets =  ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
three_char_alphabets = ["dz="]
count = len(chars)
for i in range(len(chars)-1):
    if chars[i] + chars[i+1] in special_alphabets:
        count -= 1
for i in range(len(chars)-2):
    if chars[i] + chars[i+1] + chars[i+2] in special_alphabets:
        count -= 1
print(count)