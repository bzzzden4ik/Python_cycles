import math

x_start, x_end, dx = map(float, input().split())

print("+" + "-" * 10 + "+" + "-" * 10 + "+")
print(f"| {'X':^8} | {'Y':^8} |")
print("+" + "-" * 10 + "+" + "-" * 10 + "+")

while x_start <= x_end:
    if x_start < -10.0 or x_start > 8.0:
        x_start += dx
    else:
        if x_start <= -6.0:
            r = 4.0 - (x_start + 8.0) ** 2
            y = -2.0 + math.sqrt(max(0.0, r))
        elif x_start <= 2.0:
            y = 0.5 * x_start + 1.0
        elif x_start <= 6.0:
            y = 0.0
        else:
            y = (x_start - 6.0) ** 2

        print(f"| {x_start:8.2f} | {y:8.2f} |")

        x_start += dx
