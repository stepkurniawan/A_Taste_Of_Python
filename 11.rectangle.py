def main():
    num = int(input("how big: "))
    print_rect(num)

def print_rect(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()

main()