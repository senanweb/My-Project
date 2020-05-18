# number of item in object (length)
a = "a b c d e f g"
print(len(a))
print("------------------------")
# to remove the space befor or after the letters
a = "  a b c d e f g  "
print(a.rstrip())
a = "  a b c d e f g  "
print(a.strip())
a = "  a b c d e f g  "
print(a.lstrip())
print("------------------------")
#exm for len and strip
a = "  a b c d e f g  "
print(len(a.rstrip()))
a = "  a b c d e f g  "
print(len(a))
print("------------------------")
#exm for len and strip
a = "### a b c d e f g ###"
print(a.strip("#"))
print(a.rstrip("#"))
print("------------------------")
#title()
a = "a b 2c d 3e f g"
print(a.title())
print("------------------------")
#capitalize()
a = "a b 2c d 3e f g"
print(a.capitalize())
print("------------------------")
#zfill
a, b, c, = "1", "11", "111"
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))
print("------------------------")
#upper()
a ="omar"
print(a.upper())
print("------------------------")
#lower()
a ="OMAR"
print(a.lower())




