print("Customer ID Search System \n")

# linear search function
def linear_search(key):
    found = False
    for i in range(len(customer_list)):
        if key == customer_list[i]:
            print(f"Customer ID found at index {i}")
            found = True
    if not found:
        print("Customer ID not found")

# bubble sort function
def bubble_sort():
    n = len(customer_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if customer_list[j] > customer_list[j+1]:
                customer_list[j], customer_list[j+1] = customer_list[j+1], customer_list[j]

# binary search function
def binary_search(key):
    bubble_sort()
    beg = 0
    end = len(customer_list) - 1
    found = False

    while beg <= end:
        mid = (beg + end) // 2
        if customer_list[mid] == key:
            print(f"Customer ID found at index {mid}")
            found = True
            break
        elif key > customer_list[mid]:
            beg = mid + 1
        else:
            end = mid - 1

    if not found:
        print("Customer ID not in the list")

# --------------------
# Taking inputs
# --------------------
customer_list = []
n = int(input("How many Customer IDs do you want to add? "))

for i in range(n):
    x = int(input(f"Enter Customer ID {i+1}: "))
    customer_list.append(x)

target = int(input("Enter Customer ID to find: "))

# --------------------
# Menu
# --------------------
while True:
    print("\nSearching Algorithms:")
    print("1: Linear Search")
    print("2: Binary Search")
    print("3: Exit")
    choice = int(input("Enter your choice (1, 2 or 3): "))

    if choice == 1:
        linear_search(target)
    elif choice == 2:
        binary_search(target)
    elif choice == 3:
        print("Thank you")
        break
    else:
        print("Invalid Input")