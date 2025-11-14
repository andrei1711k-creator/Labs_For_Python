from scipy import integrate
def target_func(x):
    return x**3 + 3 * x**2 + 1

start, end = 0, 2
result, error = integrate.quad(target_func, start, end)
print(f"∫[{start}, {end}] (x^3 + 3x^2 + 1) dx = {result}")


def f(y, x):
    return x**2 + 2*y
integral = integrate.dblquad(f, 0, 1, 0, 2)
print(f"Двойной интеграл ∫∫(x^2 + 2y) dxdy = {integral[0]}")
print(f"Границы: внешний ∫dy от 0 до 1, внутренний ∫dx от 0 до 2")