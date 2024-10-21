#numbers are slightly different from the tests because I only used 3.14 for pi
print("What is the diameter of the circle?")
D = float(input())
radius = float(D / 2)
A = float((radius ** 2) * 3.14)
C = float(2 * 3.14 * radius)
print("The area of the circle is:")
print(float(A))
print("The circumference of the circle is:")
print(float(C))

