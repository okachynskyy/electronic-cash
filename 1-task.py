from integersModP import IntegersModP

#Set Dimention
P = 7

#Create field
ZP = IntegersModP(P) 

#Create three instances of class
x = ZP(4)
y = ZP(2)
z = ZP(5)

# -- Arithmetic --
#Addition
print "x+y=%s" % (x+y)
print "x+z=%s" % (x+z)

#Subtraction
print "x-y=%s" % (x-y)
print "x-z=%s" % (x-z)

#Multiplication
print "x*y=%s" % (x*y)
print "x*z=%s" % (x*z)

#Division
print "x/y=%s" % (x/y)

#Multiply by the number
n = 2
print "x*%s=%s" % (n, x*n)

#Power
n = 4
print "y**%s=%s" % (n, y**n)
