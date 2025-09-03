# 1. Sum all items in a list
def sum_list(lst):
    return sum(lst)


# 2. Multiply all items in a list
def multiply_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result


# 3. Get largest number
def max_in_list(lst):
    return max(lst)


# 4. Get smallest number
def min_in_list(lst):
    return min(lst)


# 5. Count strings with same first and last char, length >=2
def match_strings(lst):
    return sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])


# 6. Sort list of tuples by last element
def sort_tuple(lst):
    return sorted(lst, key=lambda x: x[-1])


# 7. Remove duplicates
def remove_duplicates(lst):
    return list(set(lst))


# 8. Check if list empty
def is_empty(lst):
    return len(lst) == 0


# 9. Clone/copy a list
def clone_list(lst):
    return lst[:]


# 10. Words longer than n
def words_longer_than(n, lst):
    return [w for w in lst if len(w) > n]


# 11. Check if two lists have common member
def common_member(lst1, lst2):
    return any(x in lst1 for x in lst2)


# 12. Remove 0th, 4th, 5th elements
def remove_elements(lst):
    return [x for i, x in enumerate(lst) if i not in (0, 4, 5)]


# 13. Generate 3*4*6 array filled with *
def generate_array():
    return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]


# 14. Remove even numbers
def remove_even(lst):
    return [x for x in lst if x % 2 != 0]


# 15. Shuffle list
import random


def shuffle_list(lst):
    random.shuffle(lst)
    return lst


# 16. First and last 5 squares between 1 and 30
def squares_list():
    sq = [x ** 2 for x in range(1, 31)]
    return sq[:5] + sq[-5:]


# 17. Check if all numbers prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


def all_primes(lst):
    return all(is_prime(x) for x in lst)


# 18. Generate all permutations
import itertools


def permutations(lst):
    return list(itertools.permutations(lst))


# 19. Difference between two lists
def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))


# 20. Access index of list
def list_indices(lst):
    return list(enumerate(lst))


# 21. List of chars to string
def list_to_string(lst):
    return ''.join(lst)


# 22. Find index of item
def find_index(lst, item):
    return lst.index(item)


# 23. Flatten a shallow list
def flatten_list(lst):
    return [x for sub in lst for x in sub]


# 24. Append list to another
def append_lists(lst1, lst2):
    return lst1 + lst2


# 25. Select random item
def random_item(lst):
    return random.choice(lst)


# 26. Check circularly identical
def circular_identical(lst1, lst2):
    return len(lst1) == len(lst2) and ''.join(map(str, lst2)) in ''.join(map(str, lst1 * 2))


# 27. Second smallest number
def second_smallest(lst):
    return sorted(set(lst))[1]


# 28. Second largest number
def second_largest(lst):
    return sorted(set(lst))[-2]


# 29. Unique values
def unique_values(lst):
    return list(set(lst))


# 30. Frequency of elements
from collections import Counter


def frequency(lst):
    return Counter(lst)


# 31. Count elements within a range
def count_in_range(lst, low, high):
    return len([x for x in lst if low <= x <= high])


# 32. Check if list contains sublist
def contains_sublist(lst, sub):
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i + len(sub)] == sub:
            return True
    return False


# 33. Generate all sublists
def all_sublists(lst):
    sublists = []
    for i in range(len(lst) + 1):
        for j in range(i, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists


# 34. Sieve of Eratosthenes
def sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


# 35. Concatenate list with range
def concat_list(lst, n):
    return [x + str(i) for i in range(1, n + 1) for x in lst]


# 36. Variable ID
def variable_id(x):
    return id(x)


# 37. Common items in two lists
def common_items(lst1, lst2):
    return list(set(lst1) & set(lst2))


# 38. Swap every n-th with (n+1)-th
def swap_positions(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


# 39. Convert list of ints to single int
def list_to_int(lst):
    return int(''.join(map(str, lst)))


# 40. Split list by first char
from collections import defaultdict


def split_by_firstchar(lst):
    d = defaultdict(list)
    for word in lst:
        d[word[0]].append(word)
    return dict(d)


# 41. Create multiple lists
def multiple_lists(n):
    return [[] for _ in range(n)]


# 42. Missing and additional values
def missing_additional(lst1, lst2):
    return (list(set(lst1) - set(lst2)), list(set(lst2) - set(lst1)))


# 43. Split list into variables
def split_into_vars(lst):
    return tuple(lst)


# 44. Groups of 5 consecutive numbers
def group_consecutive(n):
    return [list(range(i, i + 5)) for i in range(1, n, 5)]


# 45. Pair to sorted unique array
def pair_to_array(pair):
    return sorted(set(pair))


# 46. Select odd items
def odd_items(lst):
    return lst[1::2]


# 47. Insert element before each element
def insert_before(lst, val):
    result = []
    for x in lst:
        result.append(val)
        result.append(x)
    return result


# 48. Print nested lists
def print_nested(lst):
    for sub in lst:
        print(sub)


# 49. List to list of dicts
def list_to_dicts(names, codes):
    return [{"color_name": n, "color_code": c} for n, c in zip(names, codes)]


# 50. Sort list of nested dictionaries
def sort_nested_dict(lst, key):
    return sorted(lst, key=lambda x: x[key])
