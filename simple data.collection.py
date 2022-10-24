user_inputs = input("Please enter 5 numeric values: ")

user_list = user_inputs.split(" ")

user_list.sort()

print(user_list)

print(user_list[::-1])
