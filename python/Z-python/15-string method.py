#index (subString, start, end)
a = "omar sinan nadom"
print (a.index("s"))  #index number 5
print ("##############")
print (a.index("o"))  #index number 5
print ("##############")
print (a.index("d", 0, 16))  #index number 5
print ("==========================")
#find
b = "omar sinan nadom"
print (a.find("s"))  #find number 5
print ("##############")
print (a.find("o"))  #find number 5
print ("##############")
print (a.find("m", 0, 16))  #find number 5
print ("==========================")
#rjust-ljust
c = "nadom"
print (c.rjust(10, "*"))
print (c.ljust(10, "*"))
print ("==========================")
#splitlines
d = "omar\nsinan\nnadom"
print (d.splitlines())
print ("==========================")
#expandtabs()
e = "omar\tsinan\tnadom"
print (e.expandtabs(10))
print ("==========================")
#isspace()
f = " "
print (f.isspace())
print ("==========================")
#isidentifier()
q = "sinan_10"
z = "sinan10"
v = "sinan-10"
print (q.isidentifier())
print (z.isidentifier())
print (v.isidentifier())

