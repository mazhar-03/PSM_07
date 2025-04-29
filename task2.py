# 1
sales_data = {
    'Product A': [100, 200, 300],
    'Product B': [150, 250, 350],
    'Product C': [50, 70, 90]
}


# def calculate_total_sales(sales_data):
#     total_sales = {}
#     for product, sales in sales_data.items():
#         total = sum(sales)
#         total_sales[product] = total
#
#     top_product = max(total_sales, key=total_sales.get)
#
#     return total_sales, top_product
#
#
# totals, best_product = calculate_total_sales(sales_data)
#
# print("Total Sales for Each Product:", totals)
# print("Product with the Highest Sales:", best_product)


# 3

def range_calculations(n1, n2):
    prime_numbers = []
    sum = average = 0
    for i in range(n1, n2 + 1):
        if (i > 1):
            isPrime = True
            for j in range(2, i):
                if (i % j == 0):
                    isPrime = False
                    break
            if (isPrime):
                prime_numbers.append(i)
    for i in prime_numbers:
        sum += i

    average = sum / len(prime_numbers)
    return prime_numbers, sum, average


numbers, sum, average = range_calculations(10, 30)
print(f"Prime numbers: {numbers}")
print(f"Total: {sum}")
print(f"Average: {average}")
