import datetime


names = input("Please enter 6 different names, separated by a comma: ").upper()

names_list = names.split(",")

total_length = 0
for name in names_list:
    name = name.center(40)
    print(name)
    length = len(name)
    total_length += length

print(f"\nThe total length of names is {total_length}")

today = datetime.datetime.now()

date = today.strftime("%A, %B %d, %Y")
time = today.strftime("%l:%M %p")
print(f"Date: {date}\nTime: {time}")

