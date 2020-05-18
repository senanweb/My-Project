# -----------------
# -- Set Methods --
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)
print("=" * 20)
# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))
print("=" * 20)
# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)
print("=" * 20)
# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)
print("=" * 20)
# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)
print("=" * 20)
# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)
print("=" * 20)
# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())
print("=" * 20)
# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)