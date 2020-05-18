# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name": "Osama"
}
print(user)
user.clear() # here to clear your data in the user
print(user)

print("=" * 50)

# update()

member = {
  "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"}) # here to add new data to Dictionary
print(member)

print("*" * 50)

# copy()

main = {
  "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"}) # copy data
print(main)
print(b)

# keys() + values()

print(main.keys()) # this like name,skills
print(main.values()) # this like osama,fighting