
def get_fact(n):
    """

    :param n:
    :return:
    """
    if n <= 1:
        return 1
    else:
        return n * get_fact(n-1)


print(get_fact(5))
