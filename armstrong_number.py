n = [153,370,345,678,908]

for i in n:
    total = 0
    temp_n = i
    while temp_n > 0: # 1
        unit_digit = temp_n % 10 # 1
        cube = pow(unit_digit,3) # 1
        total += cube # 27 + 125 + 1 = 153
        temp_n = temp_n // 10



















