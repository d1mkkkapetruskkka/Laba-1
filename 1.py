def calculate_pi_gregory(num_terms):
    pi_estimate = 0.0
    sign = 1.0

    for i in range(num_terms):
        denominator = 2 * i + 1
        pi_estimate += sign / denominator
        sign *= -1

    pi_estimate *= 4.0
    return pi_estimate


n = 500  # Количество членов ряда
result = calculate_pi_gregory(n)
print("Приближенное значение числа π (по формуле Грегори с", n, "членами ряда):", result)
