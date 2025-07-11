print ( "Assignement pattern 15 * ")  
print("*"*15)

# Set the size of the triangle
n = 5

# Pattern 1: Full Pyramid (your specified pattern)
print("Pattern 1: Full Pyramid")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

print("\nPattern 2: Left-aligned Half Pyramid")
for i in range(1, n + 1):
    print("* " * i)

print("\nPattern 3: Right-aligned Half Pyramid")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print("\nPattern 4: Inverted Left-aligned Half Pyramid")
for i in range(n, 0, -1):
    print("* " * i)

print("\nPattern 5: Inverted Right-aligned Half Pyramid")
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print("\nPattern 6: Diamond Pattern")
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "* " * (i + 1))

print("\nPattern 7: Pascal's Triangle")
def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

for i in range(n):
    for j in range(n - i + 1):
        print(" ", end="")

    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

print("\nPattern 8: Hollow Full Pyramid")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
