def main():
    for x in range (10):
        for y in range (10):
            multiply(x,y)
        print()


def multiply (x,y):
    product = x * y
    print(x, "*", y, "=", product)

main()