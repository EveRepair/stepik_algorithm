def gcd(a, b):
    while b:
        a, b = b, a % b
        print(a)
    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()

#print(gcd(14159572, 63967072))
