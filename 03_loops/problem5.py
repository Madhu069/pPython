# Non repeated character in a string

input_str = "Teeterkdnjbfhv"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Character is:", char)
        break
        