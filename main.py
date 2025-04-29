# result = [x for x in range(5) if x % 2 == 0]
# print(result)

# 2
# data = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"], "location": "NYC"}
# data["age"] = 31
# data["skills"].append("Git")
# data["email"] = "student@pjwstk.edu.pl"
# print(data)

# 3
# x = [1, 2, 3]
# y = x.copy()
# y.append(4)
# print(x)

# 4
# numbers = [10, 20, 30, 40, 50]
# process = lambda nums: [n + 5 for n in nums[1:4]]
# result = process(numbers)
# print(numbers)
# print(result)

# 5
# data = [5, 3, 6, 2]
# transform = lambda x: [(i, i**2) for i in sorted(x)]
# result = transform(data)
# print(result)

# 6
# def func(x):
#     return x if x <= 1 else x * func(x-1)
#
#
# print(func(5))


# Open-ended
# 7
# def log_execution(func):
#     def wrapper(*args, **kwargs):
#         print(f"[INFO] Starting function: '{func.__name__}'")
#         result = func(*args, **kwargs)
#         print(f"[INFO] Finishing function: '{func.__name__}'")
#         return result
#     return wrapper
#
# @log_execution
# def greet():
#     print("Python_Test!")
#
# greet()

# 8
# int_list = [1, 2, 3]
# str_list = ['one', 'two', 'three']
#
# result = {}
# index = 0
# while index < len(int_list):
#     result[int_list[index]] = str_list[index]
#     index += 1
#
# print(result)

# 9
# def is_valid_triangle(a,b,c):
#     return a + b > c and a + c > b and a + c > b
#
#
# print(is_valid_triangle(3, 4, 5))  # True
# print(is_valid_triangle(1, 2, 3))


# 10
# def age_group(age):
#     if age < 18:
#         return "Minor"
#     elif age > 18 and age <= 64:
#         return "Adult"
#     else:
#         return "Senior"
#
#
# print(age_group(64))

# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)

# def debug_log(func):
#     def wrapper(*args, **kwargs):
#         print(f"[DEBUG] Calling function: {func.__name__}")
#         print(f"[DEBUG] Arguments: args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"[DEBUG] Result: {result}")
#         return result
#     return wrapper
#
#
# @debug_log
# def multiply(a, b):
#     return a * b
#
#
# # Example usage:
# multiply(3, 4)


# def reverse_dict(d):
#     reverse_d = {}
#
#     for key, value in d.items():
#         reverse_d[value] = key
#     return reverse_d
#
#
# print(reverse_dict({'a': 1, 'b': 2}))

# def can_vote(age, citizen):
#     return age >= 18 and citizen
#
#
# print(can_vote(20, True))
# print(can_vote(16, True))
# print(can_vote(30, False))

