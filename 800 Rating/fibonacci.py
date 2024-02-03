n = int(input("Enter number: "))
# we already know first and second fibonacci numbers is 0,1 
f1 = 0  # first fibonacci number
f2 = 1  # second fibonacci number

print(f"Fibonacci series upto {n}th number")
print(f1) # print first fibonacci number 0

while n-1 != 0:  # n-1 cause first fibonncci number already printed
    print(f2)

    next_f = f1 + f2  # add previous 2 fibonacci number to get next fibonacci number

    f1,f2 = f2, next_f   # replacing the fib number,  Now f1 store f2 value and f2 store next_f value

    n-=1  # reduce n value -1 after one iteration