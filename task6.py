import functools

# 1
#
# current_user = {
#     "username": "mazo12",
#     "roles": ["admin", "editor"]
# }
#
# def requires_role(role_name):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if role_name in current_user["roles"]:
#                 return func(*args, **kwargs)
#             else:
#                 raise PermissionError(f"User does not have the required role: {role_name}")
#         return wrapper
#     return decorator
#
#
# @requires_role("admin")
# def delete_post(post_id):
#     return f"Post {post_id} deleted."
#
#
# @requires_role("editor")
# def edit_post(post_id):
#     return f"Post {post_id} edited."
#
#
# @requires_role("viewer")
# def view_post(post_id):
#     return f"Post {post_id} viewed."
#
#
# # Try calling the functions
# print(delete_post(42))
# print(edit_post(7))
# print(view_post(99))

# 2
# def log(level):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f"{level}: Starting {func.__name__}")
#             result = func(*args, **kwargs)
#             print(f"{level}: Finished {func.__name__}")
#             return result
#         return wrapper
#     return decorator
#
# @log("INFO")
# def greet(name):
#     print(f"Hello, {name}!")
#
# @log("DEBUG")
# def bugger(num):
#     print(f"Debugged case #{num}")
#
# @log("WARNING")
# def warn_num(n):
#     for i in range(n):
#         print("CLOSE THE PROGRAM!")
#
#
# greet("Gulcin")
# bugger(7)
# warn_num(5)

# 3
# import time
#
# def timer():
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func(*args, **kwargs)
#             end = time.time()
#             duration = end - start
#             print(f"Function '{func.__name__}' took {duration:.2f} seconds to run.")
#             return result
#         return wrapper
#     return decorator
#
# @timer()
# def show_time_after_sleeping(n):
#     time.sleep(n)
#     print("Wake up")
#
# show_time_after_sleeping(3)

# ex1
def log_call():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[INFO] Calling function: '{func.__name__}' with args: {args} and kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"[INFO] Function '{func.__name__}' returned: {result}")
            return result
        return wrapper
    return decorator


@log_call()
def multiply(a, b):
    return a * b


multiply(4, 5)

# ex2
# def log_execution():
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f"[INFO] Starting function: {func.__name__}")
#             result = func(*args, **kwargs)
#             print(f"[INFO] Finishing function: {func.__name__}")
#             return result
#         return wrapper
#     return decorator
#
#
# @log_execution()
# def greet():
#     print("Python_Test1")
#
#
# greet()
