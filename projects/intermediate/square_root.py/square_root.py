def sqrt(x: int, steps: int = 10):

    res = x
    for i in range(steps):
        res -= (res**2-x) / (2 * res)

    return res


if __name__ == "__main__":
    print(sqrt(9))
    print(sqrt(2))
