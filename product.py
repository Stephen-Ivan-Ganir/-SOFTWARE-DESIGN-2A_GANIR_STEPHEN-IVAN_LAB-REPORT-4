def multiply(m, n):
    if n == 0:
        return 0
    else:
        return m+multiply(m, n-1)

print("Product is: "+ str(multiply(4, 4)))