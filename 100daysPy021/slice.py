piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ["do", "re", "me", ]

print(piano_keys)
print(f"This is slice 2 to 5 {piano_keys[2:5]}")
print(f"This is slice 5 onwards {piano_keys[5:]}")
print(f"This is slice 2 to 5 but every other {piano_keys[2:5:2]}")
print(f"This is every other {piano_keys[::2]}")
print(f"This is a reverse list {piano_keys[::-1]}")