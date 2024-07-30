# for loops

restore = 0
n = 11
for i in range(1, 1+n):
    restore += i

print(restore)


restore1 = 0
i = 1
n = 5

while i <= n:
    restore1 += i
    i += 1
print(restore1)


restore2 = 0
i = 1
n = 8

while i <= n:
    restore2 += i
    i += 1
    i *= 2

print(i)


# Outer loop for rows
for i in range(1, 4):  # i will take values 1, 2, 3
    # Inner loop for columns
    for j in range(1, 4):  # j will take values 1, 2, 3
        product = i * j
        print(product)
# Print a newline for better readability


def recur(n):
    if n == 1:
        return 1
    res = recur(n - 1)
    return n + res


result = recur(3)
print(f"This is the result: {result}")
