# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
  "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem()

member = {
  "name": "Osama",
  "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

print("=" * 40)

# items()

view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys() # here to put data for all keys for one time

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))