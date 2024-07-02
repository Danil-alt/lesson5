immutable_var = (0, 1, 2, 3, "string", [5, 6, 7], 6, True, 8, 9)
print(immutable_var)
#immutable_var[0] = 86; immutable_var[7] = False
immutable_var[5][0] = 49
print(immutable_var)
mutable_list = [0, 1, 2, 3, "string", [5, 6, 7], 6, True, 8, 9]
print(mutable_list)
mutable_list[4] = 987
print(mutable_list)
mutable_list[5] = 'список'; mutable_list[7] = False
print(mutable_list)