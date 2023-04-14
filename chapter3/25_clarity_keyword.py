

def safe_division_c(number, divisor, *,  # Changed
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


def safe_division_d(number, divisor, /, *,  # Changed
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


if __name__ == '__main__':
    # print(safe_division_c(10, 2, False, True))
    # print(safe_division_d(1.0, 2))
    # print(safe_division_d(number=2, divisor=5))
    print(safe_division_d(2, 5, ignore_zero_division=True))
