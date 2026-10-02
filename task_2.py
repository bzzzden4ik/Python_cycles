ans = 0

for i in range(10, 100):
    number = i * 3
    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10
    
    if (first_digit + second_digit + third_digit) % 5 == 0:
        ans += 1

print(ans)
