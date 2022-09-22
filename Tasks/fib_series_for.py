def get_nth_fib(n):
    """
    it gives the value of nth fibonacci number
    :param n: position of the fibonacci number
    :return: gives the value of nth fibonacci number
    """
    fn_2, fn_1 = 0, 1
    if n <= 0:
        print("enter a positive number")
    elif n == 1:
        return fn_2
    elif n == 2:
        return fn_1
    else:
        # for i in range(2, n + 1):
        #     fn = fn_1 + fn_2
        #     fn_1 = fn_2
        #     fn_2 = fn
        fn = get_nth_fib(n-1) + get_nth_fib(n-2)
        return fn


print(get_nth_fib(6))
