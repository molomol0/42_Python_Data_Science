from array2D import slice_me

family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

# Test without errors
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# Test with errors
# family_error_1 = [
#     [1.80, 78.4],
#     [2.15, 102.7],
#     [2.10, 98.5, 1.88],
#     [1.88, 75.2]
# ]

# family_error_2 = [
#     [1.80, 78.4],
#     [2.15, 102.7],
#     [2.10, 98.5],
#     1.88
# ]

# print(slice_me(family_error_1, 0, 2))
# print(slice_me(family_error_2, 0, 2))
