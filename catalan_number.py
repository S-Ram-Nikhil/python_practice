
# program to find nth Catalan number

# c(0) = c(1) = 1
# c(2) = c0c1 + c1c0 = 1*1+1*1 = 2
# c(3) = c0c2 + c1c1 + c2c0 = 1*2 + 1*1 + 2*1 = 5
# c(4) =  c0c3 + c1c2 + c2c1 + c3c0 = 5 + 2 + 2 + 5 = 14
#  c (n) = c0cn-1 + c1cn-2 + .... + cicn-i +.... cn-1c0


# A recursive function to
# find nth catalan number


def catalan(n):
    """
    :param n: the value given to find catalan number
    :return: retrns the final result
    """
    # Base Case( if there is no base condition it goes to infinite.
    if n <= 1:
        return 1

    # Catalan(n) is the sum
    # of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan(i) * catalan( n - i -1)

    return res


for i in range(10):
    print(catalan(i), end =" ")

# for c(0) and c(1) - zero recursive calls. because these two are assumed to be 1.
# for c(2) - c(1) + c(2) = 2.
print(catalan(3))