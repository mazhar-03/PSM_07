# 1
sales = {}

while True:
    answer = input("Write the product (name, price, quantity). If you would like to exit, write 'done': ")

    if answer == 'done':
        break

    data = answer.split(',')
    if len(data) == 3:
        product, price, quantity = data[0].strip(), data[1].strip(), data[2].strip()
        if price.replace('.', '').isdigit() and quantity.isdigit():
            price, quantity = float(price), int(quantity)
            if product in sales:
                sales[product] += price * quantity
                print(f"Product {product} added successfully")
            else:
                sales[product] = price * quantity
                print(f"Product {product} created successfully")
        else:
            print("Invalid input.Price is number quantity is integer")
    else:
        print("Invalid format")

print("Sales Revenue Report:")
for product in sales:
    print(f"{product}: ${sales[product]}")


# 2
def adjust_salaries():
    employees = []

    print("Enter employee datas (type 'done' when finished):")
    while True:
        name = input("Employee Name: ")
        if name == 'done':
            break

        salary_input = input("Salary: ")
        if not salary_input.replace('.', '').isdigit():
            print(f"Invalid salary {salary_input}")
            continue
        salary = float(salary_input)

        score_input = input("Performance Score [0,5]: ")
        if not score_input.replace('.', '').isdigit():
            print(f"Invalid score {score_input}")
            continue
        score = float(score_input)

        if score >= 4.5:
            print("Salary updated")
            new_salary = salary * 1.10
        elif 3.0 <= score < 4.5:
            new_salary = salary * 1.05
            print("Salary updated")
        else:
            new_salary = salary
            print("Salary did not change")

        employees.append({'Name': name, 'Old Salary': salary, 'New Salary': new_salary, 'Score': score})

    print("\nUpdated Salary Report:")
    for emp in employees:
        print(f"{emp['Name']}: Score = {emp['Score']}, Old Salary = ${emp['Old Salary']:.2f}, "
              f", New Salary = ${emp['New Salary']:.2f}")


adjust_salaries()

# 5
correct_password = "secure123"
max_attempts = 3
attempts = 0

username = input("Enter your username: ")
while attempts < max_attempts:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print(f"Access granted for user {username}")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Wrong password! {remaining_attempts} attempts left.")
        else:
            print(f"Account locked for user {username}")
