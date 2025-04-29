# product_ids = [101, 102, 103, 104]
# print("Initial product_ids:", product_ids)
# print("Initial memory address:", id(product_ids))
#
# product_ids.append(105)
# product_ids.remove(102)
#
# print("\nModified product_ids:", product_ids)
# print("Memory address after modification:", id(product_ids))
#
# new_product_ids = product_ids.copy()
#
# print("\nNew product_ids:", new_product_ids)
# print("New memory address:", id(new_product_ids))

# 2
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)

# 3
# my_tuple = (1, [2, 3], (4, 5))
# my_tuple[1].append(6)
# print(my_tuple)

# 4
# students = {
#     101: {'name': 'Alice', 'age': 20, 'grades': {'math': 88, 'science': 92,
#                                                  'english': 85}},
#     102: {'name': 'Bob', 'age': 22, 'grades': {'math': 90, 'science': 85,
#                                                'english': 80}},
#     103: {'name': 'Charlie', 'age': 21, 'grades': {'math': 95, 'science':
#         89, 'english': 91}},
# }
#
# students[104] = {'name': 'David', 'age': 23, 'grades': {'math': 92, 'science':
#         87, 'english': 90}}
#
# students[102]['grades']['english'] = 88
# print(students)

# 6
name = input("Enter your name: ")
birth_year = int(input("Enter the year of your birth: "))

age = 2025 - birth_year
print(f"Hello, {name}! You are {age} years old.")
