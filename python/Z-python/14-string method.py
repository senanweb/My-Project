#spilt() rspilt()
a ="o m a r"
b ="omar"
c ="o-m-a-r"
d ="o-m-a-r"
e ="o-m-a-r"
print(a.split())
print(b.split())
print(c.split("-"))
print(d.split("-", 1))
print(e.rsplit("-", 1))
print("--------------------")
#center()
s = "omar"
print(s.center(8, "#"))
print("-------------------------")
#count()
o = "abcdefabc"
print(o.count("a"))
print(o.count("a", 0, 7))
print("-------------------------")
#swapcase()
n = "omar"
print(n.swapcase())
print("-------------------------")
#startswith
z = "omar"
print(z.startswith("o", 0, 3))
print("-------------------------")
#endswith
z = "omar"
print(z.endswith("r", 3, 4))

