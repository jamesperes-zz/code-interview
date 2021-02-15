"""
Sales by Match
Origin: HackerRank

There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.


input:
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

output:
3

>>> count_socks_pair(2, [10, 10])
1

>>> count_socks_pair(3, [10, 10, 20])
1

>>> count_socks_pair(4, [10, 10, 20, 20])
2

>>> count_socks_pair(5, [10, 10, 20, 20, 30])
2

>>> count_socks_pair(6, [10, 10, 20, 20, 30, 40])
2

>>> count_socks_pair(7, [30, 10, 10, 20, 20, 30, 40])
3

>>> count_socks_pair(9, [30, 10, 10, 30, 30, 20, 20, 30, 40])
4

"""

def count_socks_pair(number_of_socks, list_of_sock_colors):
    count_tmp = {}

    for item in list_of_sock_colors:
        if count_tmp.get(item):
            count_tmp[item] += 1
            continue
        count_tmp[item] = 1

    count_pair = 0
    for key, item in count_tmp.items():

        if item > 1:
            count_pair += item // 2

    return count_pair

