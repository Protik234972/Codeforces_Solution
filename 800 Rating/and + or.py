def find_a_and_b(x):
    if x == 1:
        print("0 1")
    else:
        # Find the highest set bit in x
        highest_bit = 1 << (x.bit_length() - 1)

        # Set a to highest_bit - 1, and b to x XOR a
        a = highest_bit - 1
        b = x ^ a

        print(f"{a} {b}")

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    x = int(input())
    find_a_and_b(x)
