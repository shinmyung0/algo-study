# import requests
# import mysql.connector
# import pandas as pd
import math


# Suppose that you have a list s of m lists, with each s[i] containing
# n nonempty strings. We want to print these strings as a table in a
# terminal. The table needs to have n columns, the kth one having width
# w[k]. Each pair of adjacent columns must be separated by a pipe
# character ('|').

# Visualization:

# s[0][0]  |s[0][1]  | ... |s[0][n-1]
# s[1][0]  |s[1][1]  | ... |s[1][n-1]
# ...
# s[m-1][0]|s[m-2][1]| ... |s[m-1][n-1]

# If a string s[i][k] is longer than than the width w[k] of its column,
# it will be wrapped. This means that the row of the table will span at
# least ceil(len(s[i][k]) / w[k]) lines of text. For example, if you
# need to print the string 'abcdefghij' in a column of width 4, it
# should look like
# ...|abcd|...
# ...|efgh|...
# ...|ij  |...
# and so the row containing that string must span at least 3 lines of
# text.

# Given s and w, print the table. (No need to worry about space/time complexity.)

"""

for row in input
    
    for width in w:
        print as many characters as you can in the current cell
        
    for cell in row:
        output as many characters as there are
        numbers in weights or until we don't have any characters left
        
        make sure to update the weight for the cell // tracks index of 

"""

# Examples:
# Input:
# s = [
#  ["123456789012", "1234567", "1234567890"],
#  ["123", "123456789012345", "12345"],
#  ["12345", "12345678901", "12"],
# ]

s = [
    ["abc", "defgh"],
    [
        "ij",
        "klmnopq",
    ],
]

w = [2, 5]
# Output:
# ab|defgh
# c |
# ij|klmno
#   |pq


def print_table(s, w):
    curr = 0
    while curr < len(s):
        row = s[curr]

        for i in range(len(row)):
            curr_str = row[i]
            weight = w[i]
            if i == len(row) - 1:
                print(curr_str[:weight])
            else:
                to_print = curr_str[:weight]

                padding = " " * (weight - len(to_print))
                to_print += padding
                print(to_print, end="|")
            row[i] = curr_str[weight:]

        all_empty = True
        for n in row:
            if n != "":
                all_empty = False

        if all_empty:
            curr += 1


# print_table(s, w)


# Suppose that the total width of the columns can be at most W, i.e.
# sum(w) <= W. Given s and W, find the distribution of column widths w
# that minimizes the height of the tallest row. (If there are multiple
# such w, any of them is fine.)

# Example:
# Input:
# s = [
#  ["123456789012", "1234567", "1234567890"],
#  ["123", "123456789012345", "12345"],
#  ["12345", "12345678901", "12"],
# ]
# W = 15
# Sample outputs:
# w = [5, 5, 5]: good (row heights are 3, 3, 3; tallest row has height 3)

# w = [5, 6, 4]: good (row heights are 3, 3, 2; tallest row has height 3)

# w = [4, 5, 4]: good (row heights are 3, 3, 3; tallest row has height 3)

# w = [6, 6, 3]: bad  (row heights are 4, 3, 2; tallest row has height 4)

"""


"""


def get_all_distributions(max_w, num_cols):
    if max_w == num_cols:
        return [[1] * num_cols]
    if num_cols > max_w:
        return []
    if num_cols == 1:
        return [[max_w]]

    results = []
    for i in range(1, max_w - (num_cols - 1) + 1):
        start = [i]
        possible_subresults = get_all_distributions(max_w - i, num_cols - 1)
        for item in possible_subresults:
            results.append(start + item)
    return results


def calculate_height(input_str, weight):
    return math.ceil(len(input_str) / weight)


def tallest_row_height(s, w):
    tallest_row = 0
    for row in s:
        for j in range(len(row)):
            input_str = row[j]
            weight = w[j]
            height = calculate_height(input_str, weight)
            if height > tallest_row:
                tallest_row = height
    return tallest_row


def min_distribution(s, W):
    num_cols = len(s[0])
    distributions = get_all_distributions(W, num_cols)
    min_height = -1
    min_dist = None
    for dist in distributions:
        curr_height = tallest_row_height(s, dist)
        if min_height == -1 or min_height > curr_height:
            min_height = curr_height
            min_dist = dist
    return min_height, min_dist


s = [
    ["123456789012", "1234567", "1234567890"],
    ["123", "123456789012345", "12345"],
    ["12345", "12345678901", "12"],
]
W = 15
min_height, min_dist = min_distribution(s, W)
print("min_height: ", min_height)
print("min_dist: ", min_dist)

# Brute Force complexity