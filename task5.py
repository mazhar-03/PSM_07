# def process_data(data):
#     sorted_data = sorted(data, key=lambda x: x[0])
#     filtered_data = list(filter(lambda x: x[1] >= 5, sorted_data))
#     squared_numbers = list(map(lambda x: x[1] ** 2, filtered_data))
#     sorted_strings = list(map(lambda x: x[0], filtered_data))
#     filtered_out_count = len(data) - len(filtered_data)
#
#     return {
#         "sorted_strings": sorted_strings,
#         "squared_numbers": squared_numbers,
#         "filtered_out_count": filtered_out_count
#     }
#
# data = [("apple", 3), ("banana", 7), ("cherry", 2), ("date", 10)]
# result = process_data(data)
# print(result)

# 2
def process_data(data):
    # defining the age threshold
    age_threshold = int(input("Enter the min age threshold: "))

    # Filters out tuples where the number (age) is less than a given threshold or where the status is False.
    filtered_data = list(filter(lambda e: e[1] >= age_threshold and e[2] is True, data))

    # sorting by age in descending order
    sorted_data = sorted(filtered_data, key=lambda e: e[1], reverse=True)

    # A sorted list of names (in uppercase)
    uppercase_names = list(map(lambda e: e[0].upper(), sorted_data))

    # A list of ages for the filtered data
    ages = list(map(lambda e: e[1], sorted_data))

    # The average age of the filtered data.
    average_of_ages = sum(ages) / len(ages) if ages else None

    # The count of active people.
    active_people = sum(1 for e in data if e[2] is True)

    # returning dictionary
    return {
        'Sorted Names': uppercase_names,
        'Ages': ages,
        'Average of ages': average_of_ages,
        'Number of active people': active_people
    }


data = [
    ("Alice", 30, True),
    ("Bob", 15, True),
    ("Charlie", 25, False),
    ("David", 40, True),
    ("Eve", 17, False),
    ("Frank", 20, True)
]
print(process_data(data))
