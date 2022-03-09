print("+" + "-" * 78 + "+")
i = 1
while i <= 10:
    n = 1
    while n <= 10:
        print("| %4d |" % (i*n), end="")
        n = n + 1
    print(""),
    i = i + 1
print("+" + "-" * 78 + "+")