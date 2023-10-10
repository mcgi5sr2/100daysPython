with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# modes r for read, w for write, a for append
with open("new_file.txt", mode="w") as file:
    file.write("new text.")
