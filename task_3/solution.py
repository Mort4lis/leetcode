def length_of_longest_substring(s: str) -> int:
    """
    Дана строка. Найти максимальную длину подстроки с уникальными символами.

    Например:
    abcabccbb = 3,
    bbbbb = 1

    Args:
        s: исходная строка

    Returns: максимальную длину подстроки с уникальными символами

    """
    i = 0
    j = 0
    max_length = 0
    letter_to_index_map = {}
    while j < len(s):
        letter = s[j]
        if letter in letter_to_index_map:
            i = max(i, letter_to_index_map[letter] + 1)

        max_length = max(max_length, j - i + 1)
        letter_to_index_map[letter] = j
        j += 1
    return max_length


def length_of_longest_substring_other1(s: str) -> int:
    max_length = 0
    for i in range(len(s)):
        letters = set(s[i])
        for j in range(i + 1, len(s)):
            if s[j] in letters:
                break
            letters.add(s[j])
        max_length = max(max_length, len(letters))

    return max_length


def length_of_longest_substring_other2(s: str) -> int:
    i = 0
    j = 0
    max_length = 0
    unique = set()
    while i < len(s) and j < len(s):
        if s[j] not in unique:
            unique.add(s[j])
            j += 1
            max_length = max(max_length, j - i)
        else:
            unique.remove(s[i])
            i += 1
    return max_length
