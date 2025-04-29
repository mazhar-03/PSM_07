# 2
accounts = {
 "Alice": {"balance": 1000},
 "Bob": {"balance": 250},
 "Charlie": {"balance": 80},
}


def withdraw(name, amount):
    if accounts[name]["balance"] > amount:
        if amount % 10 == 0:
            accounts[name]["balance"] -= amount
            print("Withdraw successful\n")
            return True
        else:
            print("Be sure that amount of withdraw is a multiple of 10\n")
            return False
    else:
        print("Insufficient money\n")
        return False


while True:
    name = input("Enter your name, for exit press 0: ")
    if name == "0":
        print("Exiting...")
        break
    else:
        if name not in accounts:
            print("User not found!\n")
            break
        else:
            amount = float(input("Enter the withdraw amount: "))
            withdraw(name, amount)

# 4
students = [
 {"name": "Alice", "exam_score": 85, "attendance": 90},
 {"name": "Bob", "exam_score": 58, "attendance": 75},
 {"name": "Charlie", "exam_score": 45, "attendance": 80},
 {"name": "Diana", "exam_score": 92, "attendance": 95},
 {"name": "Ethan", "exam_score": 60, "attendance": 40}
]


def evaluate(name):
    found = False
    for student in students:
        if student["name"] == name:
            found = True
            passed_score = student["exam_score"] >= 60
            passed_attendance = student["attendance"] >= 50
            if passed_attendance and passed_score:
                print(f"{student["name"]} has PASSED the class!\n")
            else:
                print(f"{student["name"]} has FAILED the class!\n")
    if not found:
        print("The student is not found.\n")


while True:
    student_name = input("Enter student name, for exit press 0: ")
    if student_name == "0":
        print("Exiting...")
        break
    evaluate(student_name)

