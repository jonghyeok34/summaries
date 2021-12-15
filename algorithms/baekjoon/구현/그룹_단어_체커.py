
char_count = int(input())


words = []
for i in range(char_count):
    words.append(input())


group_word_count = 0
for i in range(char_count):
    last_index_by_char = {

    }
    is_group_word = True
    for char_index in range(len(words[i])):
        char_in_word = words[i][char_index]
        if last_index_by_char.get(char_in_word) is not None:
            # 연속하지 않음
            if char_index - 1 != last_index_by_char[char_in_word]:
                is_group_word = False
                break
        last_index_by_char[char_in_word] = char_index

    if is_group_word:
        group_word_count += 1
print(group_word_count)
