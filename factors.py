n = int(input("Please enter a positive Integer: "))


for x in range(1,n+1):
    if n%x == 0:
        print(f"{x} is a factor of {n}")


    