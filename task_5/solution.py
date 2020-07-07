from collections import defaultdict
import itertools


def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longest_palindrome(s: str) -> str:
    entries = defaultdict(list)
    for index, letter in enumerate(s):
        entries[letter].append(index)

    max_palindrome = ''
    max_palindrome_len = len(max_palindrome)

    for letter, indices in entries.items():
        perms = itertools.permutations(indices, 2)
        filtered_perms = filter(lambda pair: pair[0] < pair[1], perms)
        sorted_perms = sorted(filtered_perms,
                              key=lambda pair: pair[1] - pair[0], reverse=True)

        for i, j in sorted_perms:
            substr_len = j - i + 1
            if substr_len <= max_palindrome_len:
                break

            if is_palindrome(s, i, j):
                max_palindrome = s[i:j + 1]
                max_palindrome_len = substr_len
                break

    return max_palindrome

    # for letter, indices in entries.items():
    #     for start in range(len(indices)):
    #         i = indices[start]
    #
    #         for end in range(len(indices) - 1, start - 1, -1):
    #             j = indices[end]
    #             substr_len = j - i + 1
    #             if substr_len > max_palindrome_len:
    #                 if is_palindrome(s, i, j):
    #                     max_palindrome = s[i:j + 1]
    #                     max_palindrome_len = substr_len
    #                     break

    # return max_palindrome
