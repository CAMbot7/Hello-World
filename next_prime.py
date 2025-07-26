import sys

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def next_prime(num: int) -> int:
    candidate = num + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1
def main():
    if len(sys.argv) < 2:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Please provide a valid integer.")
            sys.exit(1)
    else:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer.")
            sys.exit(1)
    print(next_prime(num))
if __name__ == "__main__":
    main()

