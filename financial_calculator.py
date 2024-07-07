from math import pow


def get_coefficient(n: int, i: float, set_type: str, value_type: str) -> float:
    """
    :param n: Integer representing the number of periods/intervals.
    :param i: Float representing the interest rate.
    :param value_type: String representing the type of value (present or future).
    :param set_type: String representing the type of calculation.
    :return: Float representing the coefficient value.
    """
    if value_type != "pv" and value_type != "fv":
        raise ValueError(f"Unsupported value_type: {value_type}")

    i_dec = i / 100

    if set_type == "begin":
        if value_type == "pv":
            coefficient = ((pow(1 + i_dec, n) - 1) / (i_dec * pow(1 + i_dec, n))) * (1 + i_dec)
        elif value_type == "fv":
            coefficient = (pow((1 + i_dec), n) - 1) / i_dec * (1 + i_dec)
        else:
            coefficient = 0
    elif set_type == "end":
        if value_type == "pv":
            coefficient = (pow(1 + i_dec, n) - 1) / (i_dec * pow(1 + i_dec, n))
        elif value_type == "fv":
            coefficient = (pow(1 + i_dec, n) - 1) / i_dec
        else:
            coefficient = 0
    else:
        raise ValueError(f"Unsupported set value: {set_type}")

    return coefficient


def fv_calculator(n: int, i: float, pmt: float, set_type: str) -> float:
    """
    :param n: Integer representing the number of periods/intervals.
    :param i: Float representing the interest rate.
    :param pmt: Float representing the payment amount.
    :param set_type: String representing the type of calculation.
    :return: Float representing the future value.
    """
    fv_coefficient = get_coefficient(n, i, set_type, "fv")
    fv = pmt * fv_coefficient
    return fv


def pv_calculator(n: int, i: float, pmt: float, set_type: str) -> float:
    """
    :param n: Integer representing the number of periods/intervals.
    :param i: Float representing the interest rate.
    :param pmt: Float representing the payment amount.
    :param set_type: String representing the type of calculation.
    :return: Float representing the present value.
    """
    pv_coefficient = get_coefficient(n, i, set_type, "pv")
    pv = pmt * pv_coefficient
    return pv


def pmt_calculator(n: int, i: float, v: float, value_type: str, set_type: str) -> float:
    """
    :param n: Integer representing the number of periods/intervals.
    :param i: Float representing the interest rate.
    :param v: Float representing the present/future value.
    :param value_type: String representing the type of value (present or future).
    :param set_type: String representing the type of calculation.
    :return: Float representing the payment value.
    """
    coefficient = get_coefficient(n, i, set_type, value_type)
    pmt = v / coefficient
    return pmt


print(fv_calculator(n=6, i=6, pmt=670, set_type="end"))
print(pv_calculator(n=4, i=6, pmt=230, set_type="end"))
print(pmt_calculator(n=8, i=3, value_type="pv", set_type="end", v=8000))
