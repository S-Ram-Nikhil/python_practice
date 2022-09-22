
# fibonacci series up to n terms
n_terms = int(input("no of terms: "))

# first two terms
n1, n2 = 0, 1
counter = 0

if n_terms <= 0:
    print("enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":")
    print(n1)
# generating fibonacci sequence
else:
    print("Fibonacci sequence:")
    while counter < n_terms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        counter += 1
