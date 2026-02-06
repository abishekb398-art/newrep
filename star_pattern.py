n = int(input("Enter number of rows: "))

print("\n1. Right Triangle Pattern")
for i in range(1, n + 1):
    print("*" * i)


print("\n2. Inverted Right Triangle Pattern")
for i in range(n, 0, -1):
    print("*" * i)


print("\n3. Pyramid Pattern")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


print("\n4. Square Pattern")
for i in range(n):
    print("*" * n)


print("\n5. Diamond Pattern")

# Upper part
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Lower part
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


print("\n--- Program Finished ---")
