array = []
num_elements = int(input("Enter the number of elements you want to add: "))

for i in range(num_elements):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)
print("Final array:", array)
