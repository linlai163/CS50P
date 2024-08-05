grocery_list = {}

while True:
    try:
        item = input("").lower()
    except EOFError:
        print()
        pass

    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

for item, cnt in sorted(grocery_list.items()):
    print(f"{cnt} {item}")

