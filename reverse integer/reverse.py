def reverse(x: int) -> int:
    if 10 > x > -10:
        return x
    result: int = 0
    is_sign = x < 0
    if is_sign:
        x = -x
    if x > (pow(2, 31) - 1):
        return 0
    while x > 0:
        y = x % 10
        result = (result * 10) + y
        x = int(x / 10)
    if result > (pow(2, 31) - 1):
        return 0
    if is_sign:
        result = -result
    return result


print(reverse(153423646))
print(reverse(1534236463))
print(reverse(-34236461))
print(reverse(123))
print(reverse(5))
print(reverse(666))
