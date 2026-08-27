def totalWaviness(num1, num2):
    total = 0

    for num in range(num1, num2 + 1):
        digits = [int(d) for d in str(num)]

        if len(digits) < 3:
            continue

        for i in range(1, len(digits) - 1):

            if digits[i] > digits[i-1] and digits[i] > digits[i+1]:
                total += 1

            elif digits[i] < digits[i-1] and digits[i] < digits[i+1]:
                total += 1

    return total


num1 = 120
num2 = 130

print(totalWaviness(num1, num2))