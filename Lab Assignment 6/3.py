# Making factorial function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

# Making combination function
def combination(n,r):
    return factorial(n) // (factorial(r)* factorial(n-r))

# Making Pascal's triangle function
def Pascal_traingle(rows):
    for i in range(0, rows):
        # Adjust spaces
        for j in range(rows-i):
            print(end=' ')
        # Write elements
        for j in range(0, i+1):
            print(combination(i,j), end = ' ')
        print()

no_of_lines=int(input("Enter number of lines of Pascal's triangle to print: "))
Pascal_traingle(no_of_lines)
