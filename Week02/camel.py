name = input("input a name which is camelCase: ")

snake = "".join("_" + ch.lower() if ch.isupper() else ch for ch in name)

print("snake_case:", snake)

