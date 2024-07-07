from math import pow


def fv_calculator(n: int, i: float, pmt: float, set_type: str) -> float:
    """
    :param n: Integer representing the number of periods/intervals.
    :param i: Float representing the interest rate.
    :param pmt: Float representing the payment amount.
    :param set_type: String representing the type of calculation.
    :return: Float representing the future value.
    """

    i_dec = i / 100

    if set_type == "begin":
        coefficient = (pow((1 + i_dec), n) - 1) / i_dec * (1 + i_dec)
    elif set_type == "end":
        coefficient = (pow(1+i_dec, n) - 1) / i_dec
    else:
        raise ValueError(f"Unsupported set value: {set_type}")

    fv = pmt * coefficient

    return fv


print(fv_calculator(n=3, i=5, pmt=100, set_type="begin"))
